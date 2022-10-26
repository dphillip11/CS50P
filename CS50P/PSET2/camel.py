text = input("I change camels to snakes!")

capitals = []
for i in range (len(text)):
    if text[i].isupper():
        capitals += text[i]

for letter in capitals:
    text = text.replace(letter, "_" + letter.lower())
print(text)


