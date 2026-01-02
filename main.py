import sys
from stats import get_num_words, get_char_count, get_sorted_char_count_list

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    # frankenstein_file_path = "./books/frankenstein.txt"
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_contents = get_book_text(sys.argv[1])
    num_words = get_num_words(book_contents)
    # print(f"Found {num_words} total words")
    char_dict = get_char_count(book_contents)
    # print(char_dict)
    # print(get_sorted_char_count_list(char_dict))
    sorted_char_count_list = get_sorted_char_count_list(char_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_char_count_list:
        if char["char"].isalpha():
            print(f'{char["char"]}: {char["num"]}')
    print("============= END ===============")

main()