import unittest

from tinytext import reverse_words, strip_accents, title_case, word_count


class TitleCaseTest(unittest.TestCase):
    def test_capitalizes_each_word(self):
        self.assertEqual(title_case("the quick brown fox"), "The Quick Brown Fox")

    def test_lowers_the_rest_of_each_word(self):
        self.assertEqual(title_case("hELLO wORLD"), "Hello World")


class WordCountTest(unittest.TestCase):
    def test_counts_words(self):
        self.assertEqual(word_count("one two three"), 3)

    def test_counts_a_non_breaking_hyphen_as_a_hyphen(self):
        self.assertEqual(word_count("a well‑known fact"), 3)

    def test_ignores_punctuation_and_extra_spaces(self):
        self.assertEqual(word_count("  Hello,   world!  "), 2)

    def test_empty_text_has_no_words(self):
        self.assertEqual(word_count(""), 0)

    def test_counts_hyphenated_word_once(self):
        self.assertEqual(word_count("a well-known fact"), 3)

    def test_spaced_hyphen_is_no_word(self):
        self.assertEqual(word_count("one - two"), 2)


class ReverseWordsTest(unittest.TestCase):
    def test_reverses_word_order(self):
        self.assertEqual(reverse_words("one two three"), "three two one")

    def test_collapses_spaces(self):
        self.assertEqual(reverse_words("  a   b "), "b a")


class StripAccentsTest(unittest.TestCase):
    def test_removes_accents(self):
        self.assertEqual(strip_accents("café crème"), "cafe creme")

    def test_leaves_plain_text_alone(self):
        self.assertEqual(strip_accents("plain"), "plain")


if __name__ == "__main__":
    unittest.main()
