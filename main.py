def main():
   book_file = "books/frankenstein.txt"
   text = get_text (book_file)
   word_count = word_counter(text)
   print(f"{word_count} words found in the document")

def get_text(path):
    with open(path) as f:
        return f.read()
    # inputs a path to a txt file, outputs the text in a variable

def word_counter(text):
    words = text.split()
    return len(words)
    # counts number of words in a text file
    
    
main()