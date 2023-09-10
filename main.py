import os
import random
from art import logo
score = 0
from game_data import data
game = True
#data loaded
#now from this data we have to randomly take one item in the dictionary
while game:
  print(logo)
  A = random.choice(data)
  #print(randata1)
  print(f"Compare A: {A['name']}, {A['description']}, from {A['country']}.")
  from art import vs
  print(vs)
  i=0
  while i == 0:
    B = random.choice(data)
    if B != A:
      print(f"Compare B: {B['name']}, {B['description']}, from {B['country']}.")
      i=1
    else:
      i=0
  choose = input("who has more followers? Type 'A' or 'B'")

  if choose == "A":
    if A['follower_count'] > B['follower_count']:
      print("huray")
      score += 1
      os.system('clear') 
    else:
      print(f"Sorry! you lost. Final Score = {score}")
      game = False 

  elif choose == "B":
    if B['follower_count'] > A['follower_count']:
      print("huray")
      score += 1
      os.system('clear') 
    else:
     print(f"Sorry! you lost. Final Score = {score}") 
     game = False
    
    



