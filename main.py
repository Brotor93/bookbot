def get_book_text(books/frankenstein.txt):
    """Reads the contents of a file and returns it as a string."""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "Error: File not found. Please check the filepath."

def main():
    """Main function to read and print the contents of frankenstein.txt."""
    filepath = "books/frankenstein.txt"  # Adjust the path if needed
    book_text = get_book_text(filepath)
    print(book_text)

if __name__ == "__main__":
    main()