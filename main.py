def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    word = get_number_of_word(text)
    print(word)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_number_of_word(text):
    number_of_words = 0
    for word in text.split():
        number_of_words += 1
    return number_of_words

main()
