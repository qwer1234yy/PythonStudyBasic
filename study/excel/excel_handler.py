import unittest,xlrd,xlwt,os


class MyTestCase(unittest.TestCase):

    def test_os(self):
        f_name = 'result.html'
        f_path = os.path.dirname(__file__)
        # file = open(f_path+f_name)
        print(os.curdir)
        print(os.getcwd())
        print(os.path.dirname(__file__))
        print(os.path.abspath(f_name))
        print(os.path.realpath(__file__))


    def test_something(self):
        f = r'C:\Users\yyang212\PycharmProjects\PythonStudy\SMART\Smart_resources\fields.xlsx'
        book = xlrd.open_workbook(f)  # 打开一个excel
        print(book)
        sheet_ipfield = book.sheet_by_name('ipfield')

        {'Admit Source - UB'}
        field_name = 'Admit Source - UB'
        operator = 'In'
        valueType = ''
        value1 = ''
        value2 = ''
        nrows = sheet_ipfield.nrows
        ncols = sheet_ipfield.ncols
        for i in range(1,nrows):
            if field_name in sheet_ipfield.cell(i, 0).value:
                    if operator in sheet_ipfield.cell(i, 1).value:
                        operator=sheet_ipfield.cell(i, 1).value
                        valueType=sheet_ipfield.cell(i, 2).value
                        value1=sheet_ipfield.cell(i, 3).value
                        value2=sheet_ipfield.cell(i, 5).value
        print(sheet_ipfield.cell(1, 0).value)
        print(field_name)
        print(operator)
        print(value1)
        print(valueType)
        print(value2)


if __name__ == '__main__':
    unittest.main()
