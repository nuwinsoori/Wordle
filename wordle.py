import random
import time
from termcolor import colored
from replit import clear


def get_word():
  # chooses a random word from words_list.py and lowercase 
  random_word = random.choice((open("/Users/nuwin/Dropbox/Coding/Python/Wordle/words_list.txt").read().split()))
  random_word = random_word.lower() 
  return random_word
  
backspace = "\033[A                             \033[A"

guess = "" 
win = False
guess_number = 0 # max guesses is 6
random_word = get_word()
guess_number_list = ["first", "second", "third","fourth", "fifth", "final"]
placeholders = ["_ _ _ _ _","_ _ _ _ _","_ _ _ _ _","_ _ _ _ _","_ _ _ _ _","_ _ _ _ _"]

# prints the rules of the game
print("\nWordle by Nuwin Sooriyaarachchi\nYou have six guesses to try and guess the 5 letter word\nIf a letter is correct but in he wrong spot, it will appear yellow\nIf a letter is correct and in the right position it will appear green.")
print("\nPress enter to start")
start_button = input("")
clear() # clears rules when user presses button 


while guess_number < 6:
  dont_touch_list = []
  # print placeholders and previous guesses 
  for i in range(0,len(placeholders)):
    print(f"{placeholders[i]}")
     
  
  random_word_listed = [*random_word]
  while True:
    guess = input(f"Enter {guess_number_list[guess_number]} guess: ").lower()
    # DEBUG HELP
    if guess == "help":
      print(random_word)
      print("")
      continue
    if guess in open("/Users/nuwin/Dropbox/Coding/Python/Wordle/all_words.txt").read().split():
      break
    else:
      print(backspace)


  guess_listed = [*guess] # for changing colour of text 



  # right letter right location loop 
  for i in range(0,len(guess_listed)):
    if guess_listed[i] == random_word_listed[i]:
      guess_listed[i] = colored(guess_listed[i], "green")
      random_word_listed[i] = ""
      # adds i value to list to tell computer to not change later
      dont_touch_list.append(i)

  # includes "" so computer knows to skip later 
  yellow_dont_touch = "".join(random_word_listed)

  # right letter wrong location loop
  for i in range(0, len(guess_listed)):
    if i in dont_touch_list:
      continue
    if guess_listed[i] in yellow_dont_touch:
      index = random_word.find(guess_listed[i])
      random_word_listed[index] = ""
      guess_listed[i] = colored(guess_listed[i], "yellow")
      dont_touch_list.append(i)
      yellow_dont_touch = "".join(random_word_listed)



  # join guess into string and append into list 
  guess_joined = " ".join(guess_listed)
  placeholders[guess_number] = guess_joined

  # increment guess number by +1 
  guess_number += 1
  clear()

  # breaks loop if won  
  if guess == random_word:  
    win = True
    break

for i in range(0,len(placeholders)):
  print(f"{placeholders[i]}")

if win == False:
  print("YOU LOST!\n")
  print("The word was '" + colored(random_word, "red")+"'")
else:
  print("YOU WON!")
  time.sleep(1)




