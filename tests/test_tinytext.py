import unittest

from tinytext import reverse_words, slugify, strip_accents, title_case, word_count


class TitleCaseTest(unittest.TestCase):
    def test_capitalizes_each_word(self):
        self.assertEqual(title_case("the quick brown fox"), "The Quick Brown Fox")

    def test_lowers_the_rest_of_each_word(self):
        self.assertEqual(title_case("hELLO wORLD"), "Hello World")


class WordCountTest(unittest.TestCase):
    def test_counts_words(self):
        self.assertEqual(word_count("one two three"), 3)

    def test_ignores_punctuation_and_extra_spaces(self):
        self.assertEqual(word_count("  Hello,   world!  "), 2)

    def test_empty_text_has_no_words(self):
        self.assertEqual(word_count(""), 0)


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


class SlugifyTest(unittest.TestCase):
    def test_lowercases_and_joins_words_with_hyphens(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_collapses_runs_and_trims_hyphens(self):
        self.assertEqual(slugify("  --Tips & Tricks--  "), "tips-tricks")

    def test_keeps_digits(self):
        self.assertEqual(slugify("Top 10 Python Tips"), "top-10-python-tips")

    def test_strips_accents(self):
        self.assertEqual(slugify("Café crème"), "cafe-creme")

    def test_drops_letters_outside_latin_scripts(self):
        self.assertEqual(slugify("Tokyo 東京 guide"), "tokyo-guide")

    def test_empty_text_gives_empty_slug(self):
        self.assertEqual(slugify(""), "")

    def test_punctuation_only_gives_empty_slug(self):
        self.assertEqual(slugify("!!!"), "")


if __name__ == "__main__":
    unittest.main()
