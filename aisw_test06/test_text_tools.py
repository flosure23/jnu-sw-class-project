# test_text_tools.py

import unittest
from text_tools import TextTools

class TestTextTools(unittest.TestCase):
    def setUp(self):
        self.tool = TextTools()

    def test_count_words_basic(self):
        result = self.tool.count_words("python unit test practice")
        self.assertEqual(result, 4)

    def test_count_words_empty(self):
        result = self.tool.count_words("")
        self.assertEqual(result, 0)

    def test_contains_word_true(self):
        result = self.tool.contains_word("python unittest coverage", "unittest")
        self.assertTrue(result)

    def test_contains_word_false(self):
        result = self.tool.contains_word("python unittest coverage", "mock")
        self.assertFalse(result)

    def test_make_upper(self):
        result = self.tool.make_upper("hello")
        self.assertEqual(result, "HELLO")
    
    def test_count_words_basic(self):
        result = self.tool.count_words("python unit test practice")
        self.assertEqual(result, 4)

if __name__ == "__main__":
    unittest.main(verbosity=2)