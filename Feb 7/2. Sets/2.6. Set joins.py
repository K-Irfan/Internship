from xmlrpc.client import Boolean

joins=['union()','update()','intersection()','difference()','symmetric_difference()']
print("The types of joins in sets are")
for i,no in enumerate(joins,1):
    print(i,no)
print("\n")


#union() joins both the sets
interns={'Irfan','Anusha','Sulaiman'}
numbers={2,3,4}
print("Both 'union()' and '|' are same")
set3=interns.union(numbers)
set4=interns|numbers
print(set3)
print(set4,"\n")

#We can use union to join multiple sets
#We can join set with other data types, but to do this we can't use '|', we can only use 'union()'
boole=[True,False]
alphab=('a','b','c','d')
set5=interns.union(numbers,boole,alphab)
print("Joining multiple sets")
print(set5,"\n")


#update() takes values from one set and adds them to another set
#Both union() and update() ignores duplicate values
interns.update(numbers)
print(interns,"\n")


#intersection() is used to print the common values in both the sets
print("interns=",interns)
print("set5=",set5)
set6=interns.intersection(set5)
print("Common values in both the sets are",set6)
print("\n")

#We can also use '&' instead of 'intersection()'
print("numbers=",numbers)
print("set5=",set5)
set7=numbers&set5
print("Common values in both the sets are",set7)
print("\n")

#By using the intersection_update() we can print the duplicate values
#But it will update the set instead of creating a new set
print("interns=",interns)
print("set5=",set5)
interns.intersection_update(set5)
print("Common values in both sets",interns)
print("\n")


#difference() will give the items that are in 1st set but not in 2nd
print("interns=",interns)
print("set5=",set5)
set8=interns.difference(set5)
print("Since all the items in the 'Interns' set are present in the 'set5' it will give an empty set")
print(set8,"\n")

#We can use '-' instead of 'difference()'
print("set5=",set5)
print("Interns=",interns)
set9=set5 - interns
print(set9,"\n")

#difference_update() updates the 1st set with the values not in 2nd set
print("set5=",set5)
print("Interns=",interns)
set5.difference_update(interns)
print(set5,"\n")


#symmetric_difference() will keep items that are not common in the sets
#We can also use '^' for symmetric_difference()
a={1,2,3,4,5}
b={4,5}
c=a.symmetric_difference(b)
d=a^b
print(c)
print(d,"\n")

#symmetric_difference_update()  will keep all but the duplicates
a={1,2,3,4,5}
b={4,5}
a.symmetric_difference_update(b)
print(a)