def count_characters(s):
    frequencies = {}
    for character in s.lower():
        if character in frequencies:
            frequencies[character] += 1
        else:
            frequencies[character] = 1
    return frequencies

def count_words(s):
    return len(s.split())

def read_file(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    contents = read_file(book_path)
    word_count = count_words(contents)
    char_count = count_characters(contents)
    sorted_chars = sorted(char_count, reverse=True, key=lambda item: char_count[item])
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the docment")
    print()
    for key in sorted_chars:
        if key.isalpha():
            print(f"The \'{key}\' character was found {char_count[key]} times")
    print("--- End report ---")

main()
