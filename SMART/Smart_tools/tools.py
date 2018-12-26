import xml.dom.minidom as xml
from bs4 import BeautifulSoup
import os
from SMART.Smart_tools.testResult import testResult


def spide_write_to_txt(s, file_path):
    try:
        # '../Smart_resources/cs_operators.txt'
        f = open(file_path, 'a')
        f.writelines(s)
        f.write('\n')
    finally:
        if f:
            f.close()
def write_html_report_dic(results):
    # results
    print('write_html_report_dic')
    Fobj = open('beautifullSouptest.html')
    Data = Fobj.read()
    Fobj.close()
    soup_elements = BeautifulSoup(Data, features="lxml")

    # case result and detail
    # result1_detail = {'step1': {'status': 'pass', 'action': 'action description', 'message': 'message content',
    #                             'pic_path': 'Average Length of Stay by Payer by Month.png'},
    #                   'step2': {'status': 'pass', 'action': 'action description', 'message': 'message content',
    #                             'pic_path': 'Average Length of Stay by Payer by Month.png'},
    #                   'step3': {'status': 'fail', 'action': 'action description', 'message': 'message content',
    #                             'pic_path': 'Average Length of Stay by Payer by Month.png'}}
    #
    # result2_detail = {'step1': {'status': 'pass', 'action': 'action description', 'message': 'message content',
    #                             'pic_path': 'Average Length of Stay by Payer by Month.png'},
    #                   'step2': {'status': 'pass', 'action': 'action description', 'message': 'message content',
    #                             'pic_path': 'Average Length of Stay by Payer by Month.png'},
    #                   'step3': {'status': 'pass', 'action': 'action description', 'message': 'message content',
    #                             'pic_path': 'Average Length of Stay by Payer by Month.png'},
    #                   'step4': {'status': 'pass', 'action': 'action description', 'message': 'message content',
    #                             'pic_path': 'Average Length of Stay by Payer by Month.png'}}
    #
    # result3_detail = {'step1': {'status': 'pass', 'action': 'action description', 'message': 'message content',
    #                             'pic_path': 'Average Length of Stay by Payer by Month.png'},
    #                   'step2': {'status': 'pass', 'action': 'action description', 'message': 'message content',
    #                             'pic_path': 'Average Length of Stay by Payer by Month.png'},
    #                   'step3': {'status': 'pass', 'action': 'action description', 'message': 'message content',
    #                             'pic_path': 'Average Length of Stay by Payer by Month.png'},
    #                   'step4': {'status': 'fail', 'action': 'action description', 'message': 'message content',
    #                             'pic_path': 'Average Length of Stay by Payer by Month.png'}}
    #
    # result1 = testResult(id='TC001', owner='robbin', title='login', status='pass', message='result message',
    #                      pic='Average Length of Stay by Payer by Month.png', detail=result1_detail)
    # result2 = testResult(id='TC002', owner='reeta', title='login', status='fail', message='result message',
    #                      pic='Case Mix Index (CMI) Comparison.png', detail=result2_detail)
    # result3 = testResult(id='TC003', owner='jon', title='login', status='pass', message='result message',
    #                      pic='Case Status Reimbursement Detail.png', detail=result3_detail)
    #
    # results = [result1, result2, result3]
    new_results_len = len(results)

    total_case_tag = soup_elements.select_one('.total_Cases')
    pass_case_tag = soup_elements.select_one('.pass_case')
    fail_case_tag = soup_elements.select_one('.fail_case')
    print('-------------------------------')
    print(total_case_tag.string + pass_case_tag.string + fail_case_tag.string)

    len_total = int(total_case_tag.string) + new_results_len
    len_pass = int(pass_case_tag.string)
    len_fail = int(fail_case_tag.string)

    for i in range(0, len(results)):
        if 'PASS' in str(results[i].status).upper():
            len_pass = len_pass + 1
        elif 'FAIL' in str(results[i].status).upper():
            len_fail = len_fail + 1

    total_case_tag.clear()
    total_case_tag.append(len_total.__str__())
    pass_case_tag.clear()
    pass_case_tag.append(len_pass.__str__())
    fail_case_tag.clear()
    fail_case_tag.append(len_fail.__str__())

    row = soup_elements.select_one('#main_table tbody tr')
    # insert one row
    for i in range(0, new_results_len):
        attrs = {'class': 'case', 'id': results[i].id}
        tr_new = soup_elements.new_tag('tr', attrs=attrs)
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
        a_new_pic = soup_elements.new_tag('a', href='../pics/' + results[i].pic)
        a_new_pic.string = results[i].pic
        td_new_pic.insert(position=0, new_child=a_new_pic)

        tr_new.insert(position=0, new_child=td_new_id)
        tr_new.insert(position=1, new_child=td_new_owner)
        tr_new.insert(position=2, new_child=td_new_title)
        tr_new.insert(position=3, new_child=td_new_status)
        tr_new.insert(position=4, new_child=td_new_message)
        tr_new.insert(position=5, new_child=td_new_pic)

        row.insert_after(tr_new)

        # case detail
        atts_detail_tr = {'class': str(results[i].id), 'style': "display:none"}
        detail_row_th = soup_elements.new_tag('tr', attrs=atts_detail_tr)

        # th
        atts_detail_td = {'class': 'case_detail', 'style': "text-align:center"}
        detail_td_stepNum = soup_elements.new_tag('th', attrs=atts_detail_td)
        detail_td_stepNum.string = 'Step'
        detail_td_action = soup_elements.new_tag('th', attrs=atts_detail_td)
        detail_td_action.string = 'Action'
        detail_td_status = soup_elements.new_tag('th', attrs=atts_detail_td)
        detail_td_status.string = 'Status'
        detail_td_message = soup_elements.new_tag('th', attrs=atts_detail_td)
        detail_td_message.string = 'Message'
        detail_td_pic = soup_elements.new_tag('th', attrs=atts_detail_td)
        detail_td_pic.string = 'Pic'

        detail_row_th.insert(position=0, new_child=detail_td_stepNum)
        detail_row_th.insert(position=1, new_child=detail_td_action)
        detail_row_th.insert(position=2, new_child=detail_td_status)
        detail_row_th.insert(position=3, new_child=detail_td_message)
        detail_row_th.insert(position=4, new_child=detail_td_pic)
        tr_new.insert_after(detail_row_th)

        for j in results[i].detail.keys():
            atts_detail_tr = {'class': str(results[i].id), 'style': "display:none"}
            detail_row = soup_elements.new_tag('tr', attrs=atts_detail_tr)

            # td
            detail_td_stepNum = soup_elements.new_tag('td')
            detail_td_stepNum.string = j
            detail_td_action = soup_elements.new_tag('td')
            detail_td_action.string = results[i].detail[j]['action']

            if 'PASS' in str(results[i].detail[j]['status']).upper():
                detail_td_status = soup_elements.new_tag('td', bgcolor="#28ff5c")
            elif 'FAIL' in str(results[i].detail[j]['status']).upper():
                detail_td_status = soup_elements.new_tag('td', bgcolor="#f08080")

            detail_td_status.string = results[i].detail[j]['status']
            detail_td_message = soup_elements.new_tag('td')
            detail_td_message.string = results[i].detail[j]['message']
            detail_td_pic = soup_elements.new_tag('td')
            detail_td_pic_a = soup_elements.new_tag('a', href='../pics/' + results[i].detail[j]['pic_path'])
            detail_td_pic_a.string = results[i].detail[j]['pic_path']
            detail_td_pic.insert(position=0, new_child=detail_td_pic_a)

            detail_row.insert(position=0, new_child=detail_td_stepNum)
            detail_row.insert(position=1, new_child=detail_td_action)
            detail_row.insert(position=2, new_child=detail_td_status)
            detail_row.insert(position=3, new_child=detail_td_message)
            detail_row.insert(position=4, new_child=detail_td_pic)

            detail_row_th.insert_after(detail_row)

    file = open('beautifullSouptest.html', 'w')
    file.write(str(soup_elements))
    file.close()


def write_dics_list_to_xml(root_node_name, sub_node_name, dics_list, xml_file_path):
    # field1 = {'id': '12213', 'operators': 'ewe', 'type': 'wwe', 'default': 'wewewe'}
    # field2 = {'id': '12213', 'operators': 'ewe', 'type': 'wwe', 'default': 'wewewe'}
    # field3 = {'id': '12213', 'operators': 'ewe', 'type': 'wwe', 'default': 'wewewe'}
    # field4 = {'id': '12213', 'operators': 'ewe', 'type': 'wwe', 'default': 'wewewe'}
    # field5 = {'id': '12213', 'operators': 'ewe', 'type': 'wwe', 'default': 'wewewe'}
    #
    # dics_list = [field1, field2, field3, field4, field5]
    dics_len = len(dics_list)

    # 文件名字
    file_name = "cs_fields.xml"

    # 配置节点三要素
    root_name = root_node_name
    sub_ele_name = sub_node_name
    attributes = []
    for i in dics_list[0]:
        attributes.append(i)

    doc = xml.Document()
    fields_node = doc.createElement(root_name)

    for i in range(0, dics_len):
        field = sub_ele_name
        field_node = doc.createElement(field)
        for j in range(0, len(attributes)):
            print(attributes[j])
            print(dics_list[i][attributes[j]])
            field_node.setAttribute(attributes[j], dics_list[i][attributes[j]])
        field_node_text = doc.createTextNode(dics_list[i]['id'])
        fields_node.appendChild(field_node)
        field_node.appendChild(field_node_text)

    doc.appendChild(fields_node)

    # xml_file_path = os.path.abspath(file_name)
    f = open(xml_file_path, 'w', encoding='UTF-8')
    doc.writexml(f, indent='', addindent='\t', newl='\n', encoding='UTF-8')

def file_exist_delete(file_path):
    if os.path.exists(file_path):
        print('------------file_exists_delete-----------')
        os.remove(file_path)