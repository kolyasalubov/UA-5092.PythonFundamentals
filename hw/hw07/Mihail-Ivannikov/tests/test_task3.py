import unittest
from task3 import count_characters

class TestTask3FunctionCountCharacters(unittest.TestCase):
    
    def test_count_characters_function(self):
        self.assertEqual(count_characters("hello"), {"h": 1, "e": 1, "l": 2, "o": 1})