import random

game_summary =[]

rounds_lost = 0
rounds_drawn = 0 
rounds_played = 5

For item in range(0, 5):
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

print(""
print("***** GAME HISTORY *****")
for game in game_summary:
    print(game)

print()

# display game stats with % values rounded to the nearest whole number
print(" ********* GAME STATS **********")
print("win: {}, ({:.0f}%)\nLoss: {}, "
      "({:.0f}%)\ntie: {}, ({:.0f}%)".format(rounds_won,percent_win,percent_lost,percent_lose,percent_drawn,percent_tied)