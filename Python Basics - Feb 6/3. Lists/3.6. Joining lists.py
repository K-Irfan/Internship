#To join two lists we can simply add them using '+' or use append and extend functions
from decorator import append

x=[1,2,3]
y=[4,5,6]
z=x+y
print(f"{z}\n")

#using append
for a in y:
    x.append(a)
print(f"{x}\n")

#using extend
#here the values 4,5 and 6 comes twice because the values already gets added to x in the above loop
x.extend(y)
print(x)