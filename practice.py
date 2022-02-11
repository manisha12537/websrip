# number=int(input("enter the number"))
# dicate=number%10
# ans=number-dicate
# print(dicate)
# print(ans)



# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
# m=sampleDict["class"]["student"]["marks"]["history"]
# print(m)




# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}
# for i in employees:
#     j={i:defaults}
#     print(j)





# sampleDict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york",
#   "contry":"india",
#   "job":"imploy"
# }
# list=["name","city","job"]
# dict={}
# for i in list:
#     dict.update({i:sampleDict[i]})
# print(dict)



# ample_dict = {
#     'emp1': {'name': 'Jhon', 'salary': 7500},
#     'emp2': {'name': 'Emma', 'salary': 8000},
#     'emp3': {'name': 'Brad', 'salary': 500}
# }
# ample_dict["emp1"]["salary"]=8973
# print(ample_dict)



# def func1(*args):
#     for i in args:
#         print(i)

# func1(20, 40, 60)
# func1(8
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# a=list1[2][2].append(7000)
# print(list1)


# def calculation(a,b):
#     sum=a+b
#     multiply=a*b
#     return(sum,multiply)
# reef=calculation(4,5)
# print(reef)




# list = [10,20,30,20,10,50,60,40,80,5]
# i=0
# a=[]
# while i<len(list):
#     j=list[0]
#     for k in list:
#         if j<k:
#             j=k
#     a.append(j)
#     list.remove(j)
# i=i+1
# print(a)
    





# list=[8,5,3,1,32,43,88,4]
# list1=[34,56,78,9,98,2]
# i=0
# b=[]
# for j in list:
#     if j not in b:
#         b.append(j)
#         for k in list1:
#             if k not in b:
#                 b.append(k)
# print(b)



# list=['a','b','r','a','g','b','f','d','r']
# duplicate=[]
# for i in list:
#     if list.count(i)>1:
#         if i not in duplicate:
#             duplicate.append(i)
# print(duplicate)



# num=input("rnter number")
# i=0
# list=[]
# while i<len(num):
#     j=0
#     k=[]
#     count=0
#     while j<len(num):
#         if num[j]==num[i]:
#             count=count+1
#         j=j+1
#     k.append(num[i])
#     k.append(count)
#     if k not in list:
#         list.append(k)
#     i=i+1
# print(list)




# a=[22,3,4,2]
# i=0
# while i<len(a):
#     print(a[i],end="")
#     i=i+1



# a=[1,2,3], [4,5,6], [10,11,12], [7,8,9]
# print(a[2])

# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# d1.update(d2)
# for i in d1:

# print(d1)



# a=int(input("enter the number"))
# i=1
# while i<=a:
#     print('"'+"q"+str(i)+'"','"'+"z"+str(i)+'"')
#     i=i+1



# str = "Python Output based Questions"
# word=str.split()
# for i in word:
#     print(i)



# a=input("enter the number")
# b=a.split()
# print(b)



# List = [1,2,3,1,2,2]
# a=[]
# i=0
# while i<len(List):
#     if List[i] not in a:
#         a.append(List[i])
#         # print(a)
#     i=i+1
# print(a)


# i=0
# while i<10:
#     i=i+1
#     if i==3:
#         continue
#     print(i)


# num=str(input("enter the number")) 
# j=1   
# while j<len(num):
#     if j!=3:
#         print(j)
#     j=j+1
   


# a=int(input("enter the number"))
# b=int(input("enter the number"))
# i=0
# while i<b:
#     print(a)
#     i=i+1












number=input("please enter the bynary number")
decimal_number=0
for i in number:
    decimal_number=decimal_number*2+int(i)
print(decimal_number)