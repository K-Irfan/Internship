#Bitwise operators are used to compare binary numbers
x=1
y=2
bin1=format(x,'b')
bin2=format(y,'b')
print("Binary value of 1 is:",bin1)
print("Binary value of 2 is:",bin2)
print("\nBitwise AND operator returns 1 if both bits are 1")
print(x & y)
print("Bitwise OR operator returns 1 if any one bit is 1")
print(x | y)
print("Bitwise XOR operator returns 1 only if one bit is 1")
print(x ^ y)
print("Bitwise NOT operator inverts all the bits")
print(~x)
print("The Zero fill left shift operator inserts the specified number of 0's from the right and let the same amount of leftmost bits fall off")
print(x << 2)
print("The Signed right shift operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's")
print(x >> 2)
