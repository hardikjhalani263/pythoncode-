# total = 0
# count = 0
# for i in range( 1 , 30 ):
#    # total = total+i
#     count+=1
#     print( total , count )




# n = int(input("Enter a positive integer (n): "))

# # Check if the input is a natural number
# if n >= 1:
#     print("Natural numbers from", n, "to 1 are:")
#     for i in range(n, 0, -1):  # Start at n, stop before 0, step -1
#         print(i)
# else:
#     print("Please enter a positive integer greater than 0.")

# number = 45678
# number_str = str(number)
# count = 0

# for digit in number_str:
#     count +=int (digit)

# print(count)

# number = 12345
# def first_and_last_digit(number):
#     number_str = str(number)
    
#     for i in range(len(number_str)):
        
#         if i == 0:
#             first_digit = number_str[i]
#         if i == len(number_str) - 1:
#             last_digit = number_str[i]
        
#     return first_digit+ last_digit


# first_digit, last_digit = first_and_last_digit(number)
# print("First digit:", first_digit)
# print("Last digit:", last_digit)




# n = int(input("Enter a number to reverse: "))
# num = 0
# num_str = str(n)

# for i in num_str:
#     i = n % 10
#     num = num * 10 + int(i)
#     n = n//10
# print(f"The reversed number is: {num}")


# i = 20 
# while(i<=40):
#     if (i % 3 == 0):
#         print(i)
#     i=i+1    



# i = 98
# count = 0
# while(i>= 58):
#     count+=1
#     i =i-1
# print(count)


# num = 145
# while(num>0):
#   n = num%10
#   num1 = num//10
# print(n , num1)

# 
# num = 123
# total=0
# while(num >0):
#     rem=num%10
#     num = num //10
#     total= total + rem**3
#     print(rem, rem**3)
# print("total" ,num , total , rem) 


# num = 1234
# temp = num 
# total= 0 
# while (num >0 ):
#     rem = num %10
#     num =num //10
#     total+=rem**3

# n = int(input("enter a number "))
# count = 0
# temp = 0
# while(n>0):
#     rem =num%10
#     num = num //10
#     total= total + rem ** count 
#     print(rem , rem **count)
# print ("total", num , total , rem)    

    
# def print_factors(x, y):
#     print("The common factors of", x, "and", y, "are:")
#     for i in range(1, min(x, y) + 1):
#         if x % i == 0 and y % i == 0:
#             print(i)

# num = int(input("Enter the first number: "))
# num1 = int(input("Enter the second number: "))
# print_factors(num, num1)

# n = int (input("enter a no."))
# if n>1 :
#   for num in range (n , n+1):
#    for i in range(2, num  +1):
#     if(n%i == 0):
#         print(n, "is not prime no.")
#         break
#     else: 
#         print(n,"is a prime no.")    
#     print (n)        

# s = "HARDIK" 
# i =0 
# a = 0
# end = len(s)-1
# while(i<end):

#     if (s[i] != s[end]):
#         a=1
#         break
#     i =+1 
#     end -=1
#     # print(s[i] , s[end] , i , end )

#     # i =+1 
#     # end -=1
# if (a==1):
#       print("it is not a palimdrome",s)
# else :
#     print(" a palindrome" , s)

city = "JAIPUR"
city[0:3]




