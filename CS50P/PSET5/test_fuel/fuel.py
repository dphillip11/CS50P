def main():
    fraction = input("fraction of fuel:")
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction):
    x, y = fraction.split(sep="/")
    try:
        x = int(x)
        y = int(y)
        if x > y:
            raise ValueError
    except:
        raise ValueError
    if y == 0:
        raise ZeroDivisionError
    return round(100 * x / y)


def gauge(percentage):
    if not (percentage) < 99:
        return "F"
    elif not (percentage) > 1:
        return "E"
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()
