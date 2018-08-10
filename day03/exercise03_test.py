import unittest
<<<<<<< HEAD
from exercise03_ben import *
=======
from exercise03_erin import *
>>>>>>> upstream/master

class exerciseTests(unittest.TestCase):
    
    def test_vowels(self):
        self.assertEqual(4, count_vowels("mississippi"))quit
        with self.assertRaises(TypeError): count_vowels(5)
        with self.assertRaises(TypeError): count_vowels([1,2,3])

if __name__ == '__main__':
  unittest.main()