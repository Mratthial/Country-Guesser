import requests 
from bs4 import BeautifulSoup
import re
import sys
import random

# Make a hangman style text to help figure out what Country it is based in the size.  Sourced from ChatGPT.
def hangman_style_text(text):
    return ' '.join('_' if c.isalpha() else c for c in text)

def CountryListImport():
    # access the https address of the website, and parse the data.
    res = requests.get("https://www.worldometers.info/geography/alphabetical-list-of-countries/")
    soup = BeautifulSoup(res.text, 'html.parser')

    # use beautiful soup to find the data from the website.  Find all the "td" elements with the specific CSS style, and return the HTML data in this style.  
    Country_Cells = soup.find_all('td', style="font-weight: bold; font-size:15px")
    Country_Names = [cell.text.strip() for cell in Country_Cells]

    #From ChatGPT, to remove anything within brackets that is not the country name.  Includes former names and abbreviations.
    pattern = r'\([^)]*\)'
    cleaned_data_list = [re.sub(pattern, '', item).strip() for item in Country_Names]

    # seperate the list into new lines in the .txt file.  This is where we will chose the country's from!
    with open("CountryGuesser/Data_Scrubbing_Version_Alpha/Country_List.txt", 'w') as file:
        for country_name in cleaned_data_list:
            file.write(country_name + "\n")
    return cleaned_data_list

# As the player gets their guesses wrong, give them hints.  There are 2 hints.  After the 5th wrong guess, the game will end and restart to a new country guess.
def GiveHint(Country, IncorrectGuess):
        if IncorrectGuess == 1:
            FirstLetter = str(Country[0])
            print(f"Hint 1: The country starts with the letter {FirstLetter}.")
        elif IncorrectGuess == 2:
            LastLetter = str(Country[-1])
            print(f"Hint 2: The country ends with the letter {LastLetter}.")
        
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
            countrylist = open("CountryGuesser/Data_Scrubbing_Version_Alpha/Country_List.txt", "r")
            Country = random.choice(countrylist.readlines()).strip()
            print ("Okay.  Great!")

            GuessCorrect = False
            IncorrectGuess = 0
            while GuessCorrect != True:
                Guess = input(f"What country am I thinking of?\n{hangman_style_text(Country)}\n\n")                
                if Guess.lower() == Country.lower():
                    print ("You're right!")
                    GuessCorrect = True
                    sys.exit() 
                elif IncorrectGuess == 5:
                    print("You lose!")
                    print(f"The answer was {Country}!")
                    game()
                else:
                    print ("Nope!  Try again!\n")
                    IncorrectGuess = IncorrectGuess + 1
                    GiveHint(Country, IncorrectGuess)
                    
            
        elif answer.lower() == "n":
            print("Okay.  Fine by me.  Goodbye!")
            sys.exit()
        
        else:
            print("That isn't a valid option!")

game()