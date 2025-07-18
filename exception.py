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

while True:
    try:
        num1 = int(input("enter first value: "))
        num2 = int(input("enter second value: "))
        print(num1/num2)
    except ZeroDivisionError:
        print("beta zero se divide mt kro") 
    except ValueError:
        print("error")       
    except Exception as e:
        print("error tumhare......" , e)
    else:
        break     
       