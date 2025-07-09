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

def f1(n):
    count = 0
    if n ==5:
        return 0
    while n>0:
        print(n)
        count+=1
        if count ==2:
            break
        n-=1

    return f1(n+3)
f1(3)    

def febbo(n):
    a = 0
    b = 1
    for i in range(n):
        next = a+b
        a = b
        b = next
        print(b , end = " ")   

febbo(10) 

