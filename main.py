def word_count(file_contents):
    words = file_contents.split()
    return len(words)

def character_count(file_contents):
    characters = {}
    contents_lower = file_contents.lower()
    for char in contents_lower:
        if char.isalpha():
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1
    return characters

def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        word_count_result = word_count(file_contents)
        characters = character_count(file_contents)
        
        char_list = []
        for char, count in characters.items():
            char_list.append({"char": char, "count": count})
        char_list.sort(reverse=True, key=lambda x: x["count"])
        #print(file_contents)
        #print(word_count(file_contents))
        #print(character_count(file_contents))
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count_result} words found in the document\n")
        for char_data in char_list:
            print(f"The '{char_data["char"]}' character was found {char_data["count"]} times")
        print("--- End report ---")

main()
