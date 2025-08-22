
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def get_num_words():
    num_words = 0
    book_text= get_book_text('books/frankenstein.txt')
    split_book_text = book_text.split()
    for i in split_book_text:
        num_words += 1
    print(f"{num_words} words found in the document")


def count_characters():
    book_text = get_book_text('books/frankenstein.txt')
    book_text_lower = book_text.lower()
    char_count = {}
    for char in book_text_lower:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
