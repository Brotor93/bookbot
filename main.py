from stats import get_num_words, get_char_counts, sort_char_counts

def get_book_text(filepath):
    """Reads the contents of a file and returns it as a string."""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "Error: File not found. Please check the filepath."

def main():
    """Main function to read and analyze frankenstein.txt."""
    filepath = "books/frankenstein.txt"  # Adjust path if needed
    book_text = get_book_text(filepath)
    
    if book_text.startswith("Error:"):
        print(book_text)
    else:
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
