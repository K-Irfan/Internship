#Lists can be iterated using loops
x=['Irfan','Anusha','Sulaiman']
for i in x:
    print(f"{i}")
print("\n")

#We can also iterate the index values of the lists
for j in range(len(x)):
    print(f"{j}")
print("\n")

#Using while loop
a=0
while a < 3:
    print(x[a])
    a+=1
print("\n")