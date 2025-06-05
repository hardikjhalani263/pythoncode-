age = 10
print ("memory of age=> " , id (age))
x = age 
print ("memory of x =>", id (x))
x =20
print ("new memory of x =>", id (x) , id(age))

mylist =[10,20, "abc"]
print (type (mylist))
print (mylist [0])

print (mylist)
mylist.append(100)  # add no.
print (mylist)

print (mylist)
mylist.insert(2,"69") # add the no.
print (mylist )

print (mylist)
mylist [0]=1888   # update => index => value 
print (mylist)
mylist.pop()
print ("delet =>" , mylist )

list1 = [ 10,20,30, 40, 3,2,1]
for e in list1:         # execute loop directiy => iterable
    print(e, list1)   

list1 = [ 10,20,30, 40, 3,2,1]
for index in range ( 0, len(list1)):         # execute loop directiy => iterable
    print(index , list1[index])      

list1 = [ 10,20,30, 40, 3,2,1]
for index in range ( 0, len(list1)):       # execute loop directiy => iterable
    if (list1[index] > 20):
     print(index , list1[index])      

list2 =[ ]
list1 = [ 10,20,30, 40, 3,2,1]
for index in range ( 0, len(list1)):       
 if (list1[index]%2 != 0 ) :
    list2.append(list1[index])
    print(index , list1[index])     
print (list2)   

list2 =[ ]
list1 = [ 10,20,30, 40, 3,2,70]
for index in range ( 0, len(list1)):       
 if (list1[index]%2 != 0 ) :
    list2.append(list1[index])
    print(index , list1[index])     
print (list2)   

list2 = []
list1 = [10, 20, 30, 40, 3, 2, 70]

for index in range(0, len(list1)):
    if list1[index] % 2 != 0:
        list2.append(list1[index])
        print(index, list1[index])

print(list2)
if list2:
    print("Lowest odd number:", min(list2))
else:
    print("No odd numbers found.")
 
# mylist = [ 10, 20,30,40, "abc"]

# for i in range (0,len(mylist)):
#      if (type(mylist(i))==int):
#        print(index, mylist [index])

mylist = [10,20,30,40,14]   
max =mylist[0]
for index in range (0,len(mylist)):
   print("before" , mylist[index],max)
   if(mylist[index]>max):
      max=mylist[index]
      print("after condition => " , mylist [index], max)

mylist = [10,20,30,40,14]   
max =mylist[0]
smax=0
for index in range (0,len(mylist)):
   print("before" , mylist[index],max)
   if(mylist[index]>max):
      smax=max
      max=mylist[index]
      print("after condition => " , smax, max)      

mylist = [10,20,30,40,14]   
max =mylist[0]
smax=0
for index in range (0,len(mylist)):
   print("before" , mylist[index],max)
   if(mylist[index]>max):
      smax=max
      max=mylist[index]
   elif(mylist[index]>smax):
      smax=mylist[index]  
      print("after condition => " , smax, max)      

total =0 
mylist = [ 10, 20,30,40]
for i in range (0,len(mylist)):
    total+=mylist[i]
    print(total)

total =0 
mylist = [ 10, 20,30,40]
for i in range (0,len(mylist)):
    total+=mylist[i]
print(total)

mylist = [10,20,30,40,35]
for i in range (0, len(mylist)):
   print(mylist[0],mylist[i])

mylist=[10,202,30,40,35]   
for index in range (0,1):
   print(mylist[index])
   for index2 in range (1,len(mylist)):
      print(mylist[index],mylist[index2])

mylist= [10,20,30,40,35]
for i in range (1,2):
   for j in range (1+i, len(mylist)):
        print(mylist[i], mylist[j])

mylist= [10,20,30,40,35]
for i in range (len(mylist)):
   for j in range (len(mylist)):
        if (mylist[i]+mylist[j] == 50):
         print(mylist[i], mylist[j])           

mylist = [1, 2, 3, 4, 5]
n = len(mylist)
for i in range(n // 2):
    mylist[i], mylist[n - 1 - i] = mylist[n - 1 - i], mylist[i]
print(mylist) 



#tuple 

x = (10,20, "abc", 10,20,30,40)
print ( x.count(10))
print (  x.type(30))
# x [0] = 19   # we can't insert , update , delete


mydictionary ={101:"hardik ", "salary": 20000 , "email":"hardikjhalani@gmail.com"}
print(mydictionary)
   
mydictionary ={101:"hardik ", "salary": 20000 , "email":"hardikjhalani@gmail.com"}
print(mydictionary["email"])
mydictionary["email"]="hardikjhalani263@gmail.com"    #update
print(mydictionary)

mydictionary["add "] = "jaipur "         #insert

mydictionary={10:"a" , 20:"b"}
for i in mydictionary.key():
   print (i,mydictionary[i])

mydictionary= {10:"a", "amount": 100}
mydictionary["amount"]= mydictionary["amount"]+5
print(mydictionary)   

s = "Raj5"
d = {'total':0}
for i in s:
    d["total"]+=1
print(d)


s = "abc"
x = {}
for i in s:
    if i in x:
        x[i]+=1
    else:
        x[i]=1
print(x)