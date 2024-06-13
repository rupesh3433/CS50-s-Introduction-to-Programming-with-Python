
#pip install pyfiglet
from pyfiglet import Figlet
import sys
import random

def main():
    figlet = Figlet()
    figlet_lists = figlet.getFonts()
    if not (len(sys.argv) == 1 or len(sys.argv) == 3):
        sys.exit("Invalid usage")
    if len(sys.argv) == 3:
        if (sys.argv[2] not in figlet_lists) or (sys.argv[1] != "-f" and sys.argv[1] != "--font"):
            sys.exit("Invalid usage")
    s = input("Input: ")
    if len(sys.argv) == 1:
        call_figlet_with_random(s, figlet, figlet_lists)
    elif len(sys.argv) == 3:
        call_figlet_without_random(s, figlet)


def call_figlet_with_random(s, figlet, figlet_lists):
    f = random.choice(figlet_lists)
    figlet.setFont(font = f)
    print(figlet.renderText(s))

def call_figlet_without_random(s, figlet):
    font = sys.argv[2]
    figlet.setFont(font = font)
    print(figlet.renderText(s))


main()

