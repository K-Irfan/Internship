#A set is a collection which is unordered, unchangeable, and un-indexed
interns={'Irfan','Anusha','Sulaiman'}
print(interns)
print(type(interns),"\n")

#Sets doesn't allow duplicate values
#If there is a duplicate value the set ignores it
#The values 'True' & '1' and 'False' & '0' are taken as similar values
interns= set(('Irfan','Anusha','Sulaiman','Irfan',True,1,False,0))
print(interns)
print(type(interns),"\n")

#Getting length of a string
print(len(interns))

