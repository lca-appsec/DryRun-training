"""Altera apenas app.py no repositorio didatico, com checagem de estado."""
import pathlib
import sys
p = pathlib.Path('app.py')
safe = """return db.execute(
        'SELECT name, price FROM products WHERE name = ?',
        (term,)).fetchall()"""
unsafe = """query = "SELECT name, price FROM products WHERE name = '" + term + "'"
    return db.execute(query).fetchall()"""
mode = sys.argv[1]
assert mode in ('unsafe', 'safe')
before, after = (safe, unsafe) if mode == 'unsafe' else (unsafe, safe)
text = p.read_text()
if text.count(before) != 1:
    raise SystemExit('Estado inesperado de app.py; revise o diff.')
p.write_text(text.replace(before, after))
