#To check whether the number is prime or not
num = int(input("Enter a number: "))
for i in range(2,num):
  if num%i==0:
    print("Not a prime number")
    break
  else:
    print("Its a Prime number")
    break