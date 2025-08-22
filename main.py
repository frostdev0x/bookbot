from stats import *


def main():
    book_text = get_book_text('books/frankenstein.txt')
    print(book_text)
    get_num_words()
    frequencies = count_characters()
    print(frequencies)

main()
