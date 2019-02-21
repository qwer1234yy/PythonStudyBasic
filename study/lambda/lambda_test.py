import unittest, numpy as np


class MyTestCase(unittest.TestCase):
    def test_something(self):
        x = lambda a: a + 10
        gray = lambda rgb: np.dot(rgb[..., :3], [0.299, 0.587, 0.114])
        print(gray)


if __name__ == '__main__':
    unittest.main()
