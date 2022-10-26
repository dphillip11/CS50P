import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if numbers := re.fullmatch(
        r"([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})", ip
    ):
        for n in range(1, 4):
            if int(numbers[n]) > 255:
                return False
        return True
    else:
        return False


...


if __name__ == "__main__":
    main()
