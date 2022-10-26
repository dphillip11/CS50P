def main():
    time = input("What time is it? ")
    time = convert(time)
    if 7 <= time <= 8:
        print("breakfast time")
    if 12 <= time <= 13:
        print("lunch time")
    if 18 <= time <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    try:
        minutes = float(minutes) / 60.0
    except:
        minutes, suffix = minutes.split(" ")
        minutes = float(minutes) / 60.0
        if suffix == "p.m.":
            hours = hours + 12
    return hours + minutes


if __name__ == "__main__":
    main()