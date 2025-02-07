#Once tuples are created they cannot be changes as tuples are immutable
#So to update or modify tuple values we should change it into list
x=('Irfan','Anusha','Sulaiman')
print(x)
print("Data type of X:",type(x),"\n")

y=list(x)
print(y)
y[0]='Irfan K'
x=tuple(y)
print("Data type of Y:",type(y),"\n")

print("The tuple got converted into a list and got it's value updated\n"
      "and then got converted back to a tuple")
print(x)
print(type(x),"\n")

#Adding values to a tuple is similar to modifying it
print(x)
print(type(x))
y=list(x)
y.insert(0,'Irfan')
print(y)
x=tuple(y)
print(type(x),"\n")

#We can add tuples with tuples
print(x)
print(type(x))
y=("IrfanK",)
x += y
print(x,"\n")

#To remove values from tuple we have to convert it into a list
print(x)
print(type(x))
y=list(x)
y.remove('IrfanK')
print(y)
print(type(y))
x=tuple(y)
print(x)
print(type(x),"\n")

#Deleting a tuple
print(x)
print(type(x))
del x
print(x)