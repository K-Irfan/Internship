#Tuples are just like lists
#But they are immutable
#Tuple can be of any datatype
#They also have '()' instead of '[]'
x=(1,2,3,'Irfan',True)
print(f"{x}\n")

y=tuple(('Irfan','Irfan','Irfan'))
print("Tuples can also have duplicate items")
print(f"{y}\n")

print("Using len() to determine length:")
print(f"{len(y)}\n")

#To create a tuple with only one value we need to add a comma at the end
#If not it'll be considered as a string or integer value instead of tuple depending on the value entered
a=(1)
print(a)
print(type(a))
b=("Irfan")
print(b)
print(type(b))
c=("Irfan",)
print(c)
print(type(c))

