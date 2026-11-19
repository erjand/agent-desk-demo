"""Small functions for everyday text."""

import re
import unicodedata

__all__ = ["reverse_words", "strip_accents", "title_case", "word_count"]


_WORD = re.compile(r"[^\W\d_]+(?:'[^\W\d_]+)*")


def title_case(text):
    """Capitalize the first letter of each word, where an apostrophe between letters stays inside the word."""
    return _WORD.sub(lambda match: match.group().capitalize(), text)


def word_count(text):
    """Count the words in text, where a word is a run of letters, digits, or apostrophes."""
    return len(re.findall(r"[\w']+", text))


def reverse_words(text):
    """Reverse the order of the words in text, joining them with single spaces."""
    return " ".join(reversed(text.split()))


def strip_accents(text):
    """Remove accents from letters, so that "café" becomes "cafe"."""
    decomposed = unicodedata.normalize("NFKD", text)
    return "".join(char for char in decomposed if not unicodedata.combining(char))
