def get_char_counts(contents):
    counts = {}
    for letter in contents.lower():
        if letter not in counts:
            counts[letter] = 1
        else:
            counts[letter] += 1
    return counts

def get_word_count(contents):
    return len(contents.split())

def get_book_contents(path):
    with open(path) as f:
        return f.read()

def print_report(path):
    contents = get_book_contents(path)
    print(f"--- Begin report of {path} ---")
    print(f"{get_word_count(contents)} words found in the document")
    print()
    counts = get_char_counts(contents)
    characters = list(counts)
    characters.sort()
    for char in characters:
        if char.isalpha():
            print(f"The '{char}' character was found {counts[char]} times")
    print("--- End report ---")

def __main__():
    book_path = "./books/frankenstein.txt"
    print_report(book_path)

if __name__ == '__main__':
    __main__()