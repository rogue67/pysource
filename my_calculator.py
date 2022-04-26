import io
import math
from tokenize import TokenError
from tokenizer import TokenizeWrapper


class CalculatorException(Exception):
    def __init__(self, arg):
        self.arg = arg


vardict = {}
listafeltoken = ['==','++','**']

def assignment(wtok):  
    result = expression(wtok)
    while wtok.get_current() == '=':
        wtok.next()  ## bypass =
        if ( not wtok.is_name() or is_function(wtok) ):
            raise CalculatorException(f"*** Error. Förväntades en variabel efter = hittade '{wtok.get_current()}' ")

        vardict[wtok.get_current()] = result
        wtok.next()  ## bypass name
    if wtok.get_current() in listafeltoken:
        raise CalculatorException(f"*** Error. Fel format på inmatningen '{wtok.get_current()}' ")
    return result


def expression(wtok):  
    result = term(wtok)
    while wtok.get_current() == '+' or wtok.get_current() == '-':
        wtok.next()  # bypass + or -
        if wtok.get_previous() == '+':
            if wtok.get_current()  == '+':
                raise CalculatorException("Felaktig inmatning:  ++")
            else:
                result = result + term(wtok)
        elif wtok.get_previous() == '-':
            result = result - term(wtok)
        else:
            break
    return result


def term(wtok):
    result = factor(wtok)
    while wtok.get_current() == '*' or wtok.get_current() == '/':
        wtok.next()  # bypass * or /
        if wtok.get_previous() == '*':
            result = result * factor(wtok)
        elif wtok.get_previous() == '/':
            try:
                result = result / factor(wtok)
            except ZeroDivisionError as e:
                print(e)
          ##else:
                ##break
    return result


def factor(wtok):
    if wtok.get_current() == '(':
        wtok.next()  # bypass (
        result = assignment(wtok)
        wtok.next()  # bypass )
    elif is_function(wtok):
        wtok.next()  ## bypass funktions namn
        if wtok.get_current() != '(':
            raise CalculatorException(f"Felaktig inmatning: :  '{wtok.get_previous()}'")
        if wtok.get_previous() == 'sin':
            wtok.next()
            result = math.sin(assignment(wtok))
            wtok.next()
        elif wtok.get_previous() == 'cos':
            wtok.next()
            result = math.cos(assignment(wtok))
            wtok.next()
        elif wtok.get_previous() == 'exp':
            wtok.next()
            result = math.exp(assignment(wtok))
            wtok.next()
        else:
            wtok.next()
            tal = assignment(wtok)
            if tal < 0:
                raise CalculatorException("logaritmen av ett negativt tal")
            else:
                result = math.log(tal)
            wtok.next()
    elif wtok.is_number():  ## should be a number
        result = float(wtok.get_current())
        wtok.next()  ## bypass the number
    elif wtok.get_current() == '-':
        wtok.next()  ##  bypass -
        result = -factor(wtok)
    elif wtok.is_name():
        if wtok.get_current() in vardict:
            result = vardict[wtok.get_current()]
        else:
            raise CalculatorException(f"odefinierad variabel:  '{wtok.get_current()}'")
    else:
        raise CalculatorException(
            f"Expected a left parentheses or number but found '{wtok.get_current()}'")
    return result


def statement(wtok):  
    if wtok.get_current() == 'quit':
        print('Bye!')
        exit()
    elif wtok.get_current() == 'vars':
        for key, value in vardict.items():
            print(key, ':' , value)
    elif  wtok.is_at_end():
        return None
    else:
        val = assignment(wtok)
        if wtok.get_current() == ')':
            raise CalculatorException(f"*** Error.  Fel inmatning '{wtok.get_current()}'")
        return val



def is_function(wtok):
    fun = ['sin', 'cos', 'exp', 'log']
    if wtok.get_current() in fun:
        return True


def main():
    print("Very simple calculator")
    while True:
        line = input('HAL 9000 :')
        try:
            wtok = TokenizeWrapper(line)
            result = statement(wtok)
            if result is not None:
                vardict['ans']= result
                print('Result: ', result)
        except TokenError:
            print('*** Error. Unbalanced parentheses')
        except CalculatorException as e:
            print(e)


if __name__ == "__main__":
    main()
