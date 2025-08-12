# class car:
#     color = "red"
#     model = "2023"
#     start1 = "self"
#     def start (self):
#         print("broooommmm")
#     def start (self):
#         print("stoped")

# scorpio = car()
# print(scorpio.color)
# scorpio.start()



# class car:
#     color ="black"
#     model ="2025"

#     def start(self):
#         print("petrol")
#     def stop (self):
#         print("desel")

# car.color='red'
# bmw= car()
# print(bmw.color)

# class c1:
#     data = "new data"
#     def m1(self ,a ,b):
#         self.a = a
#         self.b = b
#         print(self,a*self,b)
#     def distory_data(self):
#         del c1.data 

# obj =c1()      

# class c1:
#     data = "new data"
    
#     def __init__(self, a=0, b=0):  
#         self.a = a
#         self.b = b

#     def m1(self, a, b):
#         self.a = a
#         self.b = b

#     def mul(self):
#         print(self.a * self.b)

#     def distory_data(self):
#         del self.a
#         del self.b

# obj = c1()      
# obj.mul()       
# obj.m1(5, 3)    
# obj.mul()       


# class bank:
#     def __init__(self, account_number, name, balance=0):
#         self.account_number = account_number
#         self.name = name
#         self.balance = balance

#     def deposit(self,amount):
#         if amount >0 :
#             self.balance += amount
#             print(f'{amount} deposit successfully!')    
#         else:
#             print("deposit amount must be greater than 0.")

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient balance!")
#         elif amount <= 0:
#             print("Withdrawal amount must be greater than 0.")
#         else:
#             self.balance -= amount
#             print(f"₹{amount} withdrawn successfully!")        
    
#     def check_balance(self):
#         print(f"Account Holder: {self.name}")
#         print(f"Account Number: {self.account_number}")
#         print(f"Available Balance: ₹{self.balance}")


# amount1 = bank("123456","hardik",5000)  
# amount2 = bank("789012","hemant",6000) 

# amount1.check_balance()
# amount1.deposit(2000)
# amount1.withdraw(3000)
# amount1.check_balance()


# class parents:
#     vhicle = 'BMW'
#     account_balance = 5000000
#     def doing_job(self):
#         print("working in office")

# class child(parents):
#     vrhicle = 'bycycle'
#     def playing(self):
#         print("playing cricket")
#     def styding(self):
#         print("preparing for exam")
# class superchild(child):
#     def gym(self):
#         print("i am go gym 7:00")
#     def gpay(self):
#         print("i give gpay to my friend")


# obj = superchild()   
# obj.gym()   

# class c1:
#     data=900
#     def __init__(self):
#         print("i am from c1")

# class c2(c1):
#     data=800
#     def __init__(self):
#          print("i am from c2")

# class c3(c2):
#     data=700
#     data=c1.data
#     def __init__(self):
#         print("i am from c3")
#         # c1.__init__(self)
#         super().__init__()

# obj=c3()

# class c1:
#     data = "i am from c1"
#     def m1(self,a,b):
#         self.a = a
#         self.b = b
#         print(self.a+self.b)

#     def _init_(self):
#         print("this is conster")

# class c2:
#     print("the")

# class c3(c2,c1):
#     values=[123,34,45]
#     def _init_(self,a,b):
#         print("in the conster3 ")
#         c1. _inite_(self,a,b)

# obj=c3(int(input("n1")),(input)("n2"))
# obj._init_()

# class c1:
#     data1 = 10

# class c2(c1):
#     data2 = 90

# class c3(c1):
#     data3 = 100

# obj = c2()
# print(obj.data1)

""""encapsulation"""
# class c1:
#     _data = "here we are having passward"
# obj = c1()
# print(obj._data)    

# class c1:
#     __data = "here we are having passward"
#     def display_data(self):
#         return c1.__data(self):
# obj = c1()
# print(obj.display_data())    


# class c1:
#     def m1(self,a):
#         self.__a=a
#     def getter(self):
#         print(self.__a)

#     def setter (self,a):
#         self.__a=a        
# obj =c1()
# obj.m1(10)
# obj.getter()
# obj.setter(90)
# obj.getter()        


"""polymorphism"""

# class animal:
#     def make_sound(self):
#         print("some generic sound")

# class dog:
#     def make_sound(self):
#         print("booooooofffff")

# class cat:
#     def make_sound(self):
#         print("mmeeeeeeeooooooo")

# def call(obj):
#      obj.make_sound()

# a = animal()
# b = dog()
# c = cat()

# call (a)
# call (b)

"""method overloading"""

class c1:
    # def operation(self,a):
    #     print(a)
    # def operation(self,a,b):
    #     print(a+b)

    # def operation(self,a,b,c):
    #     print(a*b*c)
    def operations(self,a,b=0,c= 0):
        if b == 0 and c == 0:
            print (a)
        elif c ==0:
            print (a+b)
        else:
            print (a*b*c)

obj = c1()
obj .operations(10,10,10)                


