def count_vowels(s):
    """
    This function takes a string as an argument and returns the number of vowels in it.
    """
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

def count_consonants(s):
    """
    This function takes a string as an argument and returns the number of consonants in it.
    """
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    return sum(1 for char in s if char in consonants)

# Example usage
if __name__ == "__main__":
    test_string = "Hello World"
    print(f"The number of vowels in '{test_string}' is: {count_vowels(test_string)}")
    print(f"The number of consonants in '{test_string}' is: {count_consonants(test_string)}")
