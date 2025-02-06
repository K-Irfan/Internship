x=[1,'Irfan',True,'Anusha','Sulaiman']
print("Lists can have any data type")
print(x)
print("The length of the list is",len(x))
print(f"{type(x)}\n")

print("Slicing of list:")
print(x[1])
print(x[-1])
print(x[1:4])
print(f"{x[-4:]}\n")

print("Checking if present in list:")
if "Irfan" in x:
    print(f"{True}\n")

print("Modifying list items:")
x[0]=10
print(x)
x[1:3]=[True,'Irfan']
print(x)

#x=[1,'Irfan',True,'Anusha','Sulaiman']
#As there are more values getting replaced than the specified amount in the index, the rest gets moved
x[1:3]=['Irfan',True,'Anusha']
print(x)

#As we are changing two index values but specifying only one value foe changing it, the next index value gets ignored
#Here the value for index '1' gets changed to 'Hello' and the next index value '2' gets ignored
#The rest comes as it is
x[1:3]=['Hello']
print(f"{x}\n")

print("Adding items to the list:")
#By using the append function we can add a value at the end
x.append('Hi')
print(x)

#Inserting extra value at the specified index
x.insert(1,'Irfan')
print(f"{x}\n")

print("Combining two lists:")
y=[10,20,30]
x.extend(y)
print(f"{x}\n")


print("Removing values from the list:")
#The remove function only removes the first occurrence of the value
x.remove('Anusha')
print(x)

#The pop function is used to remove value from the specified index
x.pop(5)
print(x)

#If no index value is given it will remove the last value
x.pop()
print(x)

#Just like the remove function delete function can also be used to remove values
#If no index value is given in the del() the entire list will be deleted
del x[2]
print(x)

#The clear function is used to clear the values of the list
y.clear()
print(y)