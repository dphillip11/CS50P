text = input("text: ")
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
for vowel in vowels:
    text = text.replace(vowel, "")
print(text)