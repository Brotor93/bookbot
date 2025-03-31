import sys
from stats import get_num_words, get_char_counts, sort_char_counts

def get_book_text(filepath):
    """Reads the contents of a file and returns it as a string."""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print("Error: File not found. Please check the filepath.")
        sys.exit(1)

def main():
    """Main function to read and analyze a book from the given filepath."""
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]  # Get book file path from command-line argument
    book_text = get_book_text(filepath)
    
    num_words = get_num_words(book_text)
    char_counts = get_char_counts(book_text)
    sorted_char_counts = sort_char_counts(char_counts)

    # Print the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_char_counts:
        print(f"{item['char']}: {item['count']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()
