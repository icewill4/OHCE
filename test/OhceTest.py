from Ohce import Ohce
import unittest


class OhceTestMot(unittest.TestCase):
    def test_renvoi_miroir(self):
        ohce = Ohce()
        resultat = ohce.palindrome("mot")


if __name__ == '__main__':
    unittest.main()
