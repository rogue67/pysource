import io
import math
from tokenize import TokenError
from tokenizer import TokenizeWrapper


class CalculatorException(Exception):
    def __init__(self, arg):
        self.arg = arg


def expression(wtok):
    result = term(wtok)
    while wtok.get_current() == '+':
        wtok.next()                  # bypass +
        result = result + term(wtok)
    return result


def term(wtok):
    result = factor(wtok)
    while wtok.get_current() == '*':
        wtok.next()                  # bypass *
        result = result * factor(wtok)
    return result


def factor(wtok):
    if wtok.get_current() == '(':
        wtok.next()                  # bypass (
        result = expression(wtok)
        wtok.next()                  # bypass )
    elif wtok.is_number():                          # should be a number
        result = float(wtok.get_current())
        wtok.next()                  # bypass the number
    else:
        raise CalculatorException(
            f"Expected a left parentheses or number but found '{wtok.get_current()}'")
    return result


def statement(wtok):
    if wtok.get_current() == 'quit':
        print('Bye!')
        exit()
    else:
        return expression(wtok)


def main():
    print("Very simple calculator")
    while True:
        line = input('HAL 9000 :')
        try:
            wtok = TokenizeWrapper(line)
            result = statement(wtok)
            print('Result: ', result)
        except TokenError:
            print('*** Error. Unbalanced parentheses')
        except CalculatorException as e:
            print(e)


if __name__ == "__main__":
    main()
