import random 
# these are some useful subroutines 

def rollDice(side):
  result = random.randint(1,side)
  return result

def pp():
  # info = []
  for row in info:
    for item in row:
      print(item, end="\t|\t")
    print()

def password():
  correct = "Release0"
  attempts = 3
  while attempts > 0:
    passw = input("Enter your password\n> ").strip()
    if passw == correct:
      return
    else:
      attempts -= 1
      print(f"Incorrect password. {attempts} attempt(s) remaining \n")
  print("Too many incorrect attempts")
  exit()

def newPrint(color, word):
  if color=="red":
    print("\033[31m", word, sep="", end="")
  elif color=="green":
    print("\033[32m", word, sep="", end="")
  elif color=="blue":
    print("\033[34m", word, sep="", end="")
  else:
    print("\033[0m", word, sep="", end="")

