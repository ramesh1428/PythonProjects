list1 = [2,7,11,15]
list2 = []
target_value = 26
dict1 = {}
for i in range(0,len(list1)):

   a = target_value-list1[i]
   if a in dict1.keys():
       list2.append(dict1.get(a))
       list2.append(list1.index(list1[i]))
   else:
       dict1.update({list1[i]:i})

print("Index values of two elements that are equal to Sum of target value are :",list2)
