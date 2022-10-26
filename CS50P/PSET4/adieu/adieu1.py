import sys

names = []

while True:
    try:
        names.append(input("").strip())
    except EOFError:
        break

print(f"Adieu, adieu, to", end = " ")

if len(names) == 2:
    print(f"{names[0]} and {names[1]}  ")

else:
    for name in names[:-1]:

        print(f"{name}, ", end = "")

    if len(names) > 1:

        print("and", end = " ")

    print(names[len(names)-1])




