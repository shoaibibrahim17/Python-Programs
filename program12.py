def read_file_and_get_unique_words(file_path):
    """
    Reads a text file and returns a set of unique words.

    Args:
    file_path (str): The path to the text file.

    Returns:
    set: A set containing all unique words from the file.
    """
    unique_words = set()
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # Split the line into words, removing punctuation and converting to lowercase
                words = line.strip().lower().split()
                words = [word.strip('.,!?()[]{}"\'') for word in words]
                unique_words.update(words)
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return unique_words

def main():
    file_path = input("Please enter the path to the text file: ")
    unique_words = read_file_and_get_unique_words(file_path)
    
    if unique_words:
        print("Unique words found in the file:")
        for word in sorted(unique_words):
            print(word)
    else:
        print("No unique words were found or an error occurred.")

if __name__ == "__main__":
    main()
