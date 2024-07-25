def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(f"Word Count:", word_count(text))
    list = create_list(character_count(text))
    sort_characters(list)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def word_count(file):
    word_list = file.split()
    return len(word_list)

def character_count(text):
    characters = {}
    lowered_string = text.lower()
    for character in lowered_string:
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    return characters

def sort_on(dict):
    return dict["count"]

def create_list(dict):
    list = []
    for character in dict:
        list.append({"char": character, "count": dict[character]})
    list.sort(reverse=True, key=sort_on)
    return list

def sort_characters(list):
    for char in list:
        if char["char"].isalpha():
             print(f"The '{char['char']}' character was found {char['count']} times")

main()