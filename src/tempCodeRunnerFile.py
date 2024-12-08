import argparse
from .vowel_counter import count_vowels_in_string
from .advanced_vowel_counter import count_each_vowel

def main():
    """
    Main function to handle CLI arguments and execute the appropriate functionality.
    Provides options for total vowel count and detailed vowel breakdown.
    """
    # Setup argument parser for CLI options
    parser = argparse.ArgumentParser(description="Count vowels in a string.")
    parser.add_argument("text", type=str, help="The string to analyze.")  # Input string
    parser.add_argument("--detail", action="store_true", help="Show detailed vowel counts.")  # Detailed option
    parser.add_argument("--total", action="store_true", help="Show total count of vowels.")  # Total count option
    args = parser.parse_args()

    # Execute the appropriate function based on arguments
    if args.detail:
        result = count_each_vowel(args.text)  # Detailed vowel count
        print(f"Vowel Count (Detailed): {result}")
    elif args.total or not args.detail:
        total = count_vowels_in_string(args.text)  # Total vowel count
        print(f"Total Vowel Count: {total}")
    else:
        print("No valid option selected. Use --help for usage details.")  # Fallback message

if __name__ == "__main__":
    main()

# python -m src.cli "Hello World"
# python -m src.cli "Hello World" --detail