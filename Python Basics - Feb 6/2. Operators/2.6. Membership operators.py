#Used to check if a value is present in the variable or not
def group():
    x=[]
    for i in range (1,6):
       x.append(i)
    return x
x=group()
print(x)
print(3 in x)
print(7 not in x)