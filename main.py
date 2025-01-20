def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    sorted = get_sorted_list(num_chars)


    print(f'--- Begin report of {book_path} ---')
    print(f'{num_words} words found in the document')
    print()

    for thing in sorted:
        if not thing["char"].isalpha():
            continue
        print(f"The '{thing['char']}' character was found {thing['num']} times")

    print("--- End report ---")




def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_chars(text):
    num_chars = {}
    lower_text = text.lower()
    for char in lower_text:
        if char in num_chars:
            num_chars[char] += 1
        else:
            num_chars[char] = 1

    return(num_chars)


def sort_on(d):
    return d["num"]



def get_sorted_list(dict):
    new_list = []
    for entry in dict:
        new_list.append({"char": entry, "num": dict[entry]})
    new_list.sort(reverse=True, key=sort_on)
    return(new_list)




main()
