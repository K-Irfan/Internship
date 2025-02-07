#To remove an item from a set we can use remove() or discard()

#Using remove()
#If the removing item is not in the set it will give an error
interns={'Irfan','Anusha','Sulaiman'}
interns.remove('Sulaiman')
print(interns,"\n")

#Using discard()
#If the removing item is not in the set it will not give an error
interns.discard('Sulaiman')
print(interns,"\n")

#We can also use the pop() but it'll remove the item randomly
#Since sets are unordered and un-indexed we cannot specify a particular index value to pop
interns.pop()
print(interns,"\n")

#We can use the clear() to empty the set
interns.clear()
print(interns,"\n")

#We can use the del() to delete the set
del interns