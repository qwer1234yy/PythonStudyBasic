import pytest
class calculator(object):

    def add(self, a, b):
        return a+b

    def diff(self, a, b):
        return a+b

    def multible(self, a, b):
        return a+b

    def add(self, a, b):
        return a+b

class Test_pytest(object):

    cal = calculator()

    def setup_module(module):
        print("\n--------------------setup_module--------------------")

    @pytest.fixture()
    def sum(self):
        print('--------------------------smtp---------------:')
        return 1 + 2

    @pytest.mark.slow
    def test_t1(self,sum):
        result = self.cal.add(a=1, b=2)
        assert 8 == result
        print(result)
        print(sum)
        print(type(sum))
        print('test_t1-')

    def test_t2(self):
        print('test_t2-')

    def test_t3(self):
        print('test_t3-')

    def test_t4(self):
        print('test_t4-')

    def test_t5(self):
        print('test_t5-')