# num=input("enter the name")
# m=num.split()
# print((m[0]))


# def m(max_min):
#     max=0
#     min=0
#     j=max_min[0]
#     for i in max_min:
#         if j>i:
#             min=i
#         elif i>j:
#             max=i
#     print(max)
#     print(min)

# m([8, 10, 15, 40, -5, 42, 17, 28, 75])


# dic1={1:10, 2:20}
# k=2
# if k in dic1:
#     print("y")
# else:
#     print("n")


# dic={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# for i,j in dic.items():
#     print(i,"--->",j)











# num=int(input("eneter the number"))
# i=1
# j=0
# k={}
# while i<=num:
#     j=i*i
#     k[i]=j
#     i=i+1
# print(k)




# student_data = {'id1': 
#    {'name': ['Sara'], 
#     'class': ['V'], 
#     'subject_integration': ['english, math, science']
#    },
#  'id2': 
#   {'name': ['David'], 
#     'class': ['V'], 
#     'subject_integration': ['english, math, science']
#    },
#  'id3': 
#     {'name': ['Sara'], 
#     'class': ['V'], 
#     'subject_integration': ['english, math, science']
#    },
#  'id4': 
#    {'name': ['Surya'], 
#     'class': ['V'], 
#     'subject_integration': ['english, math, science']
#    },
# }
# dic={}
# for i,j in student_data.items():
#     if j not in dic.values():
#         dic[i]=j
# print(dic)
  

# list=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# list1=[]
# for i in list:
#     for j in i.values():
#         if j not in list1:
#             list1.append(j)
# print(list1)



name="MISSIPPI"
dict={}
for i in name:
    dict[i]=dict.get(i,0)+1
print(dict)         








