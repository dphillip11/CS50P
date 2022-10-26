import sys
import inflect

p = inflect.engine()

names = []

while True:
    try:
        names.append(input("").strip())
    except EOFError:
        break

text = p.join(names, final_sep=",")
print(f"Adieu, adieu, to " + text)