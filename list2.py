# x = 257
# y =x
# print (id(x) , id (y))
# y = 1000
# print(id(x) , id(y))

# mylist = [1,2,3,4,5,6,]
# sum = 0
# for i in (len(mylist)):
#     sum += mylist[i]
# print (sum)    

# mylist = [1, 2, 3, 4, 5]
# count = 0
# for _ in mylist:
#     count += 1
# print(count)  


# list = [1,2,3,4,5,5]
# list2 = []
# for i in range(len(list)):
#     list2.append(list[i]**3)
# print(list2)

# list2 =[ ]
# list1 = [ 10,20,30, 40, 3,2,1]
# sum = 0
# for i in range ( 0, len(list1)):       
#     sum += list1[i]
#     list2.append(list1[i])     
# print ( sum / len(list1))   


# list = [1,2,3,4,5,6,7]
# i = sum = 0
# while i<len(list):
#     if(i == 0 or i == len(list)-1 or i == len(list)//2):
#         sum += list[i]
#     i += 1
# print(sum)

# my_list = ['apple', 42, 3.14, 100, 'banana']
# integers = []
# for x in my_list :
#     if type(x) == int:
#         integers.append(x)
# print(integers)

# mylist = [ 10,20,305,40,50]
# x=mylist[0]
# for i in range (0,4):
#     if (mylist[i]>x):
#         x = mylist[i]
#     print (x)    

# mylist = [10,20,30,24,3,5,6]
# for i in range (len(mylist)):
#     if (i % 2 == 0):
#      print (i)

# mylist = [105 ,20, 305, 40 ,50]
# a =0
# newlist = []
# for i in range (0,5):
#     a =a+mylist[i]
#     newlist.append(a)
# print(newlist)    
        
# mylist = [10,20,3,4,5,6,70]
# for n in mylist:
#     count = 1
#     for i in range (n):
#         for j in range (2[i]//2):
#             if (i%j == 0):
#                 count +=1
#         if (count == 2):
#             print(n)


# mylist = [10,20,123,1234]
# for n in (mylist):
#     m = n
#     count = 0 
#     while n > 0:
#         n = n//10
#         count +=1
#     if(count ==3):
#         print (m)
        
# mylist = [10, 20, 30, 20, 10]
# j = len(mylist)-1
# count = 0
# for i in range(len(mylist) // 2):
#     if mylist[i] != mylist[j]:
#         count += 1
#         break
#     j -= 1
# if(count == 0):
#     print(mylist,"palindrome")
# else:
#     print(mylist,"not palindrome")

# list1 = [1,2,3,4,5,6]
# for i in range (len(list1),0,-1):
#     print(i, end=' ')

data = "wellcome to regex"
s = ''
for i in data:
    s=i+s
print (s)    
