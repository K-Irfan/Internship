#The global variable can be changed inside a function using the keyword 'global'
globalVariable='Messi'

def football():
  global x
  x='Neymar'
  print(x,"should not have left Barcelona")

football()