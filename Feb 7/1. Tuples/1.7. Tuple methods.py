#Unlike lists, tuple has only two built-in methods
#count() gives the number of times a value is in the tuple
x=(1,4,2,4,3,4,5,6,7,4)
y=x.count(4)
print(y,"\n")

#index() gives the index value of a specified number
#But it takes into account only the first occurrence of the values
a=x.index(4)
print(a)