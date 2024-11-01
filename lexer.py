from icecream import ic


class Lexer:

    operators = {"+": "", "-": "", "*": "", "/": "", "=": ""}

    special_chars = {
        ":": "",
        ";": "",
        "_": "",
        "`": "",
        "!": "",
        "@": "",
        "$": "",
        "(": "",
        ")": "",
    }

    alphabets = {
        "a": "",
        "b": "",
        "c": "",
        "d": "",
        "e": "",
        "f": "",
        "g": "",
        "h": "",
        "i": "",
        "j": "",
        "k": "",
        "l": "",
        "m": "",
        "n": "",
        "o": "",
        "p": "",
        "q": "",
        "r": "",
        "s": "",
        "t": "",
        "u": "",
        "v": "",
        "w": "",
        "x": "",
        "y": "",
        "z": "",
        "A": "",
        "B": "",
        "C": "",
        "D": "",
        "E": "",
        "F": "",
        "G": "",
        "H": "",
        "I": "",
        "J": "",
        "K": "",
        "L": "",
        "M": "",
        "N": "",
        "O": "",
        "P": "",
        "Q": "",
        "R": "",
        "S": "",
        "T": "",
        "U": "",
        "V": "",
        "W": "",
        "X": "",
        "Y": "",
        "Z": "",
    }

    numbers = {
        "0": "",
        "1": "",
        "2": "",
        "3": "",
        "4": "",
        "5": "",
        "6": "",
        "7": "",
        "8": "",
        "9": "",
    }

    def __init__(self, expresssion):
        self.expression = expresssion
        # calling the tokenize function to tokenize
        self.tokenize(self.expression)

    def tokenize(self, expression):
        # initilizing an empty list to return the tokens
        l = []

        expression_len = len(expression)
        idx = 0
        while idx < expression_len - 1:
            sample_str = ""
            ic(idx, expression_len, l)
            try:
                # checking for the expression if it belongs to operators
                if expression[idx] in self.operators:
                    while expression[idx + 1] in self.operators:
                        sample_str += expression[idx]
                        idx += 1
                    sample_str += expression[idx]
                    l.append(sample_str)
                    sample_str = ""
                # checking for the expression if it belongs to alphabets
                elif expression[idx] in self.alphabets:
                    while expression[idx + 1] in self.alphabets:
                        sample_str += expression[idx]
                        idx += 1
                    sample_str += expression[idx]
                    l.append(sample_str)
                    sample_str = ""
                # checking for the expression if it belongs to numbers
                elif expression[idx] in self.numbers:
                    while expression[idx + 1] in self.numbers:
                        sample_str += expression[idx]
                        idx += 1
                    sample_str += expression[idx]
                    l.append(sample_str)
                    sample_str = ""
                # checking for the expression if it belongs to special_chars
                elif expression[idx] in self.special_chars:
                    while expression[idx + 1] in self.special_chars:
                        sample_str += expression[idx]
                        idx += 1
                    sample_str += expression[idx]
                    l.append(sample_str)
                    sample_str = ""

            except Exception as e:
                print("An exception occurred:")
                print(f"Type: {type(e)}")
                print(f"Name: {e.__class__.__name__}")
                print(f"Message: {str(e)}")
                print(f"Args: {e.args}")
                l.append(sample_str)
            idx += 1

        ic(l)
