def main():
    #book = "books/frankenstein.txt"
    book = "/home/ronald/src/boot.dev/04-Build-a-Bookbot/bookbot/books/frankenstein.txt"
    text = get_book_text(book)
    words = word_count(text)
    letters = get_letters(text)
    print(f"{words} words found in the book")
    print(f"{letters}")
    return 0

def get_book_text(b):
    with open(b) as f:
        return f.read()

def word_count(text):
    words = text.split()
    return len(words)

def get_letters(text):
    letters = {}
    words = text.split()
    for word in words:
        word = word.lower()
        for letter in word:
            if (letter not in letters):
                letters[letter] = 1
            else:
                letters[letter] += 1
    return letters

main()
