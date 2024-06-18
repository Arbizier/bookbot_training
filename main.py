
def main():
    book_path = "books/frankenstein.txt"
    text = read(book_path)
    print(len_split_text(text))


def read(path): 
    with open(path) as f: 
         return f.read()

def len_split_text(text):
    return len(text.split())

main()