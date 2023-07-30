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
            print("Hint 5: Some other hint for hint number 5.  \nGuess carefully!  This is your last chance!")
        
# This is the game function.  Here, the player will be asked if they want to play.  If yes, the function proceeds in various while loops.
# In this section, the game() function accesses the country list and choses a country at random for the plaeyr to guess.
# The game() function calls on the GiveHint() functions to give the player hints if they make incorrect guesses.
# After 5 incorrect guesses, the function calls upon itself once more to start over with a new country guess. 

def game():
    GameStart = False
    
    while GameStart !=True:
        answer = input("Would you like to play?  y/n \n")
        
        if answer.lower() == "y":
            GameStart = True
            countrylist = list(countries_data.keys())
            Country = random.choice(countrylist)
            Stripped_Country = Country.strip(" ")
            print ("Okay.  Great!")
            time.sleep (2)

            GuessCorrect = False
            HintNumber = 0
            while GuessCorrect != True:
                Guess = input(f"{hangman_style_text(Country)}\nIt has {len(Stripped_Country)} letters!\nWhat country am I thinking of?\n")                
                if Guess.lower() == Country.lower():
                    time.sleep (1)
                    print ("You're right!")
                    GuessCorrect = True
                    sys.exit() 
                elif HintNumber == 5:
                    print("You lose!")
                    time.sleep(3)
                    game()
                else:
                    print ("Nope!  Try again!\n")
                    HintNumber = HintNumber + 1
                    time.sleep (2)
                    GiveHint(Country, HintNumber)
                    
            
        elif answer.lower() == "n":
            print("Okay.  Fine by me.  Goodbye!")
            sys.exit()
        
        else:
            print("That isn't a valid option!")

game()