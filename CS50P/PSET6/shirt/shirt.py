import sys
from PIL import Image,ImageOps as ops


def main():

    if len(sys.argv) != 3:
        sys.exit("Incorrect usage")

    if not check_extensions(sys.argv[1]):
        sys.exit("bad input extension")

    if not check_extensions(sys.argv[2]):
        sys.exit("bad output extension")

    if not check_extensions(sys.argv[1]) == check_extensions(sys.argv[2]):
        sys.exit("extensions don't match")

    try:
        im = Image.open(sys.argv[1])
    except:
        sys.exit("bad input, doesn't exist")

    shirt = Image.open('shirt.png')
    im = ops.fit(im, shirt.size, bleed=0.0, centering=(0.5, 0.5))

    im.paste(shirt, mask=shirt)

    im.save(sys.argv[2])



def check_extensions(input):

    exts = [".jpg", ".jpeg", ".png"]

    for ext in exts:
        if input.endswith(ext):
            return ext
    return False


if __name__ == "__main__":
    main()
