def main():
    book_path = "books/frankenstein.txt"
    text = read(book_path)
    num_words = get_num_words(text)
    char_dict = get_chars(text)
    sorted_dict_list = convert_dict(char_dict)

    print("--- Beginning of book report ---\n")
    print(f"{num_words} words found in the document\n")
    for slist in sorted_dict_list:
        if not slist["char"].isalpha():
            continue
        print(f"The '{slist['char']}' character was found {slist['num']} times")
    print("End Report")


def read(path):
    with open(path) as f:
        return f.read()


def get_num_words(text):
    num_words = text.split()
    return len(num_words)


def len_split_text(text):
    return len(text.split())


def sort_on(dict):
    return dict["num"]


def convert_dict(num_chars_dict):
    sort_list = []
    for ch in num_chars_dict:
        sort_list.append({"char": ch, "num": num_chars_dict[ch]})
    sort_list.sort(reverse=True, key=sort_on)
    return sort_list


def get_chars(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


main()
