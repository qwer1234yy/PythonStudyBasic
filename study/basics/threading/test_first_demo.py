import unittest, threading


class MyTestCase(unittest.TestCase):
    def test_threading(self):
        print(threading.current_thread().name)


if __name__ == '__main__':
    unittest.main()
