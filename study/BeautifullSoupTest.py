import unittest
from bs4 import BeautifulSoup

class testResult(object):
    def __init__(self, id, owner, title, status, pic, message):
        self.id = id
        self.owner = owner
        self.title = title
        self.status = status
        self.pic = pic
        self.message = message


class MyTestCase(unittest.TestCase):

    def test_len_size(self):
        result1 = testResult(id='1',owner='jon',title='login', status='pass',message='result message', pic='Average Length of Stay by Payer by Month.png')
        result2 = testResult(id='2',owner='jon',title='login', status='fail',message='result message', pic='Case Mix Index (CMI) Comparison.png')
        result3 = testResult(id='3',owner='jon',title='login', status='pass',message='result message', pic='Case Status Reimbursement Detail.png')
        results = [result1, result2, result3]

        len_total = len(results)
        len_pass = 0
        len_fail = 0
        for i in range(0, len_total):
            print(str(results[i].status).upper())
            if 'PASS' in str(results[i].status).upper():
                len_pass = len_pass + 1
            elif 'FAIL' in str(results[i].status).upper():
                len_fail = len_fail + 1
        print(len_pass)
        print(len_fail)

    def test_insert_main_table(self):
        Fobj = open('beautifullSouptest.html')
        Data = Fobj.read()
        Fobj.close()
        soup_elements = BeautifulSoup(Data, features="lxml")

        result1 = testResult(id='1', owner='jon', title='login', status='pass', message='result message',
                             pic='Average Length of Stay by Payer by Month.png')
        result2 = testResult(id='2', owner='jon', title='login', status='fail', message='result message',
                             pic='Case Mix Index (CMI) Comparison.png')
        result3 = testResult(id='3', owner='jon', title='login', status='pass', message='result message',
                             pic='Case Status Reimbursement Detail.png')

        results = [result1, result2, result3]
        len_total = len(results)
        len_pass = 0
        len_fail = 0
        for i in range(0, len_total):
            if 'PASS' in str(results[i].status).upper():
                len_pass=len_pass+1
            elif 'FAIL' in str(results[i].status).upper():
                len_fail =len_fail+ 1

        total_case_tag = soup_elements.select_one('.total_Cases')
        pass_case_tag = soup_elements.select_one('.pass_case')
        fail_case_tag = soup_elements.select_one('.fail_case')
        total_case_tag.clear()
        total_case_tag.append(len_total.__str__())
        pass_case_tag.clear()
        pass_case_tag.append(len_pass.__str__())
        fail_case_tag.clear()
        fail_case_tag.append(len_fail.__str__())


        row = soup_elements.select_one('#main_table tbody tr')
        # insert one row
        for i in range(0,len_total):
            tr_new = soup_elements.new_tag('tr')
            td_new_id = soup_elements.new_tag('td')
            td_new_id.string = results[i].id
            td_new_owner = soup_elements.new_tag('td')
            td_new_owner.string = results[i].owner
            td_new_title = soup_elements.new_tag('td')
            td_new_title.string = results[i].title
            if 'PASS' in str(results[i].status).upper():
                td_new_status = soup_elements.new_tag('td', bgcolor="#28ff5c")
            elif 'FAIL' in str(results[i].status).upper():
                td_new_status = soup_elements.new_tag('td', bgcolor="#f08080")
            td_new_status.string = results[i].status
            td_new_message = soup_elements.new_tag('td')
            td_new_message.string = results[i].message
            td_new_pic = soup_elements.new_tag('td')
            a_new_pic = soup_elements.new_tag('a', href='../pics/'+ results[i].pic)
            a_new_pic.string = results[i].pic
            td_new_pic.insert(position=0, new_child=a_new_pic)

            tr_new.insert(position=0,new_child=td_new_id)
            tr_new.insert(position=1, new_child=td_new_owner)
            tr_new.insert(position=2, new_child=td_new_title)
            tr_new.insert(position=3, new_child=td_new_status)
            tr_new.insert(position=4, new_child=td_new_message)
            tr_new.insert(position=5, new_child=td_new_pic)

            row.insert_after(tr_new)

        file = open('beautifullSouptest.html','w')
        file.write(str(soup_elements))
        file.close()


if __name__ == '__main__':
    unittest.main()
