import unittest
from datetime import datetime
from option_1 import *
from option_2 import *
from option_3 import *
from option_4 import *
from option_5 import *
from helpers import *

class TestSolutions(unittest.TestCase):
    def test_connect_db(self):
        test_db = connect_db("test.db")
        self.assertIsInstance(test_db, sqlite3.Connection)

    def test_query_option_1(self):
        connect_db("test.db")
        rows = query_option_1(datetime(1995, 12, 10))
        self.assertEqual(rows[0][0], 135202)
    
    def test_query_option_2(self):
        connect_db("test.db")
        rows = query_option_2(2017)
        self.assertEqual(len(rows), 11)

    def test_query_option_3(self):
        connect_db("test.db")
        rows = query_option_3("Monica")
        self.assertEqual(rows[0][2], 32)

    def test_query_option_4(self):
        connect_db("test.db")
        rows = query_option_4(1987)
        self.assertEqual(rows[0][0], "You Keep Me Hangin' On")
    
    def test_query_option_5(self):
        connect_db("test.db")
        rows = query_option_5(1958)
        self.assertEqual(len(rows), 8)
        self.assertEqual(rows[7], ("Tom Dooley", 1))