import re


def main():
    print(count(input("Text: ")))


def count(s):
    s = " " + s + " "
    ums = re.findall(r"\W(um)\W", s, re.IGNORECASE)
    return len(ums)


if __name__ == "__main__":
    main()
