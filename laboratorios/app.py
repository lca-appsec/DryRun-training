"""Aplicacao didatica: somente loopback; nenhuma autenticacao real."""
import json
import sqlite3
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse


def database():
    db = sqlite3.connect(':memory:')
    db.execute('CREATE TABLE products (name TEXT, price INTEGER)')
    db.executemany('INSERT INTO products VALUES (?, ?)',
                   [('book', 10), ('pencil', 2)])
    return db


def search(db, term):
    return db.execute(
        'SELECT name, price FROM products WHERE name = ?',
        (term,)).fetchall()


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path != '/search':
            self.send_error(404)
            return
        term = parse_qs(parsed.query).get('q', [''])[0]
        with database() as db:
            result = search(db, term)
        body = json.dumps(result).encode()
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(body)


if __name__ == '__main__':
    HTTPServer(('127.0.0.1', 8090), Handler).serve_forever()
