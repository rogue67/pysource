import my_calculator, io, math
from tokenize import TokenError
from tokenizer import TokenizeWrapper
vars = {}
arg = math.pi
line = "sin(2)*4"
wtok = TokenizeWrapper( line )
result = my_calculator.term( wtok )
print(vars)
print(result)
