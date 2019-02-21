import unittest
import imageio
import matplotlib.pyplot as plt


class MyTestCase(unittest.TestCase):
    def test_something(self):
        pic = imageio.imread('pics\demo_1.jpg')
        # plt.figure(figsize=(20, 15))
        # plt.imshow(pic)
        # plt.show()
        # print('Type of the image : ', type(pic))
        # print('Shape of the image : {}'.format(pic.shape))
        # print('Image Hight {}'.format(pic.shape[0]))
        # print('Image Width {}'.format(pic.shape[1]))
        # print('Dimension of Image {}'.format(pic.ndim))
        # print('Image size {}'.format(pic.size))
        # print('Maximum RGB value in this image {}'.format(pic.max()))
        # print('Minimum RGB value in this image {}'.format(pic.min()))
        # plt.title('R channel')
        # plt.ylabel('Height {}'.format(pic.shape[0]))
        # plt.xlabel('Width {}'.format(pic.shape[1]))
        # plt.imshow(pic[:, :, 0])
        # plt.show()
        # print(pic[100, 50])
        # print(pic[100, 50, 0])
        # print(pic[100, 50, 1])
        # print(pic[100, 50, 2])
        #
        # plt.title('G channel')
        # plt.ylabel('Height {}'.format(pic.shape[0]))
        # plt.xlabel('Width {}'.format(pic.shape[1]))
        # plt.imshow(pic[:, :, 1])
        # plt.show()

        pic[:, :, 1] = 255  # full intensity to those pixel's R channel
        plt.figure(figsize=(10, 10))
        plt.imshow(pic)
        plt.show()


if __name__ == '__main__':
    unittest.main()
