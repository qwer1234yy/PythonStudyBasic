import unittest, random
import imageio, numpy as np
from imageio.core.util import Image
import matplotlib.pyplot as plt


class MyTestCase(unittest.TestCase):
    def test_something(self):
        pic = imageio.imread('pics/demo_1.jpg')
        # plt.figure(figsize=(5,5))
        # plt.imshow(pic)
        # plt.show()

        print(pic[100, 50, 0])
        # pic[:, :, 0] = 255
        # create zero matrix

        split_img = np.zeros(pic.shape, dtype="uint8")  # 'dtype' by default: 'numpy.float64'
        split_img[:, :, 1] = pic[:, :, 1]

        plt.imshow(split_img)
        plt.show()
    def test_Process_Pixel(self):
        pic = imageio.imread('pics/test01.jpg')

        low_pixel = pic < 20
        print(pic.shape)
        if low_pixel.any() == True:
            print(low_pixel.shape)
        pic[low_pixel] = random.randint(100, 110)

        plt.imshow(pic)
        plt.show()
    def test_masking_pic(self):
        pic = imageio.imread('pics/test01.jpg')
        # seperate the row and column values
        total_row, total_col, layers = pic.shape
        x, y = np.ogrid[:total_row, :total_col]
        # print(x)
        # print(y)
        # get the center values of the image
        cen_x, cen_y = total_row / 2, total_col / 2
        distance_from_the_center = np.sqrt((x - cen_x) ** 2 + (y - cen_y) ** 2)
        # Select convenient radius value
        radius = (total_row / 2 - 50)
        circular_pic = distance_from_the_center > radius
        pic[circular_pic] = 100
        plt.figure(figsize=(10, 10))
        plt.imshow(pic)
        plt.show()


if __name__ == '__main__':
    unittest.main()
