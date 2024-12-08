import unittest
from src.vowel_counter import count_vowels_in_string
from src.advanced_vowel_counter import count_each_vowel


class TestVowelCounter(unittest.TestCase):
    def test_count_vowels_in_string(self):
        """Test the total vowel count function."""
        self.assertEqual(count_vowels_in_string(""), 0, "Failed on empty string")
        self.assertEqual(count_vowels_in_string("bcdfgh"), 0, "Failed on string with no vowels")
        self.assertEqual(count_vowels_in_string("aeiou"), 5, "Failed on string with vowels only")
        self.assertEqual(count_vowels_in_string("AEIOUaeiou"), 10, "Failed on mixed-case vowels")
        self.assertEqual(count_vowels_in_string("hello world"), 3, "Failed on mixed characters")

    def test_count_each_vowel(self):
        """Test the detailed vowel count function."""
        self.assertEqual(
            count_each_vowel(""), 
            {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}, 
            "Failed on empty string"
        )
        self.assertEqual(
            count_each_vowel("bcdfgh"), 
            {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}, 
            "Failed on string with no vowels"
        )
        self.assertEqual(
            count_each_vowel("aeiou"), 
            {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}, 
            "Failed on string with vowels only"
        )
        self.assertEqual(
            count_each_vowel("AEIOUaeiou"), 
            {'a': 2, 'e': 2, 'i': 2, 'o': 2, 'u': 2}, 
            "Failed on mixed-case vowels"
        )
        self.assertEqual(
            count_each_vowel("hello world"), 
            {'a': 0, 'e': 1, 'i': 0, 'o': 2, 'u': 0}, 
            "Failed on mixed characters"
        )


if __name__ == "__main__":
    # Run tests with verbosity for detailed output
    unittest.main(verbosity=2)



##python -m unittest discover -s tests -v
