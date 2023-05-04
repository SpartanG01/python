###Input/Output Interaction Test 1
def isname(name):
  for char in name:
    if char.isdigit():
      return True
  return False
print("Let's define some variables...")
name = input("What is your name? ")
show_error = False
while True:
  if isname(name):
    show_error = True
    if show_error:
      print("I don't believe you, names only contain letters. Try again.")
      name = input()
  else:
    break
age = input("What is your age? ")
show_error = False
while True:
  try:
    age_check = float(age)
    break
  except ValueError:
    show_error = True
    if show_error:
      print("Stop fucking around and put in a god damn number.")
      age = input()
quest = input("What is your quest? ")
show_error = False
swallow = input("What is the average airspeed velocity of an unladen swallow? ")
while True:
  try:
    swallow_speed = float(swallow)
    break
  except ValueError:
    show_error = True
    if show_error:
      print("Stop fucking around and put in a god damn number.")
      swallow = input()
if swallow_speed == 20.1:
  print(name, " why in the name of all things holy would you know that? you ", age, " year old bastard")
else:
  print("see, ", name, " you cant even tell me the average airspeed velocity of an unladen swallow. I knew you were useless you ", age, " year old bastard")