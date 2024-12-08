# Function to count occurrences of each vowel in a string
def count_each_vowel(text):
    # Initialize a dictionary with vowels set to 0
    vowels_count = {vowel: 0 for vowel in 'aeiou'}

    # Count each vowel occurrence
    for char in text.lower():  # Convert to lowercase for simplicity
        if char in vowels_count:
            vowels_count[char] += 1
    
    return vowels_count

# Main execution block
if __name__ == "__main__":
    # Prompt the user for input
    user_input = input("Enter a string to count vowels: ")
    
    # Call the function and print the result as a dictionary
    result = count_each_vowel(user_input)
    print(result)
