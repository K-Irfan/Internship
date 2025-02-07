x=(1,2,3,'Irfan',True)
print("Accessing the tuple values using index numbers:")
print(x[3])
print(x[-2],"\n")

print("Tuple slicing:")
print(x[0:4])
print(x[-3:-1],"\n")

print("Checking if the value is in tuple or not:")
if 'Irfan' in x:
    print("Yes, 'Irfan' is in the tuple")
else:
    print("No, 'Irfan' isn't the tuple\n")