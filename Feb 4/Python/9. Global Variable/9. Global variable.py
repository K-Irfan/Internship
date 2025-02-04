globalVariable='Messi'
def football1():
  print(globalVariable,"is the Greatest Of All Time\n")

def football2():
  globalVariable='Ronaldo'
  print(globalVariable,"is a good player")

#If we declare a variable inside the function with the same name as the global variable it'll be used only in that function
#The global variable will remain the same

football1()
football2()