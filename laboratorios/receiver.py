"""Receptor de laboratorio. Captura JSON; nao encaminha automaticamente ao Jira."""
import hashlib
import hmac
import json
import os
from pathlib import Path
from http.server import BaseHTTPRequestHandler, HTTPServer

KEY = os.environ['WEBHOOK_PATH_KEY']
OUT = Path('.evidence/events')
OUT.mkdir(parents=True, exist_ok=True)


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass  # Nao registrar a URL que contem o segredo do laboratorio.

    def do_POST(self):
        if not hmac.compare_digest(self.path, '/hook/' + KEY):
            self.send_error(404)
            return
        try:
            size = int(self.headers.get('Content-Length', '0'))
            if not 0 < size <= 1024 * 1024:
                self.send_error(413)
                return
            data = json.loads(self.rfile.read(size))
            if not isinstance(data, dict):
                raise ValueError('Objeto JSON esperado')
        except (ValueError, json.JSONDecodeError):
            self.send_error(400)
            return
        raw = json.dumps(data, sort_keys=True).encode()
        digest = hashlib.sha256(raw).hexdigest()
        dest = OUT / (digest + '.json')
        try:
            with dest.open('xb') as f:
                f.write(raw)
            print('Evento salvo:', dest, flush=True)
        except FileExistsError:
            print('Repeticao ignorada:', digest, flush=True)
        self.send_response(202)
        self.end_headers()
        self.wfile.write(b'{"accepted":true}')


if __name__ == '__main__':
    HTTPServer(('127.0.0.1', 8080), Handler).serve_forever()
