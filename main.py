
from stats import num_words
from stats import num_chars
from stats import sort_chars
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book = sys.argv[1]
    text = get_book_text(book)
    words = num_words(text)
    chars = num_chars(text)
    sorted_chars = sort_chars(chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for char in sorted_chars:
        if char['name'].isalpha():
            print(f"{char['name']}: {char['num']}")
    print("============= END ===============")







def get_book_text(filepath):
    with open(filepath) as f:

        return f.read()


main()