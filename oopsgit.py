
#                             OOPS

#Object oriented programming
#-------------------------

# object are real world entities

#object
#-----------

# data security
#real world
#reusability
#polymorphism

# how to create an object?
# behavioir = show the things that which was that 
# state
#aggregation and assosiation
# identity



# class 
#------

#- classes are logical abstraction 
#- class is a factory with is use to product an object


# object
#--------

#- instance of class 
#- classes are logical abstraction while object have physical existance 

# componds of oops 
#-----------------------

# class and object 

# syntax 
#class <classname>:

#class contains three type of member 

#- private members 
#- these member are totlly hidden and can not access by any external funcation even main program
# only  the member funcation which declear in public section of class can aceess

# ex
#   __x

# public members 
 
#member which declear in public section of class can acees by any external funcation even main program with the help of object name 

# ex
# x__ use for public 

# protected 

#  __x  - for prive (protected)


#===============================================================================

# static members
# --------------
# - these are class members 
# -class veriable:
#    only one copy of class vriable is created for the entire class
#    no matter how many object created  

# class method
# -------------------
# -can acces only static member only class
# -Invoke with the help of class name only


# @classmethod
# @staticmethod



# constructore
#--------------
#- by default each class contains a default constructore which is not visible 
#- constractore are use to instantiate(memory allocation) an object at the time of  object declaration
# __init__(self) is use to define our own  constractore within the class

# why constractore ?
# to instantiate as well  as initiate an object at the time of object declaration

#- constractore invoke implicitly at the time of object declaration


# B=Bank()
# Bank() constractore call the __init__() funcation

# constractore use for initate ,object declaretion karete samaye
# constractact invoke impliciltly when object are declear


#destructor 
#-------------

#one can define destructor funcation __del__()
# destructor funcation invoke impliciltly before destroying any object



# object as an argument 
#------------------------

# use to establish communication between two more object of same class as well as different class


# INHERITANCE =LECTURE 32 
#------------------------------

# WHY INHERITANCE ?
#- USE TO GENERALIZE AND SPECIALIZE THE CLASS SPECIFICATION 
#- USE TO INHERIT THE FEATURES OF BASE CLASS IN DERIVE CLASS 

#- ALL THE PRIVATE MEMBER OF BASE CLASS ARE TOTALLY HIDDEN AND CAN NOT ACCESS BY DERIVE CLASS DIRECTLY ONLY PUBLIC AND PROTECTED MEMBER OF BASE CLASS CAN ACCESS BY CHILD CLASS DIRECTLY


# TYPE OF INHERITANCE 
#- SINGLE INHERITANCE
#-MULTIPLE INHERITANCE
#- HIERARCHI INHERITANCE
#- MULTILEVEL INHERITANCE
#- HYBRIED INHERITANCE


# SINGLE INHERITANCE
#----------------

# HIERARCHI INHERITANCE
#-----------------------


# MULTI LEVEL INHERITANCE
#---------------------------


# FUNCATION OVERLODING IN INHERITANCE
#------------------------------------
#-- WHEN BASE CLASS OR DERIVE CLASS CONTAINS SAME NAME OF FUNCATIONS
#-TO CALL THE BASE CLASS FUNCATION WE CAN USE SUPER KEYWORD
#- SUPER().SHOW()


# CONSTRUCTOR IN INHERITENCE 
# BY DEFAULT DERIVE CLASS DEFAULT CONSTRUCTOR IMPLICITLY CALL THE BASE CLASS DEFAULT CONSTRUCTOR

  

#polymorphism
#------------


# class animal:
#    def sound(self):
#     print("makes sound")

# class dog(animal):
#   def sound(self):
#     print("dog breaks")


# class cat(animal):
#   def sound(self):
#     print("cat mewww")
# A.animal()
# A.sound()

# abstract class
#--------------------
# -one can not instantiate(create) its object 
#- also know as must inherit class

# abstract method 
#----------------
#- they have no body structure
#-they must be define in abstract class
#- they must be redefine in derive class to achive RTP








#============================================================================
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
   
#============================================================================

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

    
#============================================================================

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


#============================================================================


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


#============================================================================

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

#============================================================================
class product:
    def getproduct(self):
        self.__proid=int(input("Enter Product ID:"))
        self.__proname=int(input("Enter Product Name: "))
        self.__proprice=float(input("Enter Prpduct price: "))
        self.__stock=int(input("Enter stock: "))


    def showproduct(self):
        print("ID:",self.__proid)
        print("Name:",self.__proname)
        print("Price:",self.__proprice)
        print("Quantity  Stock:",self.__stock)


    def purproduct(self):
     
     qty=int(input("Enter Quantity of purchase:"))
     self.__stock+=qty
     print("stock uadate")


     
    def   saleproduct(self):
        qty=int(input("Enter Quantity of sale: "))
    
        if self.__stock>=qty:
           self.__stock-=qty
           print("product sold")
        else:
            print("no product")
#============================================================================

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


#============================================================================

# BANK ACCOUNT

class Bank:
    __bankbalance=0
    __count=0
    
    def openAccount(self):
        self.__acno=input("Enter Account Number:")
        self.__name=input("Enter name:")
        self.__balance=int(input("Enter balance:"))
        Bank.__bankbalance=+self.__balance
        Bank.__count+=1
        return self.__acno
    
    
    
    @classmethod
    def showBankbalance(cls):
        print("Total cutomer:",cls.__count)
        print("Total Bank balance:",cls.__bankbalance)
    
    '''
    @staticmethod
    def showBankbalance():  
         print("Total Bank balance:",Bank.__bankbalance)   
         '''
     
     
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
    print("5:show Bank balance" )
    print("6:Exit")   
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
              Bank.showBankbalance
        case 6:
             print('Good by')
        case __:
             print('wrong option')
    input("Press enter key to cont...")
    if(ch==6):
      break


#============================================================================
#default constractore


class student:

    def __init__(self):
        
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
s.getmarks()
s.showresult
   
#===========================================================================

#parameterized constractore


class student:
    def __init__(self,rollno,name):
        self.__rollno=rollno
        self.__name=name

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

s=student(100,'vivek')
s.getmarks()
s.showresult()

#========================================================================
#parameterized constractore


class student:
    def __init__(self,rollno,name):
        self.__rollno=rollno
        self.__name=name

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


data=[{'rollno':100,'Name':'peter'},{'rollno':200,'Name':'vivek'}]
L=[]
for s in data:
 roll=s['rollno']
 name=s['Name']
 print("Enter mark of ",name)
s=student(roll,name)
s.getmarks()
L.append(s)
for s in L:
   s.showresult()


#========================================================================
class twonum:
    def __init__(self,x=0,y=0):
        self.__x=x
        self.__y=y

    def getvalues(self):
        self.__x=int(input("Enter x:"))
        self.__y=int(input("Enter y:"))    

    def showvalues(self):
        print(self.__x,self.__y) 

T=twonum(10,20)
T.showvalues()


T1=twonum()
T1.getvalues()
T1.showvalues

#========================================================================
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
 
#========================================================================

class Alien:
    total=0
    def __init__(self,type,point):
        
            self.__point=point
            self.__type=self
            self.__point=type
            
    @classmethod
    def showpoint(cls):
        print("Total Points:",cls.total) 

    def __del__(self):
        Alien.total+=self.__point
        print("Alien",self.__type,"Destroyed")

A1=Alien('red',100)
input("end")



#========================================================================

# SINGLE INHERITANCE

class student:
    def getstudent(self):
        self.__name=input("Enter name:")
        self.__rollno=input("Enter roll number:")

    def putstudent(self):
        print(self.__name,self.__rollno)  


class Bsc(student):   
    def getBsc(self):
        self.getstudent()
        self.__p=input("Enter physics marks")
        self.__c=input("Enter chemistry marks")
        self.__m=input("Enter math marks")     

    def putBsc(self):
        self.putstudent()
        print(self.__p,self.__c,self.__m)    



s=Bsc()
s.getBsc()
s.putBsc()

#========================================================================
# HIERARCHI INHERITANCE

class student:
    def getstudent(self):
        self.__name=input("Enter name:")
        self.__rollno=input("Enter roll number:")

    def putstudent(self):
        print(self.__name,self.__rollno)  


class Bsc(student):   
    def getBsc(self):
        self.getstudent()
        self.__p=input("Enter physics marks")
        self.__c=input("Enter chemistry marks")
        self.__m=input("Enter math marks")     

    def putBsc(self):
        self.putstudent()
        print(self.__p,self.__c,self.__m)    



class Bcom(student):   
    def getBcom(self):
        self.getstudent()
        self.__E=input("Enter Economics marks")
        self.__BM=input("Enter BM marks")
        self.__A=input("Enter Account marks")     

    def putBcom(self):
        self.putstudent()
        print(self.__E,self.__BM,self.__A)    


S1=Bsc()
S1.getBsc()
S1.putBsc()

S2=Bcom()
S2.getBcom()
S2.putBcom()

#=================================================================================

# MULTI LEVEL INHERITANCE
class student:
    def getstudent(self):
        self.__name = input("Enter name: ")
        self.__rollno = input("Enter roll number: ")

    def putstudent(self):
        print(self.__name,self.__rollno)
        


class Bsc(student):
    def getBsc(self):
        self.getstudent()
        self.__p = int(input("Enter Physics marks: "))
        self.__c = int(input("Enter Chemistry marks: "))
        self.__m = int(input("Enter Math marks: "))

    def total(self):
        t = self.__p + self.__c + self.__m
        return t

    def putBsc(self):
        self.putstudent()
        print(self.__p,self.__c,self.__m)
      


class result(Bsc):
    def gettotal(self):
        self.getBsc()
        self.__total = self.total()

    def puttotal(self):
        self.putBsc()
        print("Total Marks:", self.__total)


s = result()
s.gettotal()
s.puttotal()


#===================================================================================

#-MULTIPLE INHERITANCE
#------------------------

# base class more than one 
class productionunitone:
    def getproductionone(self):
        self.P1=int(input("Enter producation one:"))
        def showproductionone(self):
         print("total production:",self.P1)    



class productionunittwo:
    def getproductiontwo(self):
        self.P2=int(input("Enter producation two:"))
    def showproductiontwo(self):
        print("total production:",self.P2)    


class Totalproducation(productionunitone,productionunittwo):
    def getTotal(self):
        self.getproductionone()
        self.getproductiontwo()
        self.__t=self.P1+self.P2

    def putTotal(self):
        self.showproductionone()
        self.showproductiontwo()
        print("Total:",self.__t)

T=Totalproducation()
T.getTotal()
T.putTotal()

#====================================================================================
#MULTIPLE INHERITANCE

class company:
    def getcompany(self):
        self.__c=input("Enter company:")

    def putcompany(self):
        print("company:",self.__c)  



class productionunitone(company):
    def getproductionone(self):
        self._P1=int(input("Enter producation one:"))
    def showproductionone(self):
        print("Total production:",self._P1)    



class productionunittwo(company):
    def getproductiontwo(self):
        self._P2=int(input("Enter producation two:"))
    def showproductiontwo(self):
        print("Total production:",self._P2)    


class Totalproducation(productionunitone,productionunittwo):
    def getTotal(self):
        self.getcompany()
        self.getproductionone()
        self.getproductiontwo()
        self.__t=self._P1+self._P2

    def putTotal(self):
        self.putcompany()
        self.showproductionone()
        self.showproductiontwo()
        print("Total:",self.__t)

T=Totalproducation()
T.getTotal()
T.putTotal()
#=================================================================================================
#overloding
class Base:
    def show(self):
        print("Base")
class derive(Base):
    def show(self):
        super().show()
        print("derive")


D=derive()
D.show()

#=================================================================================================


class employee:
    def __init__(self,id,name,salary):
        self.__id=id
        self.__name=name
        self._salary=salary
    def showemployee(self):
            print(self.__id,self.__name,self._salary)


class perks(employee):
    def __init__(self,id,name,salary,da,hra):
        super().__init__(id,name,salary)
        self.__da=da
        self.__hra=hra 
    def showperks(self):
         self.__netsalary=self._salary+self.__da+self.__hra
         self.showemployee()
         print(self.__da,self.__hra,self.__netsalary)

k=perks(1000,'vivek',20000,60000,2000)
k.showperks()


#=================================================================================================
#RUN TIME polymorphism
class animal:
    def sound(self):
     print("makes sound")
class dog(animal):
   def sound(self):
     print("dog breaks")
class cat(animal):
   def sound(self):
     print("cat mewww")
A=animal()
A.sound()
D=dog()
D.sound()
C=cat()
C.sound()

#=================================================================================================
#RUN TIME polymorphism

# method overwriting example
class animal:
    def sound(self):
     print("makes sound")
class dog(animal):
   def sound(self):
     print("dog breaks")
class cat(animal):
   def sound(self):
     print("cat mewww")

animal=[dog(),cat()]
animal[0].sound()
animal[1].sound()

#=================================================================================================

from abc import ABC,abstractmethod

class shapes(ABC):
    @abstractmethod
    def getshapes():
        pass
    def showArea():
        pass

class Rectangle(shapes):
    def getshapes(self):
        self.L=int(input("Enter L:"))
        self.B=int(input("Enter B:"))

    def showArea(self):
        A=self.L*self.B
        print("Rectangle:",A)



class sphere(shapes):
    def getshapes(self):
        self.R=int(input("Enter R:"))
        

    def showArea(self):
        A=4*3.14*self.R*self.R
        print("Sphere:",A)


shapes=[Rectangle(),sphere()]


for s in shapes:
    s.getshapes()

for s in shapes:
    s.showArea()

#=================================================================================================

#method overloding examplke 

def sum(a,b=20,c=10):
    return a+b+c

k=sum(20)
print(k)
k=sum (20,70,100)
print(k)
k=sum(890,222,73883)
print(k)


def sum(*x):
    return sum(x)
k=sum(10,20)
k=sum(1,2,3,4)

#=================================================================================================
# End class
#=================================================================================================

