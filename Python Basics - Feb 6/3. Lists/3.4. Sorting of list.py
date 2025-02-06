from curses.ascii import islower

marks=[89,78,83,90,97,93,10]
#The simple sort func makes the list in ascending order
marks.sort()
print(f"{marks}\n")

#To make the marks in descending order we can use (reverse=True)
marks.sort(reverse=True)
print(f"{marks}\n")

#If we use (reverse=False) the marks again will be in ascending order
desc=sorted(marks, reverse=False)
print(f"{desc}\n")

#Values closest to 50
def fun(x):
    x
    return abs(x-50)
marks.sort(key=fun)
print(f"{marks}\n")

#Case sensitive sort
names=['irfan','Anusha','Sulaiman']
names.sort()
print(f"{names}\n")
#Using the key value str.lower makes the code to take all the values as lower case and arrange them alphabetically
names.sort(key=str.lower)
print(f"{names}\n")

#Reversing string
names.reverse()
print(names)