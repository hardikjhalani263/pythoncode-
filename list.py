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

