import sys
from pyfiglet import Figlet
import random

figlet = Figlet()

l = len(sys.argv)
fonts = figlet.getFonts()

if l == 3:
    if not sys.argv[1] in ["-f", "--font"]:
        sys.exit("args should be -f and name of font")
    elif not sys.argv[2] in fonts:
        sys.exit("font not in list")
    else:
        figlet.setFont(font = sys.argv[2])

elif l != 1:
    sys.exit("args should be -f and name of font")

else:
    random.seed()
    r = random.randrange(len(fonts))
    figlet.setFont(font = fonts[r])


text = input("text here: ")

print(figlet.renderText(text))

