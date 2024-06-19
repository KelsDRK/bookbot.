def main():
    book_path = "/Users/Kels/workspace/bookbot./books/frankenstein.txt"
    text = get_book_text(book_path)
    count = count_words(text)
    character_list = count_each_character(text)
    print(text)
    print(count)
    print(character_list)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

def count_each_character(text):
    character_list = {}
    for c in text:
        lowered = c.lower()
        if lowered in character_list:
            character_list[lowered] += 1
        else:
            character_list[lowered] = 1
    return character_list

main()