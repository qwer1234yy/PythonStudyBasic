import unittest
import imageio
import matplotlib.pyplot as plt


class MyTestCase(unittest.TestCase):
    def test_something(self):
        pic = imageio.imread('pics\demo_1.jpg')
        fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))
        print(ax)


if __name__ == '__main__':
    unittest.main()
