import unittest, min_rekursion
class RecursionTestCase(unittest.TestCase):
    def test_j_icke_i_text(self):                               ##ÖVN 1
        s = "roger"
        resultat = min_rekursion.j_finds_iter(s)
        self.assertFalse(resultat,'Finna tecken nisslyckades')

    def test_j_i_text(self):
        s = "joyride"
        resultat = min_rekursion.j_finds_iter(s)
        self.assertTrue(resultat,'Finna tecken nisslyckades')

    def test_j_find_tom_text(self):                             ##ÖVN 2
        s = ""
        resultat = min_rekursion.j_finds(s)
        self.assertFalse(resultat,'Logiskt fel ska vara False')

    def test_j_find_icke_tom_text(self):
        s = "heja"
        resultat = min_rekursion.j_finds(s)
        self.assertTrue(resultat,'Logiskt fel ska vara True')

    def test_j_find_icke_tom_text_utan_j(self):
        s = "ufo"
        resultat = min_rekursion.j_finds(s)
        self.assertFalse(resultat,'Logiskt fel ska vara False')

    def test_j_find_icke_tom_text_j_index_first(self):
        s = "jag"
        resultat = min_rekursion.j_finds(s)
        self.assertTrue(resultat,'Logiskt fel ska vara True')

    def test_j_find_icke_tom_text_j_index_last(self):
        s = "maj"
        resultat = min_rekursion.j_finds(s)
        self.assertTrue(resultat,'Logiskt fel ska vara True')

    def test_finds_tom_text(self):                              ##ÖVN 3
        txt = ""
        teck = "q"
        resultat = min_rekursion.finds(teck,txt)
        self.assertFalse(resultat,'Logiskt fel ska vara False')

    def test_finds_text_med_tecken(self):
        txt = "roger"
        teck = "o"
        resultat = min_rekursion.finds(teck,txt)
        self.assertTrue(resultat,'Logiskt fel ska vara True')

    def test_finds_text_utan_tecken(self):
        txt = "roger"
        teck = "k"
        resultat = min_rekursion.finds(teck,txt)
        self.assertFalse(resultat,'Logiskt fel ska vara False')

    def test_findsNr_text_utan_tecken(self):                ##ÖVN 4
        txt = "roger"
        teck = "k"
        resultat = min_rekursion.findsNr(teck,txt)
        self.assertEqual(resultat,0)

    def test_findsNr_text_med_tecken(self):
        txt = "roger"
        teck = "o"
        resultat = min_rekursion.findsNr(teck,txt)
        self.assertEqual(resultat,1)

    def test_findsNr_text_med_2_tecken(self):
        txt = "jogging"
        teck = "g"
        resultat = min_rekursion.findsNr(teck,txt)
        self.assertEqual(resultat,3)

    def test_power_n_noll_x_skilld_fr_noll(self):           ##Övn 5
        x = 4
        n = 0
        resultat = min_rekursion.power(x,n)
        self.assertEqual(resultat, 1)

    def test_power_n_och_x_skilld_fr_noll(self):
        x = 4
        n = 3
        resultat = min_rekursion.power(x,n)
        self.assertEqual(resultat, 64)

    def test_power_n_skilld_fr_noll_x_noll(self):
        x = 0
        n = 3
        resultat = min_rekursion.power(x,n)
        self.assertEqual(resultat, 0)
        
    def test_multiply_m_eller_n_noll(self):             ##ÖVN 6
        m = 0
        n = 3
        resultat = min_rekursion.multiply(m,n)
        self.assertEqual(resultat, 0)
    
    def test_multiply_m_eller_n_noll_2(self):
        m = 3
        n = 0
        resultat = min_rekursion.multiply(m,n)
        self.assertEqual(resultat, 0)

    def test_myltiply_m_n_skild_fr_noll(self):
        m = 3
        n = 7
        resultat = min_rekursion.multiply(m,n)
        self.assertEqual(resultat, 21)

    def test_harmonic_n_lika_med_ett(self):         ##ÖVN 8
        n = 1
        resultat = min_rekursion.harmonic(n)
        self.assertEqual(resultat,1)

    def test_harmonic(self):
        n = 4
        resultat = min_rekursion.harmonic(n)
        self.assertAlmostEqual(resultat,25/12)

    def test_largest(self):                         ##ÖVN 9
        a = [16,2,7]
        resultat = min_rekursion.largest(a)
        self.assertEqual(resultat,16)

    def test_reverse(self):                         ##ÖVN 10
        s = "abc"
        ans = "cba"
        resultat = min_rekursion.reverse(s)
        self.assertEqual(resultat,ans)

    def test_reverse_ett_tecken(self):              ##ÖVN 10
        s = "q"
        ans = "q"
        resultat = min_rekursion.reverse(s)
        self.assertEqual(resultat,ans)

    def test_paren_match_left_false(self):                  ##ÖVN 14
        txt = "((())"
        match = min_rekursion.paren_match(txt)
        self.assertEqual(match,False)

    def test_paren_match_empty(self):
        txt = ""
        match = min_rekursion.paren_match(txt)
        self.assertEqual(match,True)

    def test_paren_match_true(self):
        txt = "()"
        match = min_rekursion.paren_match(txt)
        self.assertEqual(match,True)

    def test_paren_match_right_false(self):
        txt = ")"
        match = min_rekursion.paren_match(txt)
        self.assertEqual(match,False)
        
if __name__ == '__main__':
    unittest.main()
