#Syntax for list comprehension
#newlist = [expression for item in iterable if condition == True]
from nbconvert.filters import markdown2rst

#list comprehension gives the shortest syntax for looping in lists
marks=[89,78,83,90,97,93,10]
above90=[]
for x in marks:
    if x>=90:
        above90.append(x)
print(f"{above90}\n")

above90=[x for x in marks if x>=90]
print(f"{above90}\n")

#Prints the entire list
all=[x for x in marks]
print(f"{all}\n")

#Prints marks above 80
above80=[x for x in marks if x>80]
print(f"{above80}\n")

#Prints the first 3 numbers
fir3=[x for x in marks[:3]]
print(f"{fir3}\n")

#Printing the top 3 highest marks
top3=sorted(marks,reverse=True)[:3]
print(f"{top3}\n")

#Changing the datatype
inflt=[float(x) for x in marks]
print(f"{inflt}\n")
