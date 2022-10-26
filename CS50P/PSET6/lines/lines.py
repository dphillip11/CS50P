import sys

def main():
    if len(sys.argv)< 2:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    try:
        file = open(sys.argv[1], "r")
    except FileNotFoundError:
        sys.exit("File does not exist")

    line_count = 0

    for line in file:
        if not line.lstrip().startswith("#") and len(line.strip()) != 0:
            line_count += 1

    file.close()
    
    print(line_count)

if __name__ == '__main__':
    main()