class employee:
       raise_amount=1.04   
       num_of_emp=0
   

       def __init__(self,first,last,pay):
          self.first=first
          self.last=last
          self.pay=pay
          self.email=first+"."+last+"@company.com"
          self.detail='Name : '+first.title()+  " "  +last.title()+"\n"+"pay : "+str(pay)+"\n"+"E-mail : "+first+"."+last+"@company.com"
                
          employee.num_of_emp+=1
   
       def fullname(self):
          return '{} {}'.format(self.first,self.last)
          

       def apply_raise(self):
        return  int(self.pay*employee.raise_amount)
       
       def set_raise_amt(cls,amount):
           cls.raise_amt=amount

emp_1=employee(" ayush","pandey",50000)
emp_2=employee("anant","dubey",60000)


print(employee.num_of_emp)
print(emp_1.fullname())
print(emp_2.fullname())
print(emp_1.detail)
print(emp_2.pay)
print(emp_2.apply_raise())




         

