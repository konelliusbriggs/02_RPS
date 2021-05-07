# functions go home
 
  
 valid = False
  while not valid:
    
    response = input(question).lower()

    if response == "y" or response == "yes":
      return "yes"

    elif response == "n" or response == "no":
      return "no"

    else:
      print("Please enter yes / no")

played_before = yes_no("Have you played this game before? ")

if played_before != "yes":
  print("show instructions")