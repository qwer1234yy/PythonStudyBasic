from bs4 import BeautifulSoup
import requests
if __name__ == "__main__":
     target = 'http://www.biqukan.com/1_1094/5403177.html'

     req = requests.get(url=target)
     html = req.text
     bf = BeautifulSoup(html, features="html.parser")
     text1 = bf.find_all('div', id_='content')
     text2 = bf.find_all('div', class_='showtxt')
     print(text1)
     print(text2)
     print(text2[0].text.replace('\xa0' * 8, '\n\n'))


     for i in text2:
         print("text2")
         print(i.text)

     # target2 = 'https://www.biqukan.com/xuanhuanxiaoshuo/'
     target2 = 'https://www.biqukan.com/xuanhuanxiaoshuo/'
     reb = requests.get(url=target2)
     # print("req"+reb.__str__())
     html = reb.text
     # print("html"+html)
     bf = BeautifulSoup(html, features="html.parser")
     # print("bf"+bf.__str__())
     li_tags = bf.find_all("li")
     for a in li_tags:
        print(a.text)

     #
     nav_li = bf.find_all("div",class_="nav")
     for li in nav_li:
        print(li.text)

books = bf.find_all("div", class_="bd")

for li in books:
    print(li.text)

books_type = bf.find_all("span", class_="s1")
for li in books_type:
    print("s1"+li.text)


books_name = bf.find_all("span", class_="s2")
for li in books_name:
    print("s2"+li.text)

books_author = bf.find_all("span", class_="s4")
for li in books_author:
       print("s4"+li.text)
booksBox={'book_type': books_type[0].text,'book_name': books_name[0].text,'book_author':books_author[0].text}
print(booksBox)
booksList = []
print(books_type.__len__())
print(+books_name.__len__())
print(+books_author.__len__())



booksList = []
for i in range(30):
    booksBox = {'book_type': books_type[i].text, 'book_name': books_name[i].text, 'book_author': books_author[i].text}
    booksList.append(booksBox)

print("end")
#print(booksList)

for b in booksList:
 print(b)
