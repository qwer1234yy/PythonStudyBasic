import unittest, numpy as np, imageio


class MyTestCase(unittest.TestCase):
    def test_zeros(self):
        pic = imageio.imread('../pic_analysis/pics/demo_1.jpg')
        np_zeros = np.zeros(pic.shape)
        print(np_zeros[0])


if __name__ == '__main__':
    unittest.main()
