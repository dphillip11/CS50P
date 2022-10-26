import csv
import sys
import os


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    try:
        input = open(sys.argv[1], "r")
        output = open("temp.csv", "w")
    except:
        sys.exit("Could not read invalid_file.csv")

    reader = csv.DictReader(input)
    writer = csv.DictWriter(
        output, fieldnames=["first", "last", "house"], skipinitialspace=True
    )
    writer.writeheader()

    for line in reader:

        house = line["house"]
        last, first = line["name"].split(",")
        writer.writerow({"first": first, "last": last, "house": house})

    input.close()
    output.close()

    with open("temp.csv", "r") as input:
        with open(sys.argv[2], "w") as output:
            for line in input:
                output.write(line.lstrip())

    os.remove("temp.csv")


if __name__ == "__main__":
    main()
