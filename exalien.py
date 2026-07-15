
#1. Create two classes named Mammals and MarineAnimals. Create another class named BlueWhale which inherits both the above classes. Now, create a function in each of these classes which prints "I am mammal", "I am a marine animal" and "I belong to both the categories: Mammals as well as Marine Animals" respectively. Now, create an object for each of the above class and try calling
#1 - function of Mammals by the object of Mammal
#2 - function of MarineAnimal by the object of MarineAnimal
#3 - function of BlueWhale by the object of BlueWhale
#4 - function of each of its parent by the object of BlueWhale


# Multiple Inheritance.


class Mammals:
    def  getMammals(self):
        self.__m=input("I am a mammals:")
 
class Marine:
    def getMarine(self):
        self.__a=input("I am a marine animal:")

   
class BlueWhale(Mammals,Marine):
   def getBlueWhale(self):
        self.getMammals()
        self.getMarine()
        self.__q=input("I belong to both the categories: Mammals as well as Marine Animals")
    
   def showBlueWhale(self):
       print("i am a mammls:",self.__m)
       print("i am a marine animal:",self.__a)
       print("I belong to both the categories: Mammals as well as Marine Animals:",self.__q)

B=BlueWhale()
B.getBlueWhale()
B.showBlueWhale()



#===================================================================================================================
# Make a class named Fruit with a data member to calculate the number of fruits in a basket. Create two other class named Apples and Mangoes to calculate the number of apples and mangoes in the basket. Print the number of fruits of each type and the total number of fruits in the basket.
#multiple Inheritance

class fruit:
    def getfruit(self):
        self.__total=0
  
class apple(fruit):
    def getapple(self):
        self.apples=int(input("Enter number of apple:"))
    
class mangoes(fruit):
    def getmangoes(self):
        self.mangoes=int(input("Enter number of mangoes:"))
class total(apple,mangoes):

    def gettotal(self):
        self.getapple()
        self.getmangoes()
        self.getfruit()
        self.__total= self.apples+self.mangoes
        
    def showtotal(self):
        print("number of apples:",self.apples)
        print("namber of mangoes",self.mangoes)
        print("total fruit in the basket:",self.__total)


T=total()
T.gettotal()
T.showtotal()

#===================================================================================================================

#. We want to calculate the total marks of each student of a class in Physics,Chemistry and Mathematics and the average marks of the class. The number of students in the class are entered by the user. Create a class named Marks with data members for roll number, name and marks. Create three other classes inheriting the Marks class, namely Physics, Chemistry and Mathematics, which are used to define marks in individual subject of each student. Roll number of each student will be generated automatically.

class marks:
    def getmarks(self):
        self.__name=input("Enter name of student:")
        self.__rollno=input("Enter Roll number of student:")
        

    def showmarks(self):
        print(self.__name,self.__rollno)

class physics(marks):
    def getphysics(self):
        self.p=int(input("Enter physicas marks:"))

class chemistry(marks):
    def getchemistry(self):
        self.c=int(input("Enter chemistry marks:"))


class mathematics(marks):
    def getmathematics(self):
        self.m=int(input("Enter mathematics marks:"))

class totalmarks(physics,chemistry,mathematics):
    def gettotalmarks(self):
        self.getmarks()
        self.getphysics()
        self.getchemistry()
        self.getmathematics()
        self.__total= (self.p+self.c+self.m)
        self.__AVG= (self.p+self.c+self.m)//3
        
    def showtotalmarks(self):
        print("Total marks:",self.__total)
        print("average marks:",self.__AVG)
        
        

S=totalmarks()
S.gettotalmarks()
S.showtotalmarks()

#=====================================================================================================
#4. We want to store the information of different vehicles. Create a class named Vehicle with two data member named mileage and price. Create its two subclasses
#*Car with data members to store ownership cost, warranty (by years), seating capacity and fuel type (diesel or petrol).
#*Bike with data members to store the number of cylinders, number of gears, cooling type(air, liquid or oil), wheel type(alloys or spokes) and fuel tank size(in inches)
#Make another two subclasses Audi and Ford of Car, each having a data member to store the model type. Next, make two subclasses Bajaj and TVS, each having a data member to store the make-type. 
#Now, store and print the information of an Audi and a Ford car (i.e. model type, ownership cost, warranty, seating capacity, fuel type, mileage and price.) Do the same for a Bajaj and a TVS bike.

class Vehicle:
    def getVehicle(self):
        self.mileage=float(input(" mileage:"))
        self.price=float(input("price:"))

    def showVehicle(self):
        print(" mileage:",self.mileage)
        print("price:",self.price)

class car(Vehicle):
    def getcar(self):
        self.ownershipcost=input("car ownership:")
        self.warranty =input("Enter car warranty:")
        self.seatingcapacity =input("car seating capacity:")
        self.__fule=input("car fuel type (diesel or petrol):")
    def showVcar(self):
        print("car ownership:",self.ownershipcost)
        print("car warranty:",self.warranty) 
        print("car seating capacity:",self.seatingcapacity)
        print("car fuel type (diesel or petrol):",self.__fule)

class bike(Vehicle):
    def getbike(self):
        self.cylinders=input("number of cylinders:")
        self.gears=input("number of gears:")
        self.coolingtype=input("cooling type(air, liquid or oil:")
        self.wheeltype=input("wheel type(alloys or spokes:")
        self.fueltanksize=input("fuel tank size(in inches:")       

    def showbike(self):
              
        print("number of cylinders:",self.cylinders)
        print("number of gears:",self.gears) 
        print("cooling type(air, liquid or oil:",self.coolingtype)
        print("wheel type(alloys or spokes:",self.wheeltype)
        print("fuel tank size(in inches:",self.fueltanksize)
class Audi(car):
    def getAudi(self):
        self.getVehicle()
        self.getcar()
        self.model1=input("Enter Audi model:")
    def showAudi(self):
        self.showVehicle()
        self.showVcar()
        print("model:",self.model1)


class ford(car):
    def getford(self):
        self.getVehicle()
        self.getcar()
        self.__model2=("Enter ford model:")
    def showford(self):
        self.showVehicle()
        self.showVcar()
        print("model:",self.__model2)


class Bajaj(bike):
    def getBajaj(self):
        self.getVehicle()
        self.getbike()
        self.type1=("Enter make-type:")
    def showBajaj(self):
        self.showVehicle()
        self.getbike()
        print("type:",self.type1)
class TVS(bike):
    def getTVS(self):
        self.getVehicle()
        self.getbike()
        self.type2=("Enter make-type:") 
    def showTVS(self):
         self.showVehicle()
         self.getbike()
         print("type:",self.type2)

A=Audi()
A.getAudi()
A.showAudi()

F=ford()
F.getford()
F.showford()

B=Bajaj()
B.getBajaj()
B.showBajaj()


T=TVS()
T.getTVS()
T.showTVS()
#=====================================================================================================
#5. Create a class named Shape with a function that prints "This is a shape". Create another class named Polygon inheriting the Shape class with the same function that prints "Polygon is a shape". Create two other classes named Rectangle and Triangle having the same function which prints "Rectangle is a polygon" and "Triangle is a polygon" respectively. Again, make another class named Square having the same function which prints "Square is a rectangle". 
#Now, try calling the function by the object of each of these classes.


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

#=====================================================================================================
#6. All the banks operating in India are controlled by RBI. RBI has set a well-defined guideline (e.g. minimum interest rate, minimum balance allowed, maximum withdrawal limit etc) which all banks must follow. For example, suppose RBI has set minimum interest rate applicable to a saving bank account to be 4% annually; however, banks are free to use 4% interest rate or to set any rates above it.
#Write a program to implement bank functionality in the above scenario. Note: Create few classes namely Customer, Account, RBI (Base Class) and few derived classes (SBI, ICICI, PNB etc). Assume and implement required member variables and functions in each class.

class Customer:
    def getCustomer(self):
        self.name=input("Enter customer Name:")
        self.acc_no=input("Enter Account number:")

    def showCustomer(self):
        print("customer Name:",self.name)
        print("Account number:",self.acc_no)



class Account(Customer):
    def getAccount(self):
        self.balance=float(input("Enter Balance:"))

    def showAccount(self):
        print("Balance:",self.balance)

class RBI(Account):
    def RBI_Rules(self):
        self.min_interest = 5
        self.min_balance = 1000
        self.max_withdraw = 500000

    def showRules(self):
        print("minimum interest:",self.min_interest)
        print("minimum balance :",self.min_balance)
        print("maximum withdraw:",self.max_withdraw)


class SBI(RBI):
    def getSBI(self):
        self.getCustomer()
        self.getAccount()
        self.RBI_Rules()
        self.interest=7

    def showSBI(self):
        self.showCustomer()
        self.showAccount()
        self.showRules()
        print("SBI Interest Rate:", self.interest)

class ICICI(RBI):
    def getICICI(self):
        self.getCustomer()
        self.getAccount()
        self.RBI_Rules()
        self.interest=10

    def showICICI(self):
        self.showCustomer()
        self.showAccount()
        self.showRules()
        print("ICICI Interest Rate:", self.interest)




S=SBI()
S.getSBI()
S.showSBI()
I=ICICI()
I.getICICI()
I.showICICI()

#=====================================================================================================
#End all assignments
#=====================================================================================================