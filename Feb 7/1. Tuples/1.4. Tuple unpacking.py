#Unpacking a tuple is the same as unpacking a list
x=(1,2,3,4)
one,two,three,four=x
print(one)
print(two)
print(three)
print(four,"\n")

#Using asterisk
x=(1,2,3,4)
one,two,*three=x
print(one)
print(two)
print(three,"\n")

x=(1,2,3,4)
one,*two,three=x
print(one)
print(two)
print(three,"\n")

#Unpacking with slicing
x=(1,2,3,4)
one,two=x[:2]
print(one)
print(two)