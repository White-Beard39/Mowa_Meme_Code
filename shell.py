import time
from lexer import Lexer


def run():
    print("mowa meme code")
    while True:
        command = input(">>>>")
        if command == "mowa_inka_chalu":
            slowprint("Poora Na Kodaka (`_`)")
            exit()
        obj = Lexer(command)


def slowprint(text: str) -> None:

    for letter in text.split(" "):
        print(letter)
        time.sleep(0.3)


run()
