import re


def main():
    print(parse(input("HTML: ")))


def parse(s):

    if links := re.findall(r'src="([\w/.:]+)"', s):
        if "youtube.com/embed/" in links[0]:
            link = (
                "https://youtu.be/"
                + links[0].rsplit("/")[len(links[0].rsplit("/")) - 1]
            )
            return link
        else:
            return


if __name__ == "__main__":
    main()
