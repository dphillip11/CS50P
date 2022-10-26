def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #check length of plate
    length = len(s)
    if not 2<= length <= 6:
        return False

    for i in range(2):
        if not s[i].isalpha():
            return False

    #check all characters are letters or numbers
    for character in s:
        if not (character.isalpha() or character.isdigit()):
            return False

    # first number not equal to 0
    for i in range(length):
        if s[i].isdigit():
            if s[i] == "0":
                return False
            # check for letter after number
            for j in range(i + 1, length):
                if s[j].isalpha():
                    return False
            break;

            break
    #no failure conditions
    return True

if __name__ == "__main__":
    main()