import unittest,datetime,openpyxl


class MyTestCase(unittest.TestCase):
    def test_create(self):

        wb = openpyxl.Workbook()

        # grab the active worksheet
        ws = wb.active
        ws.title = 'IP'

        # Data can be assigned directly to cells
        # ws['A1'] = 42

        # Rows can also be appended
        ws.append(['Report Module','Report Name','Saved Search','Result','Screen Shot'])
        ws.append(['Report Module', 'Report Name', 'Saved Search', 'Result', 'Screen Shot'])
        ws.append(['Report Module', 'Report Name', 'Saved Search', 'Result', 'Screen Shot'])
        ws.append(['Report Module', 'Report Name', 'Saved Search', 'Result', 'Screen Shot'])

        # Python types will automatically be converted
        # ws['A2'] = datetime.datetime.now()

        # Save the file
        wb.save("legacy reports auto test result.xlsx")

    def test_read(self):
        file_path = 'legacy reports auto test result.xlsx'
        wb = openpyxl.load_workbook(file_path)
        ip_sheet = wb['IP']
        ip_sheet.column_dimensions['A'].width = 20
        ip_sheet.column_dimensions['B'].width = 20
        ip_sheet.column_dimensions['C'].width = 20
        ip_sheet.column_dimensions['D'].width = 20
        ip_sheet.column_dimensions['E'].width = 20

        # nrows = ip_sheet.max_row

        cell = ip_sheet.cell(row=2, column=1).value = 'test'
        # print(cell.value)
        # ip_sheet.append(['Report Module', 'Report Name', 'Saved Search', 'Result', 'Screen Shot'])

        wb.save(file_path)



if __name__ == '__main__':
    unittest.main()
