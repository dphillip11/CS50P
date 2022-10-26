def main():
    text = input("text: ")
    print(text)

def shorten(word):
    vowels = ["a", "e", "i", "o", "u","A", "E", "I", "O", "U"]
    for vowel in vowels:
        word = word.replace(vowel, "")
    return word

if __name__ == "__main__":
    main()