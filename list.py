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
# lst = [1, [2, 3], [4, [5, 6], 7], 8]
# a = []

# for item in lst:
#     if isinstance(item, list):
#         for subitem in item:
#             if isinstance(subitem, list):
#                 a.extend(subitem)
#             else:
#                 a.append(subitem)
#     else:
#         a.append(item)

# print("flattened list:", a)


# question 8 
# list = [1,2,3,4,5,6]
# target = 9
# pairs = []
# for i in range (len(list)):
#     for j in range (i+1,len(list)):
#         if(list [i] +list[j] == target):
#             pairs.append (list[i], list[j])
# print (target , ":" , pairs)   


# question 9
# lst = [1, 2, 3, 2, 1]
# pal = True
# for i in range(len(lst)//2):
#     if lst[i] != lst[-i-1]:
#         pal = False
#         break

# print(pal)

# question 10
# num = [1, 2, 2, 3, 4, 4, 5 ]
# dup = []
# for i in range (len(num)):
#    for j in range (i+1 , len(num)):
#       if num[i] != num[j] and num[i] not in dup:
         
#          dup.append(num[i])
# print (dup)

# questin 11
# list1 = [1, 2, 3, 4, 5]
# list2 = [2, 3, 4, 6, 7]
# dup = []

# for i in list1:
#     if i in list2 and i not in dup:
#         dup.append(i)
# print(dup)

# question 12
# words = ["apple", "banana", "strawberry", "kiwi"]
# longest_word = ""
# for word in words:
#     if len(word) > len(longest_word):
#         longest_word = word

# print("The longest word is:", longest_word)


# question 13
# numbers = [1, 2, 4, 5, 6]

# for i in range(1, len(numbers)):
#     if numbers[i] - numbers[i - 1] != 1:
#         print("Missing number is:", numbers[i - 1] + 1)

# question 14
# numbers = [1, 2, 4, 5, 6]

# for i in range(1, len(numbers)):
#     if numbers[i] - numbers[i - 1] != 1:
#         print("Missing number is:", numbers[i - 1] + 1)

# question 15 
# numbers = [4, 5, 1, 2, 0, 4, 5, 2]
# frequency = {}
# for num in numbers:
#     if num in frequency:
#         frequency[num] += 1
#     else:
#         frequency[num] = 1
# for num in numbers:
#     if frequency[num] == 1:
#         print("First non-repeating element is:", num)
#         break

# question 16
# numbers = [0, 1, 0, 3, 12]
# index = 0
# for i in range (len(numbers)):
#     if numbers[i] != 0:
#         numbers[index] = numbers[i]
#         index += 1
# while index < len(numbers):
#     numbers[index] = 0
#     index += 1
# print (numbers)

# question 17
a = [1, 3, 2, 6, 5, 8, 7]

for i in range (len(a)-1):
    if(a[i]<a[i+1]):
     print (a[i+1])