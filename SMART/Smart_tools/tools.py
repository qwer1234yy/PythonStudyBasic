import xml.dom.minidom as xml
import os


def spide_write_to_txt(s, file_path):
    try:
        # '../Smart_commons/cs_operators.txt'
        f = open(file_path, 'a')
        f.writelines(s)
        f.write('\n')
    finally:
        if f:
            f.close()


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