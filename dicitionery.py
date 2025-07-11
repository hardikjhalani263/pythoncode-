<<<<<<< HEAD
# myAdhar = {10:"yash" , 11:"happy"}
# print (myAdhar[11])    # access[key]

# myAdhar [11] = "sad"        #update
# myAdhar [19] = "kajal"      # insert
# print(myAdhar)

# myAdhar = {10:"yash" , 11:"happy" , "salary": 80000}
# myAdhar.pop(11)
# print (myAdhar)

# myAdhar ={"salary": 58000}
# myAdhar ["salary"] = myAdhar["salary"] + 1000
# print (myAdhar)

# dict ={"total":0}
# for i in range (1,19):
#   dict ["dict"] = dict ["total"] +1
#   print (dict)  

# data = "hard"
# mydict ={"count":0}
# for i in data:
#   print(i)
#   mydict["count"]+1

# # a = "abcdefghijk"
# # dict = {"total":10}
# # count = 0
# # for i in a:
# #   if (i== 'a' or i == 'o' or i == 'u' or i == 'e' or i == 'i' ):
# #     count +=1
# #     dict["total"] = count
# #     print(dict)

# data = {}
# for i in range (0,6):
#  data[i] = i*i
# print (data)    

# s = "adefghi"
# dict = {}
# for i in s:
#  if (i in "aeiou"):
#   dict[i] = 1

# mylist = [10,20,30,10,40,50,50,30]
# mydictionery ={}
# for i in mylist:
#     if(i in mydictionery):
#         mydictionery[i] = mydictionery[i]+1
#     else:
#         mydictionery[i] = 1
# print (mydictionery)        


# s = 'abc'
# for i in range(0,4):
#     data  = " "
#     for j in range (0,i):
#         print(i,j,s[j])
#         data = data+s[j]
#     print ("data ==>" , data )    


# s ='abc'
# data = {}
# for i in s:
#     s1 = ''
#     for j in s:
#         if(i!=j):
#             s1+=j
#     data[s1] = 1
# print(data)        



s ='abc'
dict={}

for i in range(0,len(s)):
    value=""
    for j in range(0,len(s)):
        if(i!=j):
            value=s[i]+s[j]
            dict[value]=1
        if(i==j):
            dict[s[i]]=1

    data = 1
=======
# myAdhar = {10:"yash" , 11:"happy"}
# print (myAdhar[11])    # access[key]

# myAdhar [11] = "sad"        #update
# myAdhar [19] = "kajal"      # insert
# print(myAdhar)

# myAdhar = {10:"yash" , 11:"happy" , "salary": 80000}
# myAdhar.pop(11)
# print (myAdhar)

# myAdhar ={"salary": 58000}
# myAdhar ["salary"] = myAdhar["salary"] + 1000
# print (myAdhar)

# dict ={"total":0}
# for i in range (1,19):
#   dict ["dict"] = dict ["total"] +1
#   print (dict)  

# data = "hard"
# mydict ={"count":0}
# for i in data:
#   print(i)
#   mydict["count"]+1

# # a = "abcdefghijk"
# # dict = {"total":10}
# # count = 0
# # for i in a:
# #   if (i== 'a' or i == 'o' or i == 'u' or i == 'e' or i == 'i' ):
# #     count +=1
# #     dict["total"] = count
# #     print(dict)

# data = {}
# for i in range (0,6):
#  data[i] = i*i
# print (data)    

# s = "adefghi"
# dict = {}
# for i in s:
#  if (i in "aeiou"):
#   dict[i] = 1

# mylist = [10,20,30,10,40,50,50,30]
# mydictionery ={}
# for i in mylist:
#     if(i in mydictionery):
#         mydictionery[i] = mydictionery[i]+1
#     else:
#         mydictionery[i] = 1
# print (mydictionery)        


# s = 'abc'
# for i in range(0,4):
#     data  = " "
#     for j in range (0,i):
#         print(i,j,s[j])
#         data = data+s[j]
#     print ("data ==>" , data )    


# s ='abc'
# data = {}
# for i in s:
#     s1 = ''
#     for j in s:
#         if(i!=j):
#             s1+=j
#     data[s1] = 1
# print(data)        



s ='abc'
dict={}

for i in range(0,len(s)):
    value=""
    for j in range(0,len(s)):
        if(i!=j):
            value=s[i]+s[j]
            dict[value]=1
        if(i==j):
            dict[s[i]]=1

    data = 1
>>>>>>> e4549c6dedbff28b19613904c35f1515644cb5fb
print(dict)   