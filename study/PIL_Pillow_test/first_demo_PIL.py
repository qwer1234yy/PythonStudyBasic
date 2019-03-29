import unittest, PIL
from PIL import ImageGrab


class MyTestCase(unittest.TestCase):
    def test_grab_full_screenshot(self):
        im = ImageGrab.grab()
        im.show()
        im.save(fp='full_screenshot01.png')
        

if __name__ == '__main__':
    unittest.main()
