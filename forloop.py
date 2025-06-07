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
n = int(input("enter a no."))
last = n %10 
while(n>0):
    first = n %10
    n =n // 10 
print (f"first last = {first , last}")


# question 9 
n = int(input("enter a no."))
last = n %10 
q = 0
while(n>0):
    first = n %10
    n =n // 10
q = first + last 
print (f"first last = {q}")

#question 10
n = int(input("Enter a number to reverse: "))
num = 0
for i in n:
    i = n % 10
    num = num * 10 + int(i)
    n = n//10
print(f"The reversed number is: {num}")

#question 11
base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent (non-negative): "))
result = 1
for _ in range(exponent):
    result *= base
print(f"{base}^{exponent} = {result}")


#question 12 
num = int (input("enter a positive no."))
for i in range (1,num +1):
    if (num % i == 0):
        print (f"the factor of no are " , i  )

#question 13 
num = int(input("Enter a non-negative integer: "))
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *i
    print(f"The factorial of {num} is: {factorial}")

#question 14 
x = int(input("Enter the first number: "))
y= int(input("Enter the second number: "))
for i in range(1, min(x, y) + 1):
    if x % i == 0 and y % i == 0:
            print(i)

# question 15 
n = int (input ("enter a no ."))
if n >1 :
    for i in range (2 , n ):
        if (n%i ==0 ):
            print (n , "is not a prime no .")
            break 
        else :
            print ("it is aprime no.")

# question 16   



# question 17