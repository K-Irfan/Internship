from operator import index

x=[1,2,3,4,5]
y=[6,7,8,9,10]

#append()
def app():
    localx=x.copy()
    for a in y:
        localx.append(a)
    print(f"{localx}\n")
app()

#extend
def ext():
    localx=x.copy()
    localx.extend(y)
    print(f"{localx}\n")
ext()

#clear()
def clr():
    localx=x.copy()
    localx.clear()
    print(f"{localx}\n")
clr()

#copy()
z=x.copy()
print(f"{z}\n")

#count
a=x.count(3)
print(f"{a}\n")

#index
b=x.index(4)
print(f"{b}\n")

#insert
x.insert(3,5)
print(f"{x}\n")

#pop
x.pop(3)
print(f"{x}\n")

#remove
x.remove(2)
print(f"{x}\n")

#reverse
x.reverse()
print(f"{x}\n")

#sort
p=[6,7,23,6,3,2,9]
p.sort()
print(f"{p}\n")
p.sort(reverse=True)
print(f"{p}\n")