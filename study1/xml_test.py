import unittest,os,exception
import xml.dom.minidom as xml

class MyTestCase(unittest.TestCase):
    def test_something(self):
        # 使用minidom解析器打开 XML 文档
        xmlfilepath = os.path.abspath("movies.xml")
        DOMTree = xml.Document
        movies= DOMTree.getElementsByTagName('movie')
        for i in movies:
            print(i)
        nodes=DOMTree.childNodes
        for i in nodes:
            print(i)


        create_movie = DOMTree.createElement('movie2')
        create_movie_title =create_movie.setAttribute('title','title')
        # create_movie_type = DOMTree.createElement('type')
        # create_movie_format= DOMTree.createElement('format')
        # create_movie_rating= DOMTree.createElement('rating')
        # create_movie_description= DOMTree.createElement('description')
        # create_movie.appendChild(create_movie_type)
        # create_movie.appendChild(create_movie_format)
        # create_movie.appendChild(create_movie_rating)
        # create_movie.appendChild(create_movie_description)
        DOMTree.appendChild(create_movie)
        # DOMTree.insertBefore(create_movie,DOMTree.getElementById('id1'))


    def test_create_xml(self):
        # 1.创建DOM树对象
        dom = xml.Document()
       # 2.创建根节点。每次都要用DOM对象来创建任何节点。
        root_node = dom.createElement('root')
        # 3.用DOM对象添加根节点
        dom.appendChild(root_node)
        book_node = dom.createElement('book')
        # 用父节点对象添加元素子节点
        root_node.appendChild(book_node)
        # 设置该节点的属性
        book_node.setAttribute('price', '199')
        name_node = dom.createElement('name')
        root_node.appendChild(name_node)
        # 也用DOM创建文本节点，把文本节点（文字内容）看成子节点
        name_text = dom.createTextNode('计算机程序设计语言 第1版')
        # 用添加了文本的节点对象（看成文本节点的父节点）添加文本节
        name_node.appendChild(name_text)

        # 每一个结点对象（包括dom对象本身）都有输出XML内容的方法，如：toxml()--字符串, toprettyxml()--美化树形格式。

        fh = open('dom_write.xml', 'w', encoding='UTF-8')
        # 4.writexml()第一个参数是目标文件对象，第二个参数是根节点的缩进格式，第三个参数是其他子节点的缩进格式，
        # 第四个参数制定了换行格式，第五个参数制定了xml内容的编码。

        dom.writexml(fh, indent='', addindent='\t', newl='\n', encoding='UTF-8')

        print('写入xml OK!')

    def test_dic(self):

        field1={'id': '12213', 'operators': 'ewe', 'type': 'wwe', 'default': 'wewewe'}
        field2={'id': '12213', 'operators': 'ewe', 'type': 'wwe', 'default': 'wewewe'}
        field3={'id': '12213', 'operators': 'ewe', 'type': 'wwe', 'default': 'wewewe'}
        field4={'id': '12213', 'operators': 'ewe', 'type': 'wwe', 'default': 'wewewe'}
        field5={'id': '12213', 'operators': 'ewe', 'type': 'wwe', 'default': 'wewewe'}

        fields_list = [field1,field2,field3,field4,field5]
        fields_len = len(fields_list)

        for i in range(0, fields_len-1):
            print(fields_list[i])

        for i in fields_list[0]:
            print(i)


    def test_write_dics_to_xml(self):

        field1 = {'id': '12213', 'operators': 'ewe', 'type': 'wwe', 'default': 'wewewe'}
        field2 = {'id': '12213', 'operators': 'ewe', 'type': 'wwe', 'default': 'wewewe'}
        field3 = {'id': '12213', 'operators': 'ewe', 'type': 'wwe', 'default': 'wewewe'}
        field4 = {'id': '12213', 'operators': 'ewe', 'type': 'wwe', 'default': 'wewewe'}
        field5 = {'id': '12213', 'operators': 'ewe', 'type': 'wwe', 'default': 'wewewe'}

        dics_list = [field1, field2, field3, field4, field5]
        dics_len = len(dics_list)

        # 文件名字
        file_name = "cs_fields.xml"

        # 配置节点三要素
        root_name = 'Fields'
        sub_node_name = 'Field'
        attributes = []
        for i in dics_list[0]:
            attributes.append(i)

        doc = xml.Document()
        fields_node = doc.createElement(root_name)

        for i in range(0, dics_len):
            field = sub_node_name
            field_node = doc.createElement(field)
            for j in range(0, len(attributes)):
                print(attributes[j])
                print(dics_list[i][attributes[j]])
                field_node.setAttribute(attributes[j], dics_list[i][attributes[j]])

            fields_node.appendChild(field_node)

        doc.appendChild(fields_node)

        xml_file_path = os.path.abspath(file_name)
        f = open(xml_file_path, 'w', encoding='UTF-8')
        doc.writexml(f, indent='', addindent='\t', newl='\n', encoding='UTF-8')



if __name__ == '__main__':
    unittest.main()
