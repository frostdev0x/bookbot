from stats import *


def main():
    num_words = get_num_words()
    print(f"""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------""")
    sorted_report()
    print("============= END ===============")
main()
