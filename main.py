def main():
   book_file = "books/frankenstein.txt"
   text = get_text (book_file)
   word_count = word_counter(text)
   chars_dict = get_chars_dict(text)
   chars_list = get_chars_list(chars_dict)

   print(build_report(chars_list))

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

def get_chars_list(chars):
    char_list = []
    for c in chars:
        if c.isalpha() == True:
            letter_dict = {"letter": c, "num": chars[c]}
            char_list.append(letter_dict)
    char_list.sort(reverse=True, key=lambda x: x["num"])
    return char_list
    # generates a list of dictionaries, then sorts them in descending order of occurence.
    
    
main()