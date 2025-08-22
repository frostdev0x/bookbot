import sys
from stats import *


def main():
    if len(sys.argv) != 2: 
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    num_words = get_num_words(book_path)
    print(f"""============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------""")
    sorted_report(book_path)
    print("============= END ===============")
main()
