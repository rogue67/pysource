import my_calculator, io, math
from tokenize import TokenError
from tokenizer import TokenizeWrapper
vars = {}
arg = math.pi
line = "sin(3.141592653589793/4)*sin(3.141592653589793/4)"
wtok = TokenizeWrapper( line )
result = my_calculator.assignment( wtok )
print(vars)
print(result)
