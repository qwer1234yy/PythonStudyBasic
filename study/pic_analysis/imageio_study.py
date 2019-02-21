import unittest
import imageio
import matplotlib.pyplot as plt


class MyTestCase(unittest.TestCase):
    def test_something(self):
        im_screen = imageio.imread('<screen>')
        # im_clipboard = imageio.imread('<clipboard>')
        print()
        plt.imshow(im_screen[:, :, 2])
        plt.show()


if __name__ == '__main__':
    unittest.main()
