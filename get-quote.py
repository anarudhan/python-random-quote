import random

<<<<<<< HEAD
def main():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = 13
  rnd = random.rndint(0, last)
=======
def primary():
  # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = 13
  rnd = random.randint(0, last)

>>>>>>> 298d9fe54c21551aaf02a969687279dc2ffb255f

  print(quotes[rnd])

if __name__== "__main__":
  primary()
