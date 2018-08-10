import unittest
from lab03_ben import *

class labTests(unittest.TestCase):
	
	## fill in a few tests for each
	## make sure to account for correct and incorrect input

    def test_shout(self):
    	self.assertEqual("HELLO", shout("hello"))
    	self.assertNotEqual("Harambe", shout("hello"))
        self.assertEqual("This isnt a string", shout(365))

    def test_reverse(self):
    	self.assertEqual("olleh", reverse("hello"))
    	self.assertNotEqual("Harambe", reverse("hello"))	
        self.assertEqual("This isnt a string", reverse(2765))

    def test_reversewords(self):
    	self.assertEqual("ben hello", reversewords("hello ben"))
    	self.assertNotEqual("Harambe", reversewords("hello ben"))
        self.assertEqual("This isnt a string", reversewords(387458724))

    def test_reversewordletters(self):
    	self.assertEqual("olleh neb", reversewordletters("hello ben"))
    	self.assertNotEqual("Harambe", reversewordletters("hello ben"))
        self.assertEqual("This isnt a string", reversewordletters(37465))

    def test_piglatin(self):
    	self.assertEqual("ellohay enbay", piglatin("hello ben"))
    	self.assertNotEqual("Harambe", piglatin("hello ben"))
        self.assertEqual("This isnt a string", piglatin(87487))

if __name__ == '__main__':
  unittest.main()