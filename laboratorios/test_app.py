import unittest
from app import database, search


class SearchTest(unittest.TestCase):
    def test_known_product(self):
        with database() as db:
            self.assertEqual(search(db, 'book'), [('book', 10)])

    def test_injection_is_literal(self):
        with database() as db:
            self.assertEqual(search(db, "' OR 1=1 --"), [])


if __name__ == '__main__':
    unittest.main()
