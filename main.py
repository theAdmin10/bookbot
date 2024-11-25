def main():
    #book = "books/frankenstein.txt"
    book = "/home/ronald/src/boot.dev/04-Build-a-Bookbot/bookbot/books/frankenstein.txt"
    text = get_book_text(book)
    words = word_count(text)
    letters = get_letters(text)
    sorted_letters = sort_letters_dict(letters)

    print(f"--- Begin report of {book} ---")
    print(f"{words} words found in the document")
    print()

    for letter in sorted_letters:
        if not letter["letter"].isalpha():
            continue
        print(f"The '{letter['letter']}' character was found {letter['num']} times")

    print("--- End report ---")
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
            if letter.isalpha():
                if (letter not in letters):
                    letters[letter] = 1
                else:
                    letters[letter] += 1
    return letters

def sort_letters_dict(letters):
    sorted_list = []
    for letter in letters:
        sorted_list.append({"letter": letter, "num": letters[letter]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    
def sort_on(dict):
    return dict["num"]

main()
