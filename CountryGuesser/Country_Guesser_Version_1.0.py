import requests 
from bs4 import BeautifulSoup
import pprint 
import re
import sys
import random
import time
from Country_Dictionary import * 

# Make a hangman style text to help figure out what Country it is based in the size.  Sourced from ChatGPT.
def hangman_style_text(text):
    return ' '.join('_' if c.isalpha() else c for c in text)

# As the player gets their guesses wrong, give them hints.  There are 5 hints.  After the 5th wrong guess, the game will end and restart to a new country guess.
def GiveHint(Country, Hint_Number):
        if Hint_Number == 1:
            country_data = countries_data[Country]
            continent = country_data['continent']
            print(f"Hint 1: The country is in {continent}")
        elif Hint_Number == 2:
            FirstLetter = str(Country[0])
            print(f"Hint 2: The country starts with the letter {FirstLetter}.")
        elif Hint_Number == 3:
            LastLetter = str(Country[-1])
            print(f"Hint 3: The country ends with the letter {LastLetter}.")
        elif Hint_Number == 4:
            country_data = countries_data[Country]
            language = country_data['language']
            print(f"Hint 4: In this country, the languages spoken are {language}.")
        elif Hint_Number == 5:
            FirstTwoLetters = str(Country[:2])
            print(f"Hint 5: The country starts with the letters {FirstTwoLetters}.  \nGuess carefully!  This is your last chance!")
        
# This is the game function.  Here, the player will be asked if they want to play.  If yes, the function proceeds in various while loops.
# In this section, the game() function accesses the country list and choses a country at random for the plaeyr to guess.
# The game() function calls on the GiveHint() functions to give the player hints if they make incorrect guesses.
# After 5 incorrect guesses, the function calls upon itself once more to start over with a new country guess. 

def Need_Rules():
    while True:
        Ask_Rules = input("Do you want the rules? y/n\n")
        if Ask_Rules.lower() == "y":
            time.sleep (2)
            print ("I will think of a random country out of all the countries in the world.  If you want, you can check the country list in the 'Country List' text file!")
            time.sleep (4)
            print ("You guess the country based on how many letters the country name is.  If you guess wrong, I'll give you some hints!")
            time.sleep (3)
            print ("But be careful!  You only get 5 guesses!  If you run out of guesses, you lose!")
            break
        elif Ask_Rules.lower() == ("n"):
            print("Ok.  No problem!")
            time.sleep (1.5)
            break
        else: 
            print("That option isn't valid!")

def Country_Guesser_game():
    GameStart = False
    rules_shown = False

    while GameStart !=True:
        answer = input("Would you like to play the country guessing game?  y/n \n")
        
        if answer.lower() == "y":
            GameStart = True
            Play_Again = False
         
            if not rules_shown:
                print("Okay.  Great!\n")  
                Need_Rules()
                rules_shown = True

            while Play_Again != True:
                countrylist = list(countries_data.keys())
                Country = random.choice(countrylist).strip()
                Stripped_Country = Country.strip(" ")
            
                GuessCorrect = False
                HintNumber = 0
                while GuessCorrect != True:
                    Guess = input(f"{hangman_style_text(Country)}\nIt has {len(Stripped_Country)} letters!\nWhat country am I thinking of?\n")                
                    if Guess.lower() == Country.lower():
                        time.sleep (1)
                        print ("You're right!")
                        GuessCorrect = True
                        Play_Again = False
                        break
                    elif HintNumber == 5:
                        print("You lose!")
                        time.sleep(1.5)
                        print(f"The country I was thinking of was {Country}!")
                        break
                    else:
                        print ("Nope!  Try again!\n")
                        HintNumber = HintNumber + 1
                        time.sleep (2)
                        GiveHint(Country, HintNumber)
                
                while True:
                    Play_Again = input("Would you like to play again? y/n\n")
                    if Play_Again.lower() == "y":
                        print("Sure!")
                        break
                    elif Play_Again.lower() == "n":
                        print("Ok. Thanks for playing!")
                        sys.exit()
                    else:
                        print("That isn't a valid option!")  
                
        elif answer.lower() == "n":
                print("Okay.  Fine by me.  Goodbye!")
                sys.exit()
            
        else:
            print("That isn't a valid option!")

Country_Guesser_game()