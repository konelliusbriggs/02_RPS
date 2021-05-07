import random


# functions go here
def choice_checker(quistions, valid_list, error):

  error = "please choose from paper/ paper /scissors(or xxx to quit)"

  valid = false
  while not valid:

   # ask user for choice ( and put choice in lowercase)
    response = input(question).lower()
   
   
    if response == "r" or response == "rock":
      return response
    elif response =="p" or response == "paper":
      return response
    elif response == "s" or response == "scissors":
      return response

    # check for the exit code...
    elif response =="xxx":
      return response

# main routine goes here 
rounds_played


# loop for testing purposes
user_choice = ""
while user_choice != "xxx":

    # ask user for choice and check it's valid
    user_choice = choice_checker("choose rock / paper / " "scissors (r/p/s): " "please choose from rock / paper / scissors (or xxx to quit)")

    
    # print out choice for comparison purposes
    print(" you chose {}".format (user_choice))
 







# ask user for # of rounds, <ENTER> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

  
    # rounds heading
    print
    if rounds == "":
      heading = "countinous mode: round {}".format(rounds_played + 1)
      print (heading)    
      choose = input("{} or  'xxx' to end: ".format(choose_instruction))
      if choose == "xxx":
        break
    else:
      heading = "round {} of  {}".format(rounds_played + 1, rounds)
      print (heading)
      choose = input(choose_instruction)
      if rounds_played == rounds - 1:
        end_game = "yes"



game_summary =[]

rounds_lost = 0
rounds_drawn = 0 
rounds_played = 5

for item in range(0, 5):
  result = input("choose result: ")

  outcome = "Round {}: {}".format(item, result)

  if result == "lost":
    round_lost += 1
  elif result == "tie":
    rounds_drawn += 1

  game_summary.append(outcome)

rounds_won = rounds_played - rounds_lost - rounds_drawn

# **** Calculate game stats ******
percent_win = rounds_won / rounds_played * 100
percent_lose = rounds_lost / rounds_played * 100
percent_tie = rounds_drawn / rounds_played * 100



