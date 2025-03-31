def get_num_words(text):
    """Counts the number of words in a given text string."""
    return len(text.split())

def get_char_counts(text):
    """Counts the number of times each character appears in the text."""
    text = text.lower()  # Convert all characters to lowercase
    char_counts = {}  # Dictionary to store character frequencies

    for char in text:
        char_counts[char] = char_counts.get(char, 0) + 1  # Update count

    return char_counts
