a=10
b=21
def greater():
    if (a>b):
        print(f"{a} is greater than {b}\n")
    else:
        print(f"{b} is greater than {a}\n")
greater()

print("We can use the isinstance() function to check if the corresponding\ndata type for a variable is true"
      " or not\n")
print(f"Is the variable 'a' an integer data type: {isinstance(a,int)}")

#Boolean values will always be 'True' for almost every values
#Except for empty values like [],{},() and 0