#https://github.com/sarbajoy/Number/Guess/blob/master/numberguess.py
import random
number = random.randrange(0,20)
guessCheck = "wrong"
print("Welcome to Number Guess")

while guessCheck == "wrong":
  response = int(input("please input a number between 0 and 20: "))
  try:
    val = int(response)
  except ValueError:
    print("This is not an integer, please enter a number")
    continue
  val = int(response)
  if val < number:
    print("Too low")
  elif val > number:
    print("Too high")
  else:
    print("Congrats, you guessed right")
    guessCheck = "correct"
    print("Thanks for playing, see you soon")