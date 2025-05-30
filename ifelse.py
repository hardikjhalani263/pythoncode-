#question 1
num = int(input ("enter an intiger "))
if num %2 == 0:
    print("even ")
else :
    print ("odd")

#question 2 
i = int(input("enter a no. "))
k = int(input("enter a no. "))       
j = int(input("enter a no. "))
if (i >= j ) and (i >=k):
    large = i 
elif (j>=k ) and (j >= i ):
    large = j 
else :
    large = k 

#question 3 
n = int(input("enter a year "))
if (n%4 ==0 and n %100 != 0 ) or (n % 400 ==0 ):
    print ("leap year ")
else :
    print (" not a leap year ")

#question 4 
marks = int(input("Enter marks (out of 100): "))
if marks >= 90:
  print("Grade A")
elif marks >= 80:
  print("Grade B")
elif marks >= 70:
  print("Grade C")
elif marks >= 60:
  print("Grade D")
else:
  print("Fail")

#question 5 
x = (input("enter a alphavate"))
if (x == 'a' or x == 'e' or
        x == 'i' or x == 'o' or x == 'u'):
    print("it is a vowel")
else:
    print("it is a consonent")   

#question 6 
i = int (input ("enter a no."))
k = int (input ("enter a no."))
if '+':
   print (i+k )
elif '-':
   print (i-k)
elif '*':
   print (i*k)
elif '/':
   print (i/k)
if k ==0 :
   print (" no. is divide by them ")
else:
   print ("in valied no ")       

# question 7
i = int(input ("enter a intiger"))
if i>0:
  print("positive")
elif i<0:
  print("negative")
else : 
  print ("zero") 

# question 8
username = (input ("enter a name "))
passward = int(input("enter a passward "))
if username=="admin" and passward == "1234" :
  print ("it is correct login successfull ! ") 
else:
   print ("not correct useer and login failed")

#question 9
side1 = int(input("enter a legth no. "))
side2 = int(input("enter a legth no. "))
side3 = int(input("enter a legth no. "))
def it_triangle (side1 , side2 , side3 ) :
 if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1 :
   print ("true")
 else :
   print ("fale ")

 if it_triangle (side1 , side2 , side3 ) :
   print ("this side can fome a triangle ")
 else:
   print ("this side can not be form a valied triangle ")

#question 11 
p = input ("enter a price ")
if p >1000:
   print ("your discount is 10% ", p*0.1 )
elif 500 < p < 1000 :
   print ("your discount is 5%" , p* 0.05)
else :
    p < 500 
    print ("your discount is 0% " , p *0)
print ("the final price of the applying the discount " , p )  

#question 12
month_name = input("Enter the name of the month: ")
year_input = int(input("Enter the year: "))
days = (month_name, year_input)
print(f"Number of days in {month_name}: {days}")
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
def days_in_month(month, year):
    if ("january", "march", "may", "july", "august", "october", "december"):
        return 31
    elif ("april", "june", "september", "november"):
        return 30
    elif  "february":
        if is_leap_year(year):
            return 29
        else:
            return 28
    else:
        return
if __name__ == "__main__":
   
#question 14
    age = int(input("Enter your age: "))
if age <=0 :
   print ("enter a valied age ")
elif age <= 1 :
   print ("ifant ")   
elif age <= 4 :
   print ("toddler")
elif age <= 12 :
   print ("child")
elif age <= 19:
   print ("teenage ")
elif age <= 59 :
   print ("adult ")
else :
   print (" senior ")

   print (age)           

#question 15
def print_day(day_number):
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    if 1 <= day_number <= 7:
        print(days[day_number])
    else:
        print("Invalid input. Please enter a number between 1 and 7.")

day = int(input("Enter a number (1-7): "))
print_day(day)
