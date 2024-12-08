# Function to count vowels in a given string
def count_vowels_in_string(text):
    # Define a set of vowels for quick lookup
    vowels_set = set('aeiouAEIOU')  # Both lowercase and uppercase
    
    # Count vowels by checking each character in the string
    vowel_count = sum(1 for char in text if char in vowels_set)
    
    # Return the total count of vowels
    return vowel_count


# Main execution block
if __name__ == "__main__":
    # Prompt the user for input
    user_input = input("Enter a string to count vowels: ")
    
    # Display the original string entered by the user
    print("Input String:", user_input)
    
    # Call the function and print the number of vowels found
    print("Vowel Count:", count_vowels_in_string(user_input))
