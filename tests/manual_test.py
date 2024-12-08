from src.vowel_counter import count_vowels_in_string
from src.advanced_vowel_counter import count_each_vowel



def test_count_vowels_in_string():
    """Manually test the count_vowels_in_string function."""
    assert count_vowels_in_string("") == 0, "Failed on empty string"
    assert count_vowels_in_string("bcdfgh") == 0, "Failed on string with no vowels"
    assert count_vowels_in_string("aeiou") == 5, "Failed on string with only vowels"
    assert count_vowels_in_string("AEIOUaeiou") == 10, "Failed on mixed-case vowels"
    assert count_vowels_in_string("hello world") == 3, "Failed on mixed characters"
    print("All tests passed for count_vowels_in_string")


def test_count_each_vowel():
    """Manually test the count_each_vowel function."""
    assert count_each_vowel("") == {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}, "Failed on empty string"
    assert count_each_vowel("bcdfgh") == {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}, "Failed on string with no vowels"
    assert count_each_vowel("aeiou") == {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}, "Failed on string with only vowels"
    assert count_each_vowel("AEIOUaeiou") == {'a': 2, 'e': 2, 'i': 2, 'o': 2, 'u': 2}, "Failed on mixed-case vowels"
    assert count_each_vowel("hello world") == {'a': 0, 'e': 1, 'i': 0, 'o': 2, 'u': 0}, "Failed on mixed characters"
    print("All tests passed for count_each_vowel")


if __name__ == "__main__":
    # Run both test functions
    test_count_vowels_in_string()
    test_count_each_vowel()


## python -m tests.manual_test
