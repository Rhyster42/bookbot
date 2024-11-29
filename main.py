def main():
   book_file = "books/frankenstein.txt"
   text = get_text (book_file)
   word_count = word_counter(text)
   chars_dict = get_chars_dict(text)
   print(chars_dict)

def get_text(path):
    with open(path) as f:
        return f.read()
    # inputs a path to a txt file, outputs the text in a variable

def word_counter(text):
    words = text.split()
    return len(words)
    # counts number of words in a text file

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars
    # generates dictionary of characters in a text file
    
    
main()