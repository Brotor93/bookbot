from stats import get_num_words

def get_book_text(filepath):
    """Reads the contents of a file and returns it as a string."""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "Error: File not found. Please check the filepath."

def main():
    """Main function to read and count the words in frankenstein.txt."""
    filepath = "books/frankenstein.txt"  # Adjust the path if needed
    book_text = get_book_text(filepath)
    if "Error:" not in book_text:
        num_words = count_words(book_text)
        print(f"{num_words} words found in the document")
    else:
        print(book_text)

if __name__ == "__main__":
    main()