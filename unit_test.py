import unittest

class Mis_tests(unittest.TestCase):

    sumando_uno=0
    sumando_dos=0
    correr=True

    def setUp(self):
        self.sumando_uno=2
        self.sumando_dos=2
        if self.sumando_uno*self.sumando_dos==2000:
            self.correr=False

    def test_suma(self):
        self.assertEqual(self.sumando_uno+self.sumando_dos,4)
        self.assertTrue(self.correr)

    def test_resta(self):
        self.assertTrue(self.sumando_uno-self.sumando_dos==0)
        self.assertTrue(self.correr)

    def test_verificar_iguales(self):
        a=5
        b=4+1
        self.assertEqual(a,b)
    
    def test_verificar_no_iguales(self):
        a=10
        b=5*3
        self.assertNotEqual(a,b,"a should be different of b")

    def test_validar_si_verdadero(self):
        a=2
        self.assertTrue(a==2,"it will be a True")

    def test_validar_si_falso(self):
        a=3
        self.assertFalse(a!=3,"it will be a False")

    def test_es_nulo(self):
        a=None
        self.assertIsNone(a)

    def test_no_nulo(self):
        a=2
        self.assertIsNotNone(a)

    def test_es(self):
        a=5
        b=5
        self.assertIs(a,b,"the same tye of data was expected")
    
    def test_no_es(self):
        a=2
        b=2.00
        self.assertIsNot(a,b)

    def test_texto_en(self):
        a="hi"
        b="hi world"
        self.assertIn(a,b)

    def test_es_mayor(self):
        a=7
        b=3
        self.assertGreater(a,b,"a have to be greater than b")

    def tearDown(self):
        print("Save Case")

if __name__=='__main__':
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(Mis_tests)
    unittest.TextTestRunner(verbosity=2).run(suite)