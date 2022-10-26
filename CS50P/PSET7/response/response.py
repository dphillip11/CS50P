from validator_collection import validators


def main():
    print(validate(input("email: ")))


def validate(input):
    try:
        email_address = validators.email(input, allow_empty=False)
        if email_address:
            return "Valid"
    except:
        return "Invalid"


if __name__ == "__main__":
    main()
