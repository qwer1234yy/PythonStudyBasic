import unittest
from PIL import Image


class MyTestCase(unittest.TestCase):
    def test_something(self):
        image = Image.open('pics/Cases Processed on Import.png   ')
        

if __name__ == '__main__':
    unittest.main()
