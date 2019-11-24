import unittest
import xmlrunner
from Operaciones import Operaciones


class calculadoraTest(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(Operaciones.suma(1,2),3)

    def test_resta(self):
        self.assertEqual(Operaciones.resta(2,1),1)
        
    def test_dividir(self):
        self.assertEqual(Operaciones.dividir(4,2),2)

    def test_multiplicar(self):
        self.assertEqual(Operaciones.multiplicar(1,1),1)



if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="resultado"))
