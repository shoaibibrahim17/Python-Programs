def create_and_write_file(file_path, content):
    """
    Creates a file and writes the given content to it.

    :param file_path: Path to the file to be created.
    :param content: Content to be written to the file.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        print(f"File '{file_path}' created and content written successfully.")
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")

def display_file_content(file_path):
    """
    Displays the content of the specified file.

    :param file_path: Path to the file whose content is to be displayed.
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(f"Content of the file '{file_path}':\n{content}")
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
    except IOError as e:
        print(f"An error occurred while reading the file: {e}")

if __name__ == "__main__":
    file_path = 'example.txt'
    content = 'Hello, this is a sample content written to the file.'

    create_and_write_file(file_path, content)
    display_file_content(file_path)
