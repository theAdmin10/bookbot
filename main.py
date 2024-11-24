with open("/home/ronald/src/boot.dev/04-Build-a-Bookbot/bookbot/books/frankenstein.txt") as f:
    file_contents = f.read()

words = file_contents.split()
print(len(words))
