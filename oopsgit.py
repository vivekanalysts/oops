#
class student:
    def getstudent(self):
        self.__rollno=(input("Enter roll number:"))
        self.__name=(input("Enter name:"))
    def getmarks(self):
        self.__p=(input("enter physica marks:")) 
        self.__c=(input("enter chemistry marks:"))
        self.__m=(input("enter math marks:"))
    def showresult(self):
        print("roll number:",self.__rollno)
        print("name:",self.__name)
        print("physics:",self.__p)
        print("chemistry:",self.__c)
        print("math:",self.__m)

s=student()
# m=student()
s.getstudent()
s.getmarks()
s.showresult
   
#=====================================
class student:
    def getstudent(self):
        self.__rollno=(input("Enter roll number:"))
        self.__name=(input("Enter name:"))
    def getmarks(self):
        self.__p=(input("enter physica marks:")) 
        self.__c=(input("enter chemistry marks:"))
        self.__m=(input("enter math marks:"))
    def showresult(self):
        print("roll number:",self.__rollno)
        print("name:",self.__name)
        print("physics:",self.__p)
        print("chemistry:",self.__c)
        print("math:",self.__m)
        self. getgrade()

    def getgrade(self):
        t=self.___p+self.__c+self.__m
        p=t/3
        if(p>=80):
           grade="A"
        elif(p>=60 and 79<=p): 
           grade="B"
        else:
           grade="c" 

        print(f"total:{t:.f}")
        print(f"percentage:{p:.f}")
        print(f"grade:{grade:.f}")     
 
n = int(input("Enter n:"))
ls=[]
for i in range(n):

 s=student()
 s.getstudent()
 s.getmarks()
 ls.append(s)

for s in ls:
   print(s)
   s.showresult()


#=====================================



class student:
    def getstudent(self):
        self.__rollno=input("Enter roll number:")
        self.__name=input("Enter name:")

    def getmarks(self):
        self.__p=int(input("Enter physica marks:")) 
        self.__c=int(input("Enter chemistry marks:"))
        self.__m=int(input("Enter math marks:"))

    def showResult(self):
        print("Roll number:",self.__rollno)
        print("Name:",self.__name)
        print("Physics:",self.__p)
        print("Chemistry:",self.__c)
        print("Math:",self.__m)
        self.getGrade()
        
        

    def getGrade(self):
        t=self.__p+self.__m+self.__c
        p=t/3

        if (p>= 80):
             grade ="A"
        elif(p >=60 and p<=79):
             grade ="B"
        else:
             grade ="C"

        print(f"Total: {t:.1f}")
        print(f"Percentage: {p:.1f}")
        print(f"Grade:{grade}")

    def search (self,rollno):

        if (self.__rollno==rollno):
              self.showResult()
              return True
        return False
        
    
 
n=int(input("Enter N:"))
LS=[]
for i in range(n):

 s=student()
 s.getstudent()
 s.getmarks()
 LS.append(s)

rollno=input("Enter Roll Number u want to search1:")
for s in LS:
    found=s.search(rollno)
    if (found):break

if(not found):
    print(rollno,"Roll Number not exist" )

    
#=====================================



class person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def showperson(self):
        print(self.__name,self.__age)
    def __del__(self):
        print("person destory",self.__name,self.__age)

p1=person("peter",25)
p2=person("Herry",35)
p1.showperson()
del p1
p2.showperson()
input("End of program")   


#=======================

class person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def showperson(self):
        print(self.__name,self.__age)
    def __del__(self):
        print("person destory",self.__name,self.__age)

p1=person("peter",25)
p1.showperson()
p1=person("Herry",36)
p1.showperson()
input("End of program")   

#========================================

class Alien:
    total=0
    def __init__(self,type):
        if(type=='red'):
            self.__point=10
            self.__type='red'
        elif(type=='green'):
            self.__point=20
            self.__type='green'
    @classmethod
    def showpoint(cls):
        print("Total Points:",cls.total) 

    def __del__(self):
        Alien.total+=self.__point
        print("Alien",self.__type,"Destroyed")

A1=Alien('red')
A2=Alien('green')
A3=Alien('green')
Alien.showpoint()
del A2
Alien.showpoint()
del A1
input("end")

#==============================================



class employee:
    def getemployee(self):
        self.__name=(input("Enter name:"))
        self.__id=(input("Enter identity:"))
        self.__salary=(float(input("Enter basic salary:")))



    def showemployee(self):
        print("Name:",self.__name)
        print("ID:",self.__id) 
        print("salary:",self.__salary)  

    def getnetsalary(self):
        self.__da=self.__basic*20/100
        self.__hra=self.__basic*12/100
        self.__pf=self.__basic*12/100
        self.__netsalary = self.__basic + self.__da + self.__hra - self.__pf
        return self.__netsalary
    
    def showsalary(self):
        print=("da:",self.__da)
        print=("hra:",self.__hra)
        print=("pf:",self.__pf)
        print=("netsalary:",self.__netsalary)


e=employee()
e.getemployee()
e.showemployee()
e.getnetsalary()
e.showsalary()


#==============================================


class twonum:
     
 def gettwonum(self):
    self.__x=int(input("enter x="))
    self.__y=int(input("enter y="))

 def add(self):
   a=self.__x+self.__y
   print(f"sum={a}")

 def sub(self):
   b=self.__x-self.__y
   print(f"sub={b}")

 def multiply(self):
   c=self.__x*self.__y
   print(f"multiply={c}")

 def division(self):
   d=self.__x/self.__y
   print(f"division={d}")

 def power(self):
   e=self.__x**self.__y
   print(f"power={e}")

 def minmax(self):
   if(self.__x>self.__y):
      print(f"max={self.__x}\nmin={self.__y}")
   else:
      print(f"max={self.__y}\nmin={self.__x}")

t=twonum()
t.gettwonum()
t.add()
t.division()
t.minmax()
t.power()
t.sub()


#========================================

class Product:
    
    def prod(self):
        self.__productid = int(input("Enter ID: "))
        self.__catagory = input("Enter Category: ")
        self.__productname = input("Enter Product Name: ")
        self.__productrate = int(input("Enter Rate: "))

    def showproduct(self):
        print("Product ID:", self.__productid)
        print("Category:", self.__catagory)
        print("Product Name:", self.__productname)
        print("Rate:", self.__productrate)

    def searchid(self, id):
        if self.__productid == id:
            self.showproduct()
            return True
        return False

    def searchcat(self, cat):
        if self.__catagory.lower() == cat.lower():
            self.showproduct()
            return True
        return False

    def searchpat(self, pat):
        if pat.lower() in self.__productname.lower():
            self.showproduct()
            return True
        return False


# Main Program
i = int(input("Enter how many products:? "))
b = []

for i in range(i):
    p = Product()
    p.prod()
    b.append(p)

#search by id

id = int(input("Search ID: "))

found = False

for i in b:
    found = i.searchid(id)
    if found:break
        

if not found:
    print("Product doesn't exist...")


#search by catargory
#cat=input("search by catargory:")
#for i in b:
#   i.searchcat(cat)

# search by pattern

# pat=input("enter pattern:")
# for i in b :
#     i.searchpat(pat)

        
#========================================

class Bank:
    def openAccount(self):
        self.__acno=input("Enter Account Number:")
        self.__name=input("Enter name:")
        self.__balance=int(input("Enter balance:"))
        return self.__acno

    def showAccount(self):
        print(self.__acno,self.__name,self.__balance) 
         
    def Deposit(self):
        amt=int(input("Enter Amount u want to Deposit:"))
        self.__balance+=amt

    def withdrawal(self):
        amt=int(input("Enter Amount u want to withdraw:"))
        if(self.__balance>=amt):
           self.__balance-=amt

        else:
            print("Insufficiant Balance...")


n=int(input("Enter N:"))
C={}
for i in range (n):
     B=Bank()
     acno=B.openAccount()
     C.setdefault(acno,B)

print("SBI Main Manu") 
print("1:Display All")   
print("2:Search By Account No")  
print("3:Deposit")   
print("4:withdrawal")
print("5:Exit")   
ch=int(input ("Enter Choice:"))

match ch:
    case 1:
        for customer in C.values():
            customer.showAccount()         


#========================================

class Bank:
    def openAccount(self):
        self.__acno=input("Enter Account Number:")
        self.__name=input("Enter name:")
        self.__balance=int(input("Enter balance:"))
        return self.__acno

    def showAccount(self):
        print(self.__acno,self.__name,self.__balance) 
         
    def Deposit(self):
        amt=int(input("Enter Amount u want to Deposit:"))
        self.__balance+=amt

    def withdrawal(self):
        amt=int(input("Enter Amount u want to withdraw:"))
        if(self.__balance>=amt):
           self.__balance-=amt

        else:
            print("Insufficiant Balance...")


n=int(input("Enter N:"))
C={}
for i in range (n):
     B=Bank()
     acno=B.openAccount()
     C.setdefault(acno,B)
while(True):

    print("SBI Main Manu") 
    print("1:Display All")   
    print("2:Search By Account No")  
    print("3:Deposit")   
    print("4:withdrawal")
    print("5:Exit")   
    ch=int(input ("Enter Choice:"))
    match ch:

        case 1:
            for customer in C.values():
                customer.showAccount()
                
        case 2:
                acno=int(input("Enter Account Number u want to search"))  
                customer=C.get(acno,"Customer Not Exits  ") 
                if(isinstance(customer,Bank)):
                    customer.showAccount()
                else:
                    print(customer)

        case 3:
                acno=int(input("Enter Account Number u want to search for Deposit"))  
                customer=C.get(acno,"Customer Not Exits  ") 
                if(isinstance(customer,Bank)):
                    customer.showAccount()
                    customer.Deposit
                else:
                    print(customer)


        case 4:
                acno=int(input("Enter Account Number u want to search for Whitdraw"))  
                customer=C.get(acno,"Customer Not Exits  ") 
                if(isinstance(customer,Bank)):
                    customer.showAccount()
                    customer.withdrawal
                else:
                    print(customer)

        case 5:
            print('Good by')
        case 6:
            print('wrong option')

            if(ch==5):
                break

                
        
#========================================