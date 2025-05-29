# q .1 answer
# number = int(input("Enter an integer: "))
# if number % 2 == 0:
#   print("Even")
# else:
#   print("Odd")


# q . 2 answer
# i = int(input ("enter a intiger"))
# if i>0:
#   print("positive")
# elif i<0:
#   print("negative")
# else : 
#   print ("zero") 


# #q . 3 answer
# i = int(input("enter a no."))
# j = int(input("enter a no."))
# k = int(input("enter a no."))
# if (i>=j) and (i>=k):
#   larger = i
# elif (j>=k) and (j>=i):
#   larger = j 
# else: 
#    larger = k


# q . 4 answer
# year = int(input("enter a year"))
#if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         print("Leap Year")
# else:
#         print("Not a Leap Year")


 # q . 5 answer
# i = int(input("enter a value"))
# if (i % 3 == 0 and i % 5 == 0 ):
#     print("it is divisible by 3 and 5 ")
# else:
#     print("it is not divisible by them")


# q . 6 answer
# x = (input("enter a alphavate"))
# if (x == 'a' or x == 'e' or
#         x == 'i' or x == 'o' or x == 'u'):
#     print("it is a vowel")
# else:
#     print("it is a consonent")    


# q . 7
# marks = int(input("Enter marks (out of 100): "))
# if marks >= 90:
#   print("Grade A")
# elif marks >= 80:
#   print("Grade B")
# elif marks >= 70:
#   print("Grade C")
# elif marks >= 60:
#   print("Grade D")
# else:
#   print("Fail")


# q . 8 answer
# i = int(input("enter your age "))
# if (i>= 18):
#     print("he can give a vote")
# else:
#     print("not eligibal for vote")    


# #q .10 answer
# i = int(input("enter a no."))
# k = int(input("enter a no."))
# while (i<=k):
# # if (i%2 == 0):
#   print(i)
#   i= i+2


# q. 11 answer
# N = int(input("Enter an integer: "))
# sum = (N * (N + 1)) / 2
# print("The sum of integers from 1 to", N, "is", sum)


# q . 12 answer
# n = int(input("Enter a number for the multiplication table: "))
# i = 1
# while i <= 10:
#     print(f"{n} x {i} = {n * i}")
#     i += 1


# Q.13 answer
# n = int(input("Enter a number to reverse: "))
# num = 0
# while n > 0:
#     digit = n % 10
#     num = num * 10 + digit
#     n = n // 10
# print(f"The reversed number is: {num}")


# Q.14 answer
# num = int(input("Enter a number to count digits: "))
# count = 0
# if num == 0:
#     count = 1
# else:
#     num = abs(num)
#     while num > 0:
#         num //= 10
#         count += 1
# print(f"The number of digits is: {count}")

# q. 15

def print_factors(x , y):
   print("The factors of",x,y ,"are:")
   for i in range( x , y + 1):
       if x % i == 0:
        if y % i == 0:    
          print(i)

num = int(input("enter a no."))
num1 = int(input("enter a no."))
print_factors(num , num1)

def age_group(age):
    """
    This function takes an age as input and returns the corresponding age group.
    """
    if age <= 0:
        return "Invalid Age"
    elif age <= 1:
        return "Infant"
    elif age <= 4:
        return "Toddler"
    elif age <= 12:
        return "Child"
    elif age <= 19:
        return "Teenager"
    elif age <= 59:
        return "Adult"
    else:
        return "Senior"

# Example usage
age = int(input("Enter your age: "))
print(age_group(age))


