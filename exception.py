"""exeception """
# try:
#     num1 = input("enter first value: ")
#     num2 = input("enter second value: ")
#     print(num1/num2)
# except Exception:
#     print("beta lg gye tumhare......")

# else:
#     print("no error occur")

# try:
#     num1 = int(input("enter first value: "))
#     num2 = int(input("enter second value: "))
#     print(num1/num2)
# except ZeroDivisionError:
#     print("beta zero se divide mt kro")
#     num1 = int(input("enter first value: "))
#     num2 = int(input("enter second value: "))
#     print(num1/num2)
# except Exception as e:
#     print("error tumhare......")

# else:
#     print("no error occur")
    

# while True:
#     try:
#         num1 = int(input("enter first value: "))
#         num2 = int(input("enter second value: "))
#         print(num1/num2)
#     except ZeroDivisionError:
#         print("beta zero se divide mt kro")
#     except Exception as e:
#         print("error tumhare......" , e)
#     else:
#         break

# while True:
#     try:
#         num1 = int(input("enter first value: "))
#         num2 = int(input("enter second value: "))
#         print(num1/num2)
#     except ZeroDivisionError:
#         print("beta zero se divide mt kro") 
#     except ValueError:
#         print("beta value se divide mt kro")       
#     except Exception as e:
#         print("error tumhare......" , e)
#     else:
#         break     
       

# count = 1
# while count >1:
#     try:
#         num1 = int(input("enter first value: "))
#         num2 = int(input("enter second value: "))
#         print(num1/num2)
#     except ZeroDivisionError:
#         count +1
#     except ValueError:
#         count +1   
#     except Exception as e:
#         count +1
#     else:
#         break     

# try:
#     a = "shekhar"
#     print(a+"9")
# except Exception as e:
#     print(e)

# """file handling"""
# try:
#     age = int(input("enter the age :"))
#     if age< 18:
#         print("age error occured")
#         raise 
#     else:
#         print("you are eligible for voting")

# except Exception as e:
#     print("error is -->>>",e)        

# try:
#     age = int(input("enter the age :"))
#     if age< 18:
#         print("age error occured")
#         raise Exception
#     else:
#         print("you are eligible for voting")

# except Exception as e:
#     e = "age error"
#     print("error is -->>>",e) 

try:
    age = int(input("enter the age :"))
    if age< 18:
        print("age error occured")
        raise ValueError ("error")
    else:
        print("you are eligible for voting")

except Exception as e:
    print("error is -->>>",e)                   