#getting first three elements using unpacking
fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
print("Getting the first three elements:")
one,two,three,*remaining=fruits
print(one)
print(two)
print(f"{three}\n")

#getting last three elements using unpacking
print("Getting the last three elements:")
*frontremaining,five,six,seven=remaining
print(five)
print(six)
print(f"{seven}\n")

#reversing the list using slicing
print("Reversing the list using slicing:")
print(f"{fruits[::-1]}\n")

#creating a list of 20 numbers using 'for' loop
print("Creating a list of 20 numbers using 'for' loop:")
def creatinglist():
    numbers=[]
    for i in range (1,21):
        numbers.append(i)
    return numbers

numbers=creatinglist()
print(f"{numbers}\n")

#getting the even values using list comprehension
#list comprehension gives the shortest syntax for looping in lists
print("Getting the even values from the list:")
even=[x for x in numbers if x%2==0]
print(even)

#swapping two numbers using list unpacking
print("\nSwapping two values:")
a=5
b=10
list=[a,b]
first,second=list
print("A=",second)
print("B=",first)