import random


def main():

    level = get_level()
    score = 0

    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        correct = x + y

        tries = 3

        while tries > 0:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == correct:
                    score += 1
                    break
                else:
                    print("EEE")
                    tries -= 1
            except:
                print("EEE")
                tries -= 1
        if tries == 0:
            print(correct)

    print(f"Score: {score}")


def get_level():

    # dummy level
    level = -1

    while not 0 < level < 4:
        try:
            level = int(input("Level: "))
        except:
            pass
    return level


def generate_integer(level):

    if level < 1 or level > 3:
        raise ValueError
    # produce a random number with level digits
    if level == 1:
        random_number = round(random.randrange(10))
    else:
        random_number = round(random.randrange(10 ** (level - 1), 10 ** (level)))

    return random_number


if __name__ == "__main__":

    main()
