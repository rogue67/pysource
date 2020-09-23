import io
import math
from tokenize import TokenError
from tokenizer import TokenizeWrapper


class CalculatorException(Exception):
    def __init__(self, arg):
        self.arg = arg

vardict = {}

def assignment(wtok):
    result = expression(wtok)
    while wtok.get_current() == '=':
        wtok.next()                     ## bypass =
        vardict[wtok.get_current()] = result      
        wtok.next()                     ## bypass name
    return result

def expression(wtok): ## KLAR      
    result = term(wtok)
    while  wtok.get_current() == '+' or wtok.get_current() == '-':
        wtok.next()                  # bypass + or -
        if wtok.get_previous()   == '+':
            result = result + term(wtok)
        elif wtok.get_previous()  == '-' :
            result = result - term(wtok)
        else:
            break
    return result

def term(wtok):     ## KLAR
    result = factor(wtok)
    while wtok.get_current() == '*' or wtok.get_current() == '/':
        wtok.next()                  # bypass * or /
        if wtok.get_previous()   == '*':
            result = result * factor(wtok)
        elif wtok.get_previous()   == '/':
            try:
                result = result / factor(wtok)
            except ZeroDivisionError as e:
                print(e)
            else:
                break
    return result

def factor(wtok):
    if wtok.get_current() == '(':
        wtok.next()                  # bypass (
        result = assignment(wtok)
        wtok.next()        # bypass )
    elif is_function( wtok ):
        wtok.next()
        if wtok.get_previous() == 'sin':
            result = math.sin( expression( wtok ) )
        elif wtok.get_previous() == 'cos':
            result = math.cos( expression( wtok ) )
        elif wtok.get_previous() == 'exp':
            result = math.exp( expression( wtok ) )
        else:
            try:
                result = math.log( expression( wtok ) )
            except ValueError as e:
                print( "Logaritmen av negativt tal " + e )    
    elif wtok.is_number():                          ## should be a number
        result = float(wtok.get_current())
        wtok.next()                  ## bypass the number
    elif wtok.get_current() == '-':
        wtok.next()        ##  bypass -
        
        result = -factor( wtok )
    elif wtok.is_name() and not is_function(wtok):
        vardict[wtok.get_current()] = result
        wtok.nect()                 ## bypass name
    else:
        raise CalculatorException(
            f"Expected a left parentheses or number but found '{wtok.get_current()}'")
    return result


def statement(wtok):
    if wtok.get_current() == 'quit':
        print('Bye!')
        exit()
    else:
        return assignment(wtok)

def is_function(wtok):
    fun = ['sin','cos','exp','log']
    if wtok.get_current() in fun:
        return True
    
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
