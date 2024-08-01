def read_file_to_set(file_path):
    """Reads the contents of a file and returns a set of words."""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        words = content.split()
        return set(words)

def analyze_files(file1_path, file2_path):
    """Analyzes the contents of two text files using set operations."""
    set1 = read_file_to_set(file1_path)
    set2 = read_file_to_set(file2_path)

    # Common elements in both files
    common_elements = set1.intersection(set2)

    # Unique elements in each file
    unique_elements_file1 = set1 - set2
    unique_elements_file2 = set2 - set1

    # All elements from both files
    all_elements = set1.union(set2)

    return common_elements, unique_elements_file1, unique_elements_file2, all_elements

def main():
    file1_path = 'file1.txt'  # Replace with the path to your first text file
    file2_path = 'file2.txt'  # Replace with the path to your second text file

    common_elements, unique_elements_file1, unique_elements_file2, all_elements = analyze_files(file1_path, file2_path)

    print("Common elements in both files:", common_elements)
    print("Unique elements in file1:", unique_elements_file1)
    print("Unique elements in file2:", unique_elements_file2)
    print("All elements from both files:", all_elements)

if __name__ == "__main__":
    main()
