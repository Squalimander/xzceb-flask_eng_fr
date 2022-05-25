
from translator import englishToFrench
from translator import frenchToEnglish
import unittest

class TestStringMethods(unittest.TestCase):
    def test_e2f(self):
        self.assertEqual(englishToFrench('hello'), 'Bonjour')
        self.assertEqual(englishToFrench('Hello, how are you?'),'Bonjour, comment es-tu?')
        self.assertIsNone(englishToFrench(None))

    def test_f2e(self):
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')
        self.assertEqual(frenchToEnglish('Bonjour, comment es-tu?'), 'Hello, how are you?')
        self.assertIsNone(englishToFrench(None))

    


#assertNotEqual()

if __name__ == '__main__':
    unittest.main()