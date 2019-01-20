import unittest

class a(object):

    def say2(self):
        print('a')
    def say(self):
        print('a')


class b(object):

    def say1(self):
        print('b')
    def say(self):
        print('b')


class c(a,b):
    def __init__(self):
        pass
    def sayc(self):
        print('c')


class testcase(unittest.TestCase):

    def test_extends(self):
        a1 = a()
        c1 = c()
        c1.sayc()
        c1.say()


