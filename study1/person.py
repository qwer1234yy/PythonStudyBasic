class person_:
    name = "dddd"
    def tell(self):
        print("什么鬼"+ self.name)
    def __init__(self, name):
        self.name = name
        print("Hi Person" + self.name)
a = person_("nameeeee")
a.tell()

class teacher(person_):
    age = 10
    __subject = "python"
    def __teach(self):
        print(self.name + "老师能上课")
b = teacher("teacher")
print("dddd" + b.age.__str__())
b.tell()
b.__teach()

class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0    # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print (self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
print (counter.publicCount)
print (counter.__secretCount)  # 报错，实例不能访问私有变量