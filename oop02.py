class person:
    def __init__(self,name,age,gender):
         self.name=name
         self.age=age
         self.gender=gender


    def setdata(self):
         print("i am "+ self.name)
         print("i am "+self.age)
         print("i am "+self.gender)


p=person("ayush","21","male")
p.setdata()


class student(person):
       def __init__(self,name,age,gender,doing):
         person.__init__(self,name,age,gender)
         self.doing=doing
       def setdata(self):
         print("i am  "+self.name+"  i am doing "+self.doing)
s=student("anny","21","male","police")
s.setdata()
