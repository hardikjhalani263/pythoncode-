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

def print_numbers(n):
    if n > 10:
        return
    print(n)
    print_numbers(n + 1)
print_numbers(1)
