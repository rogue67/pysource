import unittest, my_calculator, io, math
from tokenize import TokenError
from tokenizer import TokenizeWrapper

class CalculatorTestCase(unittest.TestCase):

    def test_assignment_pythagoras(self):
        line = "sin(2)*sin(2) + cos(2)*cos(2)"
        wtok = TokenizeWrapper( line )
        result = my_calculator.assignment( wtok )
        self.assertEqual(result , 1.0 )

    def test_assignment_visa_variabel(self):
        line = "3 = a"
        line1 = "a"
        wtok = TokenizeWrapper( line )
        result = my_calculator.assignment( wtok )
        wtok1 = TokenizeWrapper(line1)
        self.assertEqual( my_calculator.assignment(wtok1) , 3 )

    def test_assignment_z(self):
        line = "1 + 2 + 3 = z"
        wtok = TokenizeWrapper( line )
        result = my_calculator.assignment( wtok )
        self.assertEqual( my_calculator.vardict.get('z') , 6 )

    def test_assignment_inget_lika_med(self):
        line = "1 - (5 - 2*2)/(1+1) - (-2 + 1)"
        wtok = TokenizeWrapper( line )
        result = my_calculator.assignment( wtok )
        self.assertEqual(result , 1.5 )        

    def test_assignment_parantes(self):
        line = "(3 = z)"
        wtok = TokenizeWrapper( line )
        result = my_calculator.assignment( wtok )
        self.assertEqual( my_calculator.vardict.get('z') , 3 )
        
    def test_assignment_two_equal_vars(self):
        line = "(2=x=y)"
        wtok = TokenizeWrapper( line )
        result = my_calculator.assignment( wtok )
        self.assertEqual(my_calculator.vardict.get('x') , 2 )
        self.assertEqual(my_calculator.vardict.get('y') , 2 )
        
    def test_assignment_full(self):
        line = "(2=x) + (3=y=z) = a"
        wtok = TokenizeWrapper( line )
        result = my_calculator.assignment( wtok )
        self.assertEqual(my_calculator.vardict.get('x') , 2 )
        self.assertEqual(my_calculator.vardict.get('y') , 3 )
        self.assertEqual(my_calculator.vardict.get('z') , 3 )
        self.assertEqual(my_calculator.vardict.get('a') , 5 )

    def test_expression_sju(self):
        line = "7"
        wtok = TokenizeWrapper( line )
        result = my_calculator.expression( wtok )
        self.assertEqual( result , 7 )
        
    def test_expression_plus(self):
        line = "2 + 3 + 4"
        wtok = TokenizeWrapper( line )
        result = my_calculator.expression( wtok )
        self.assertEqual( result , 9 )

    def test_expression_minus(self):
        line = "2-3"
        wtok = TokenizeWrapper( line )
        result = my_calculator.expression( wtok )
        self.assertEqual( result , -1 )

    def test_term_sju(self):
        line = "7"
        wtok = TokenizeWrapper( line )
        result = my_calculator.term( wtok )
        self.assertEqual( result , 7 )
        
    def test_term_mul(self) :
        line = "2 * 3"
        wtok = TokenizeWrapper( line )
        result = my_calculator.term( wtok )
        self.assertEqual( result , 6 )

    def test_term_sinus(self) :
        line = "sin(2)*sin(2)"
        wtok = TokenizeWrapper( line )
        result = my_calculator.term( wtok )
        self.assertEqual( result , math.sin(2)*math.sin(2) )

    def test_term_div(self) :
        line = "2 / 2"
        wtok = TokenizeWrapper( line )
        result = my_calculator.term( wtok )
        self.assertEqual( result , 1 )
        

    def test_function_true(self):
        line = 'sin';
        wtok = TokenizeWrapper( line )
        self.assertTrue( my_calculator.is_function( wtok ),msg=None )

    def test_function_false(self):
        line = 'roger';
        wtok = TokenizeWrapper( line )
        self.assertFalse( my_calculator.is_function( wtok ),msg=None )

    def test_factor_funktion_utan_parantes(self):
        line = "sin 4"
        wtok = TokenizeWrapper( line )
        self.assertRaises( my_calculator.CalculatorException , my_calculator.factor, wtok )

    def test_factor_sin(self):
        line = 'sin( 10 )'
        wtok = TokenizeWrapper( line )
        result = my_calculator.factor( wtok )
        self.assertEqual( result , math.sin( 10 ) )
        
    def test_factor_cos(self):
        line = "cos(3.141592653589793)"
        wtok = TokenizeWrapper( line )
        result = my_calculator.factor( wtok )
        self.assertEqual( result , math.cos(math.pi))

    def test_factor_log_negativ_input(self):
        line = "log( -1 )"
        wtok = TokenizeWrapper( line )
        self.assertRaises( my_calculator.CalculatorException , my_calculator.factor, wtok )

    def test_factor_log(self):
        line = "log( 2.718281828459045 )"
        wtok = TokenizeWrapper( line )
        result = my_calculator.factor( wtok )
        self.assertEqual( result , 1.0)

    def test_factor_exp(self):
        line = 'exp( 0 )'
        wtok = TokenizeWrapper( line )
        result = my_calculator.factor( wtok )
        self.assertEqual( result , 1.0)

    def test_factor_minus(self):
        line = "-(2+2)"
        wtok = TokenizeWrapper( line )
        result = my_calculator.factor( wtok )
        self.assertEqual( result , -4.0)        

    def test_statement_quit(self):
        line = "quit"
        wtok = TokenizeWrapper( line )
        self.assertRaises(SystemExit, my_calculator.statement, wtok)

if __name__ == '__main__':
    unittest.main()
