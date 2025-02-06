#Identity operators are used to check if the memory location of the objects are
#It's not used to check if they are same values
x=['Irfan','Anusha']
y=['Irfan','Anusha']
z=x
a=x
b=y
print(x is y)
print("'x is y' returns false because even though x and y have same values they are not same.\n")
print(x is z)
print("'x is z' returns true because they have the same memory.\n")
print(a is x)
print("'a is x' returns true because they have the same memory.\n")