import unittest, keyboard, time


class MyTestCase(unittest.TestCase):
    def test_something(self):
        time.sleep(5)
        keyboard.press_and_release('enter')


if __name__ == '__main__':
    unittest.main()
