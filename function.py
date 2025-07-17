'''
def function_name ():
     FUNCTION BODY
_
_
-
'''

# def display():
#     print("hi")
#     print("herllo")
#     print("bey")

# display()

# a=10
# b=90
# sum=a+b

# display()

# def add():
#     a=10
#     b=90
#     sum=a+b
#     print(sum)
# add()    

# def add():
#     a=int(input("enter a no"))
#     b=int(input("enter a no"))
#     sum=a+b
#     print('addition of no',sum)
# add()    

# def f1(a,b):
#     print(a+b)

# f1(10,45)
# f1(90,10)


# def f1(a,b):
#     print(a+b)
#     return "hello"

# print(f1(10,45))
# f1(10,90)


# """
# user define function
# parameter   return
#    yes       yes
#    no        yes
#    yes       no
#    no        no
   
# """

# def sum():
#     a= 10
#     b = 20
#     sum = a+b
#     return sum
# sum() 

# def f1(a,b):
#     print(a+b)
#     return "hello"

# print(f1(10,45))
# f1(10,90)

# def add(a, b):
#     result = a + b
#     return result

# sum = add(5, 3)
# print("Sum:", sum)

# def f1(a = 10,b = 5, c = 0):
#     return a,b,c
# print(f1(10,90,))


# """"lamda function """
# multiply = lambda a,b : a*b
# print(multiply (10,6))

# def f1():
#     return "hello from f1"
# def f2(n):
#     print(n)
#     return f1()

# print(f2(90))

# def print_numbers(n):
#     if n > 10:                                            ex of recirsion function 
#         return
#     print(n)
#     print_numbers(n + 1)
# print_numbers(1)


# def factorial(n):
#     if n==1:
#         return 1
#     return n*factorial(n-1)

# print(factorial(5))

# def f1(n):
#     count = 0
#     if n ==5:
#         return 0
#     while n>0:
#         print(n)
#         count+=1
#         if count ==2:
#             break
#         n-=1

#     return f1(n+3)
# f1(3)    

# def febbo(n):
#     a = 0
#     b = 1
#     for i in range(n):
#         next = a+b
#         a = b
#         b = next
#         print(b , end = " ")   

# febbo(10) 

"""nested function"""
# def outer():
#     def inner():
#         return 10
#     return inner()

# print(outer())

"""highi oerder function"""
# def operation(a,b,op):
#     return op(a,b)
# def add (a,b):
#     return a+b
# def sub (a,b):
#     return a-b

# print(operation(90,10,sub))

"""map function"""
# data =[1,2,3,4,5]

# def square(n):
#     return n*n
# new = list(map(square,data))
# print(new)

# data = list(map(int, input("Enter : ").split()))
# print(data)

"""filter function"""
# data =[12,13,57,4,3,56]
# def filter_num(n):
#     return n%2==0
# new=list(filter(filter_num,data))
# print(new)

"""variable argument function"""
# # print(1,2,3,4,5,6,)
# def display(*args):
#     print(args)
#     print(type(args))

# display(9,2,34,45,6,7,34)    
# def display(*add):
#     sum =0
#     for i in add:
#         sum+=i
#     return sum
# print(add(1,2,3,4,56,11,22,33))    

# def display(*even):
#     sum = 0
#     for i in even:
#         if i%2 ==0:
#             sum +=i 
#     return sum           

# even= int(input("enter a:"))

"""keywards argument function """
# def f1 (**kwargs):
#     print(kwargs)
#     print(type(kwargs))
# f1(a =10,b = 90 , c =89)

# def f1(**kwargs):
#     kwargs['a']=123
#     return kwargs
# print (f1(a = 10,b=90,c=89))

# n = int (input ("enter a no ."))
# if n >1 :
#     for i in range (2 , n ):
#         if (n%i ==0 ):
#             print (n , "is not a prime no .")
#             break 
#         else :
#             print ("it is aprime no.")

# n = 4867
# while n>=10:
#   add = 0
#   while n > 0:
#     add += n%10
#     n //= 10
#   n = add
# print(n)


n = 4867
d = 0
while n >= 10:
    n = sum(int(d) for d in str(n))

print(n)

