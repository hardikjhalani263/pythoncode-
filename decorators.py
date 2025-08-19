"""how to creat yhe decorators"""
# def mydecorators (func):
#     def wrapper():
#         print("befor function run")
#         func()
#         print("after function run")
#     return wrapper
# @mydecorators
# def say_hello():
#     print("hello")

# say_hello        


""""abstractmethod"""
# from abc import abstractmethod , ABC
# class shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class triangle(shape):
#     def area(self,a,b,c):
#         self.a= a
#         self.b = b
#         self.c = c
#         print(self.a*self.b*self.c)

# class rectangular(shape):
#     def area(self,a,b):
#         self.a=a
#         self.b=b
#         print(self.a*self.b)
# obj = triangle()
# obj.area(90,20,10)        


"""starticemethod"""
# class c1:
#     data =90
#     @staticmethod
#     def m1():
#         a=90
#         b=10
#         print(a+b)
#         c1.data=89
#         print(c1.data)
#         print("i am m1 from staticemethod")

# obj=c1()
# obj.m1()

"""classmethod"""
'''class method is a method which is bounded to the class rather then its instance'''
# class c1:
#     data =90
#     @classmethod
#     def m1(cls):
#         cls.data ="data new"
#         cls.a =100
#         print (cls.data)
# obj=c1()
# obj.m1()
# print(c1.a)


"""generator"""

'''it is a 'less Memory Efficiency': and 'lazy evaluation' and 'simple functon' and 'use return' and infinite data set . '''
# def gen():
#     yield 1
#     yield 2
#     yield 3
# data = gen()
# print(next(data))
# print(next(data)) 
# print(next(data))

