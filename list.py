# question 1
# numbers = [10, 20, 4, 45, 99]
# max = numbers[0]
# for i in ( numbers):
#    if i>max:
#     max = i
# print ("the maxium no is " , max)


#question 2
# num = [10,20,30,40]
# sum =0 
# for i in num:
#   sum+=i
# print(sum)


# question 3
# mylist = [1, 2, 3, 4, 5]
# n = len(mylist)
# for i in range(n // 2):
#     mylist[i], mylist[n - 1 - i] = mylist[n - 1 - i], mylist[i]
# print(mylist) 


# question 4 
# numbers = [10, 20, 4, 45, 99]
# n = len(numbers)
# for i in range(n):
#     for j in range(0, n - i - 1):
#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
# print("Sorted list in ascending order:", numbers)


# question 5
# num = [1, 2, 2, 3, 4, 4, 5 ]
# dup = []
# for i in range (len(num)):
#    for j in range (i+1 , len(num)):
#       if num[i] != num[j] and num[i] not in dup:
         
#          dup.append(num[i])
# print (dup)         

     
 #question 6
# list = [ 1,2,3,4,3,5,6]
# target = 6
# pairs = []
# for i in range (len(list)):
#     for j in range (i+1,len(list)):
#         if(list [i] +list[j] == target):
#             pairs.append ((list[i], list[j]))
# print (target , ":" , pairs)   
  

#question 7
lst = [1, [2, 3], [4, [5, 6], 7], 8]
a = []

for item in lst:
    if isinstance(item, list):
        for subitem in item:
            if isinstance(subitem, list):
                a.extend(subitem)
            else:
                a.append(subitem)
    else:
        a.append(item)

print("flattened list:", a)



