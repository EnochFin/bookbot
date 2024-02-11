A_ASCII = ord('a')
Z_ASCII = ord('z')

def main():
    book_path = 'books/frankenstein.txt'
    with open(book_path) as f:
        print(f'--- Begin report of {book_path} ---')
        file_contents = f.read()
        occ = get_occurances(file_contents.lower())
        for k, v in occ:
            print(f"The '{k}' character was found {v} times")
        print("--- End report ---")

def valid_char(k):
    _, v = k
    return v != 0 

def init_chars():
    characters = {}
    for x in range(A_ASCII, Z_ASCII + 1):
        characters[chr(x)] = 0
    return characters

def sort_on(o):
    _, v = o
    return v

def get_occurances(val):
    characters = init_chars()

    for c in val:
        if c not in characters:
            continue
        characters[c] += 1

    found_chars = [c for c in characters.items() if valid_char(c)] 

    found_chars.sort(reverse=True, key=sort_on)

    return found_chars

main()