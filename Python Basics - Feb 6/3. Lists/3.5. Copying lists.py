#We can use list(), copy() and slice operator to copy the list

names=['Irfan','Anusha','Sulaiman']
#copy() method
names2=names.copy()
print(f"{names2}\n")

#list() method
names3=list(names)
print(f"{names3}\n")

#Slice operator
names4=names[:]
print(f"{names4}\n")
