import unittest
from bs4 import BeautifulSoup

class testResult(object):
    def __init__(self, id, owner, title, status, pic, message, detail):
        self.id = id
        self.owner = owner
        self.title = title
        self.status = status
        self.pic = pic
        self.message = message
        self.detail = detail


class MyTestCase(unittest.TestCase):
    @unittest.skip
    def test_len_size(self):
        # result1 = testResult(id='1',owner='jon',title='login', status='pass',message='result message', pic='Average Length of Stay by Payer by Month.png')
        # result2 = testResult(id='2',owner='jon',title='login', status='fail',message='result message', pic='Case Mix Index (CMI) Comparison.png')
        # result3 = testResult(id='3',owner='jon',title='login', status='pass',message='result message', pic='Case Status Reimbursement Detail.png')
        # results = [result1, result2, result3]

        result1_detail = {'step1': {'status': 'pass', 'action': 'action description'},
                          'step2': {'status': 'pass', 'action': 'action description'},
                          'step3': {'status': 'fail', 'action': 'action description'}}

        result2_detail = {'step1': {'status': 'pass', 'action': 'action description'},
                          'step2': {'status': 'pass', 'action': 'action description'},
                          'step3': {'status': 'pass', 'action': 'action description'},
                          'step4': {'status': 'pass', 'action': 'action description'}}
        result3_detail = {'step1': {'status': 'pass', 'action': 'action description'},
                          'step2': {'status': 'pass', 'action': 'action description'},
                          'step3': {'status': 'pass', 'action': 'action description'},
                          'step4': {'status': 'fail', 'action': 'action description'}}
        print(result3_detail.keys())
        for i in result3_detail.keys():
            print(i)

    def test_insert_main_table(self):
        Fobj = open('beautifullSouptest.html')
        Data = Fobj.read()
        Fobj.close()
        soup_elements = BeautifulSoup(Data, features="lxml")

        # case result and detail
        result1_detail = {'step1':{'status':'pass', 'action':'action description','message':'message content'},
                          'step2':{'status':'pass', 'action':'action description','message':'message content'},
                          'step3':{'status':'fail', 'action':'action description','message':'message content'}}

        result2_detail = {'step1':{'status':'pass', 'action':'action description','message':'message content'},
                          'step2':{'status':'pass', 'action':'action description','message':'message content'},
                          'step3':{'status':'pass', 'action':'action description','message':'message content'},
                          'step4':{'status':'pass', 'action':'action description','message':'message content'}}

        result3_detail = {'step1':{'status':'pass', 'action':'action description','message':'message content'},
                          'step2':{'status':'pass', 'action':'action description','message':'message content'},
                          'step3':{'status':'pass', 'action':'action description','message':'message content'},
                          'step4':{'status':'fail', 'action':'action description','message':'message content'}}

        result1 = testResult(id='1', owner='jon', title='login', status='pass', message='result message',
                             pic='Average Length of Stay by Payer by Month.png',detail=result1_detail)
        result2 = testResult(id='2', owner='jon', title='login', status='fail', message='result message',
                             pic='Case Mix Index (CMI) Comparison.png', detail=result2_detail)
        result3 = testResult(id='3', owner='jon', title='login', status='pass', message='result message',
                             pic='Case Status Reimbursement Detail.png', detail=result3_detail)

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
            td_new_id = soup_elements.new_tag('td', style="color:red")
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

            # case detail
            atts_detail_tr = {'id': results[i].id, 'class': "case_detail", 'style': "display:"}
            detail_row_th = soup_elements.new_tag('tr', attrs=atts_detail_tr)

            # th
            detail_td_stepNum = soup_elements.new_tag('th', display=True)
            detail_td_stepNum.string = 'Step'
            detail_td_action = soup_elements.new_tag('th', display=True)
            detail_td_action.string = 'Action'
            detail_td_status = soup_elements.new_tag('th', display=True)
            detail_td_status.string = 'Status'
            detail_td_message = soup_elements.new_tag('th', display=True)
            detail_td_message.string = 'Message'

            detail_row_th.insert(position=0, new_child=detail_td_stepNum)
            detail_row_th.insert(position=1, new_child=detail_td_action)
            detail_row_th.insert(position=2, new_child=detail_td_status)
            detail_row_th.insert(position=3, new_child=detail_td_message)
            tr_new.insert_after(detail_row_th)



            for j in results[i].detail.keys():
                atts_detail_tr = {'id':results[i].id,'class':"case_detail",'style':"display:"}
                detail_row = soup_elements.new_tag('tr',attrs=atts_detail_tr)

                # td
                detail_td_stepNum = soup_elements.new_tag('td', display=True)
                detail_td_stepNum.string = j
                detail_td_action = soup_elements.new_tag('td', display=True)
                detail_td_action.string = results[i].detail[j]['action']
                detail_td_status = soup_elements.new_tag('td', display=True)
                detail_td_status.string = results[i].detail[j]['status']
                detail_td_message = soup_elements.new_tag('td', display=True)
                detail_td_message.string = results[i].detail[j]['message']

                detail_row.insert(position=0, new_child=detail_td_stepNum)
                detail_row.insert(position=1, new_child=detail_td_action)
                detail_row.insert(position=2, new_child=detail_td_status)
                detail_row.insert(position=3, new_child=detail_td_message)

                detail_row_th.insert_after(detail_row)


        file = open('beautifullSouptest.html','w')
        file.write(str(soup_elements))
        file.close()


if __name__ == '__main__':
    unittest.main()
