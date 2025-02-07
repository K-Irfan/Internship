#Once created we cannot modify the set but can add to it

#To add a single value
interns={'Irfan','Anusha','Sulaiman'}
interns.add(20)
print(interns,"\n")

#To add values from another set
interns={'Irfan','Anusha','Sulaiman'}
numbers={1,2,3}
interns.update(numbers)
print(interns,"\n")

#We can add values from any iterable objects like tuples, lists and dictionaries
interns={'Irfan','Anusha','Sulaiman'}
print(interns)
print(type(interns))
numbers=[1,2,3]
print(numbers)
print(type(numbers))
interns.update(numbers)
print(interns)