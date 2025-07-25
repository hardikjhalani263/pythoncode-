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

# try:
#     age = int(input("enter the age :"))
#     if age< 18:
#         print("age error occured")
#         raise ValueError ("error")
#     else:
#         print("you are eligible for voting")

# except Exception as e:
#     print("error is -->>>",e)

# def atm_simulation():
#     try:
#         balance =10000

#         while True:
#             print("""
#             welcome to my ATM
#             press 1 for exit
#             press 2 for deposit
#             press 3 for withdrow      """)
#             decision=int(input("enter 1/2/3 :  "))
#             if decision==1:
#                 print(" Thanks For Using my ATM")
#                 break
#             elif decision==2:
#                 deposit_amount=int(input("enter the amount to deposit :  "))
#                 balance+=deposit_amount
#                 print("your balanceis ",balance)
#             elif decision==3:
#                 w_amount=int(input("enter the amount to withdrow : "))
#                 if balance>=w_amount:
#                     balance-=w_amount
#                 else:
#                     raise ValueError("transaction fail due to insufficent balance")
#                 print("remaining balance",balance)
#             else:
#                 print("invalid input")
#     except Exception as e:
#         print("error",e)
# atm_simulation()          

    
# """file handeling"""  
# # file = open("file_name.extension(txt)','mode")
# '''
# r = read
# w = write
# a = append

# + - read and write
# '''

# file = open("regex.txt","r")
# con = file.read()
# print(con)
# file.close()


# file = open ("regex.txt",'a')
# file.write("\n this is append new ")
# file.close()

# file = open ("regex2.txt", 'a')
# file.write("i am inside regex2 file")
# file.close()

# with open("regex.txt",'r') as file:
#     file.write("line 1")
#     file.write("\nline2")

# with open("regex.txt","r") as source,open("regex2.txt","a") as destination:
#     for line in source:
#         destination.write('\n'+line) 

# with open("regex.txt","r") as source,open("regex2.txt","a") as destination:
#     context1 = source.read()
#     context2 = destination.read()
#     print(context1)
#     print(context2)

# with open("regex.txt","r") as file:
#     for line in file :
#         print (line)

# with open("regex.txt","r") as file:
#     count = 0
#     for line in file :
#         count+=len(line.split())
#     print(count)   

with open ("regex.txt" , 'r') as file:
    context=file.read()
    print(context)
    

with open ("regex.txt" ,'r+') as file:
    file.write("line1")
    file.write("\n line 2")   
    file.write("\n line 3")   
    file.write("\n line 4")  
    # file.write("/n line 2")    
    file.seek(2)
    print(file.read())