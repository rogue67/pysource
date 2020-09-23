import unittest, my_calculator, io, math
from tokenize import TokenError
from tokenizer import TokenizeWrapper

class CalculatorTestCase(unittest.TestCase):

    def test_korrekt_expression(self):
        while True:
            line = "1 + 1 + 1"
            try:
                wtok = TokenizeWrapper(line)
                result = my_calculator.expression(wtok)
                self.assertEqual( result , 3)
            except TokenError:
                print('*** Error. Unbalanced parentheses')
            except CalculatorException as e:
                print(e)

if __name__ == '__main__':
    unittest.main()
