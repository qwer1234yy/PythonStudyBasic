import pytest

class cal():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
    def sub(self):
        return self.a-self.b

class Test_pytest(object):

    def test_assert(self):
        x = 5
        y = 6
        assert x + 1 == y, "test passed: 5+1=6"
        assert x == y, "test failed: 5 <> 6"


if __name__ == '__main__':
    pytest.main()
    print('------------')
