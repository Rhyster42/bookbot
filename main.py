def main():
   book_file = "books/frankenstein.txt"
   text = get_text (book_file)
   print(text)

def get_text(path):
    with open(path) as f:
        return f.read()
    
main()