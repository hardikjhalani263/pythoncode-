# question 1 
i = int (input ("enter a valied no."))
for n in range (1 , i+1 ) :
    if i<=0 :
        print ("it is a positive no. ")
        break 
    else :
        print (" it is not a positive no . ")
print (n ) 

#question 2 
n = int (input ("enter a positive intiger "))
for i in range (n , 0 , -1 ):
    if (n>=1 ):
        print ("natural no. from n to 1 are ")
    else :
        print ("enter a positive intiger greater than 0 ")

# question 3 
char = 'a '
while char <='z':
    print (char , end = " ")
    char = char

# question 4 
for i in range (2 , 101):
    if (n % 2 ==0 ):
        print ("it is a even no . ")
        print (i )

# question 5 
n = int (input ("enter a positive intiger "))
sum = 0 
for i in range (1 , n+1):
    if (n %2 != 0 ) :
        print ("it is odd no. ")
        sum +=i
print ("sum of odd no. is 1 to" , n , sum )

# question 6 
n = 45678
count = 0 
for i in range (n ):
    count +1 
print (count)     

# question 7 
n = int (input("enter a valied no. "))
count = 0 
for i in range (n ):
    count +int (i )
print (count ) 

#question 8 
number = 12345
def first_and_last_digit(number):
    number_str = str(number)
    
    for i in range(len(number_str)):
        
        if i == 0:
            first_digit = number_str[i]
        if i == len(number_str) - 1:
            last_digit = number_str[i]
        
    return first_digit+ last_digit
first_digit, last_digit = first_and_last_digit(number)
print("First digit:", first_digit)
print("Last digit:", last_digit)

# question 9 
num = int(input ("enter a no. "))
res = num % 10
while num > 9:
    num = num // 10
res += num
print('Addition of first and last digit of number is', res)

#question 10
n = int(input("Enter a number to reverse: "))
num = 0

for i in n:
    i = n % 10
    num = num * 10 + int(i)
    n = n//10
print(f"The reversed number is: {num}")

#question 11
a = float (input("enter a no . "))
b = int(input("enter a no. "))
def power(a, b):
    result =1 
    for i in range (b ):
        result =a 
        print (result)
    result = power(a, b )
print (a )

#question 12 
def print_factors(x, y):
    print("The common factors of", x,  "are:")
    for i in range(1, x+ 1):
        if x % i == 0 :
            print(i)

num = int(input("Enter the first number: "))
print_factors(num, )    

#question 13 



#question 14 
def print_factors(x, y):
    print("The common factors of", x, "and", y, "are:")
    for i in range(1, min(x, y) + 1):
        if x % i == 0 and y % i == 0:
            print(i)

num = int(input("Enter the first number: "))
num1 = int(input("Enter the second number: "))
print_factors(num, num1)

# question 15 
n = int (input ("enter a no ."))
if n >1 :
    for i in range (2 , n ):
        if (n%i ==0 ):
            print (n , "is not a prime no .")
            break 