import unittest, random
import cookies


class MyTestCase(unittest.TestCase):
    def test_something(self):
        print(cookies.Cookies[random.randint(0, len(cookies.Cookies)-1)])


if __name__ == '__main__':
    unittest.main()
