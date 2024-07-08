def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    print(f"Word Count:", word_count(text))

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def word_count(file):
    word_list = file.split()
    return len(word_list)

main()