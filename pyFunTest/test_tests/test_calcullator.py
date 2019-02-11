from pyFunTest.business.calculator import Calculator


class TestCalculator(object):
    caculator = Calculator(a=1332, b=342)
    a = 1332
    b = 342

    # def __init__(self):
    #     self.caculator = Calculator(a=1332, b=342)
    #     self.a = 1332
    #     self.b = 342

    def test_add(self):
        actual_result = self.caculator.add()
        expected_result = self.a + self.b
        assert actual_result == expected_result

    def test_subtract(self):
        actual_result = self.caculator.subtract()
        # expected_result = self.a - self.b
        expected_result = 1111
        assert actual_result == expected_result

    def test_divide(self):
        actual_result = self.caculator.multible()
        expected_result = self.a / self.b
        assert actual_result == expected_result

    def test_multible(self):
        actual_result = self.caculator.divide()
        expected_result = self.a * self.b
        assert actual_result == expected_result
