class Employee:
    def __init__(self,name,age,language):
        self.name=name
        self.age=age
        self.language=language
        print("{} is {} years old and speaks {}".format(name,age,language))
class man(Employee):
    pass
a = Employee("abc",10,"eng")
b=Employee("xyz",20,"eng'")
print(a.name,a.age)
c=man("sai",22,"spanish")