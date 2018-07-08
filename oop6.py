class methodoverloading(): 
        def demo(self,name=None,age=None):
           if(name!=None and age!=None):
               print("name : "+self.name+ "\n" +"age : "+self.age)
           elif(name==None):
               print("age : "+self.age)
           elif(age==None):
               print("name : "+self.name)
std=methodoverloading()
std.demo("ayush")

