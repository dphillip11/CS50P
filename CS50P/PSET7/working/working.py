import re


def main():
    number = convert(input("time: "))
    print(number)


def convert(input):

    input = input.replace("to", "")
    input = input.replace("M", "")

    # colon format
    if ":" in input:
        # # correct number format
        if numbers := re.match(
            r"([0-9][0-9]?):([0-5][0-9]) ([PA])  ([0-9][0-9]?):([0-5][0-9]) ([PA])",
            input,
        ):

            # add 12 for evening
            if (numbers[3] == "P" and int(numbers[1]) < 12) or (
                numbers[3] == "A" and numbers[1] == "12"
            ):
                from_hours = int(numbers[1]) + 12
            else:
                from_hours = int(numbers[1])

            from_minutes = int(numbers[2])

            # add 12 for evening
            if (numbers[6] == "P" and int(numbers[4]) < 12) or (
                numbers[6] == "A" and numbers[4] == "12"
            ):
                to_hours = int(numbers[4]) + 12
            else:
                to_hours = int(numbers[4])

            to_minutes = int(numbers[5])

            # check hours and minutes are reasonable
            if from_minutes > 60 or to_minutes > 60 or from_hours > 24 or to_hours > 24:
                raise ValueError
            from_minutes = from_minutes % 60
            to_minutes = to_minutes % 60
            from_hours = from_hours % 24
            to_hours = to_hours % 24

            return "{:02d}:{:02d} to {:02d}:{:02d}".format(
                from_hours, from_minutes, to_hours, to_minutes
            )

        # # incorrect number format
        else:

            raise ValueError

    # not colon format
    else:
        # # correct number format
        if numbers := re.match(r"([1]?[0-9]?) ([PA])  ([1]?[0-9]?) ([PA])", input):
            if (numbers[2] == "P" and int(numbers[1]) < 12) or (
                numbers[2] == "A" and numbers[1] == "12"
            ):
                from_hours = int(numbers[1]) + 12
            else:
                from_hours = int(numbers[1])
            if (numbers[4] == "P" and int(numbers[3]) < 12) or (
                numbers[4] == "A" and numbers[3] == "12"
            ):
                to_hours = int(numbers[3]) + 12
            else:
                to_hours = int(numbers[3])

            if from_hours > 24 or to_hours > 24:
                raise ValueError

            from_hours = from_hours % 24
            to_hours = to_hours % 24

            return f"{from_hours:02d}:00 to {to_hours:02d}:00"

        # # incorrect number format
        else:
            raise ValueError


if __name__ == "__main__":
    main()
