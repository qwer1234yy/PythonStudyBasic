print('hello python')
name = 'Jon'
age = 25
weight = 120.50
introduce = 'I am '+name+', I am ' + age.__str__() + ' years old'
print(introduce)
print(type(name))

me = {
    "name": "jon",
    'age': 12,
    'weight': 120
}
hobbies = ['java', 'python', 'C#']
print(hobbies[0])
print(me["name"]+'----------------class------------')


class Peaple:

    name = 'yang'
    age = 24

    def __init__(self, address, hobbies):

        self.address = address
        self.hobbies = hobbies

    def _self_introduce_(self):
        print(self.name+self.age.__str__()+self.address+self.hobbies)


student = Peaple('shanghai', 'java')
print(student.name+student.address)
student._self_introduce_()

myTuple = ("apple", "banana", "cherry")
myIt = iter(myTuple)

print(next(myIt))
print(next(myIt))
print(next(myIt))

myStr = "banana"
myIte = iter(myStr)

print(next(myIte))
print(next(myIte))
print(next(myIte))
print(next(myIte))
print(next(myIte))
print(next(myIte))

for y in myStr:

 print(y)


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
