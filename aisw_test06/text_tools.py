# text_tools.py

class TextTools:
    def count_words(self, text):
        if text.strip() == "":
            return 0
        return len(text.split())

    def contains_word(self, text, word):
        words = text.split()
        return word in words

    def make_upper(self, text):
        return text.upper()