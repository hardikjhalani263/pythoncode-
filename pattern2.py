#assiment question 
# num = int(input("Enter the number:"))
# for i in range(0, num):
#     for j in range(1, i+1):
#         print(" ", end="")
#     for j in range(0, num):
#         print("*", end="")
#     print()
 
# question 1
# row = 5 
# for i in range (1 , row +1 ):
#     for j in range ( 1 , row +1):
#         if (j ==row or i == row or j== 1 or i== 1 ):
#             print ("*", end = "" )
#         else :
#             print ("" , end = " ")
#     print ()                

# question 2
#for i in range(1,5):
#   x = 65
#   for j in range(1,i+1):
#     print(chr(x),end="")
#     x+=1
#   print(" ")

#question 3
#x =65
# for i in range(1,5):
#   for j in range(1,i+1):
#     print(chr(x),end="")
#   x+=1
#   print(" ")

# question 4
# rows = 5
# for j in range(1, rows+1):
#     print("* " * j)
 
# question 5
# row = 6
# for i in range (1 , row ):
#     num =1
#     for j in range (row , 0,-1 ):
#         if j >i:
#             print (" " , end = ' ')
#         else :
#             print ( num , end = " ")
#             num +=1
#    print (" ")              

# question 6
# row = 6
# for i in range (row , 0, -1):
#     num = 65
#     for j in range (row , 0,-1 ):
#         if j >i:
#             print (" " , end = ' ')
#         else :
#             print ( chr(num)  , end = " ")
#             num +=1
#     print (" ")         
# 
# question 8 
# num = 5
# for i in range(num , 0 ,-1):
#     for j in range(0, i-1):
#         print(" ", end="  ")
#     for j in range(0, num):
#         print("*", end = " ")
#     print( ) 

# question 9 
# num = int(input("Enter the number:"))
# for i in range(num , 0 ,-1):
#     o=1
#     for j in range(0, i-1):
#         print(" ", end="  ")
#     for j in range(0, num):
#         print(o, end = " ") 
#         o+=1  
#     print( ) 

# question 10
# num = int(input("Enter the number:"))
# for i in range(num , 0 ,-1):
#     o=65
#     for j in range(0, i-1):
#         print(" ", end="  ")
#     for j in range(0, num):
#         print(chr(o), end = " ") 
#         o+=1  
#     print( )   

#question 11
# rows = 5
# for i in range(1, rows + 1):  
#     for j in range(rows  - i):  
#         print(" ", end=" ")
#     for k in range(1, 2 * i): 
#         print("*", end=" ")
#     print()

# question 12 
# rows = 5
# for i in range(1, rows + 1):  
#     for j in range(rows  - i):  
#         print(" ", end=" ")
#     for k in range(1, 2 * i):  
#         if k == 1 or k == 2 * i - 1 or i == rows:  
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")  
#     print()

# question 13
# rows = 5
# for i in range(rows , 0 ,-1):  
#     for j in range(rows  - i):  
#         print(" ", end=" ")
#     for k in range(1, 2 * i):  
#         if k == 1 or k == 2 * i - 1 or i == rows:  
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")  
#     print()

# question 14
# raw = 5
# for i in range (0 , raw):
#     for j in range (0 , i+1):
#         print("*", end = " ")
#     print ("")  
# for i in range ( raw +1 , 0 ,-1):
#         for k in range (0,i-1):
#             print("*", end = " ")
#         print ( )    

# question 15
# raw = 5
# for i in range (0 , raw):
#     for j in range (0 , i+1):
#         print("*", end = " ")
#     print ("")  
# for i in range ( raw +1 , 0 ,-1):
#         for k in range (0,i-1):
#             print("*", end = " ")
#         print ( )    

#question 16
# rows = int(input("Enter the row size for the pattern: "))
# for i in range(1,rows + 1): 
#     for j in range(rows  - i):
#         print(" ", end=" ")
#     for k in range(1, 2 * i):
#         print("*", end=" ")
#     print()
# for i in range(rows  - 1, 0, -1):  
#     for j in range(rows  - i):
#         print(" ", end=" ")
#     for k in range(1, 2 * i):
#         print("*", end=" ")
#     print()        

#question 17
# rows = int(input("Enter the row size for the pattern: "))
# for i in range(1,rows + 1):
#     o = 1 
#     for j in range(rows  - i):
#         print(" ", end=" ")
#     for k in range(1, 2 * i):
#         print(o, end=" ")
#         o+=1
#     print()
# for i in range(rows  - 1, 0, -1): 
#     o = 1 
#     for j in range(rows  - i):
#         print(" ", end=" ")
#     for k in range(1, 2 * i):
#         print(o, end=" ")
#         o+=1
#     print()        

#question 19

row = 5 


