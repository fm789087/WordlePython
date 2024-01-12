#Wordle 
#4/24/2023 
#In this program we code our wordle game 

import numpy as np #import the numpy library to read word files 
import random #import random 

validWords=np.loadtxt("words.txt",dtype="str") #splits the words file into an array made up of strings. This is used for checking valid words 
wordAnswers=np.loadtxt("text.txt",dtype="str") #splits the text file into an array made up of strings. This is used for checking the possible answer words 
#COLORS AND TEXT STYLES USED IN THE  GAME 
bold = "\u001b[1m"
CYAN = "\033[1;36m"
LIGHT_GREEN = "\033[1;32m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
BACKGROUND_PINK = "\u001b[45m"

#SET DEFAULT USER MENU INPUT TO 0 TO START 
userMenuInput=0


#---------------------------------------TITLE---------------------------------------------------  
print("")
print(LIGHT_BLUE+"                _ _     ")
print(" _ _ _ ___ ___ _| | |___")
print("| | | | . |  _| . | | -_|") 
print("|_____|___|_| |___|_|___|") 
print("")
print(""+LIGHT_GRAY)                 

#-----------------------------FUNCTIONS----------------------------
def help(): #FUNCTION FOR HELP/INSTRUCTIONS 
  print("") #for spacing style
  print("") #for spacing style
  print(LIGHT_PURPLE+"      💟💟💟      INSTRUCTIONS     💟💟💟    ")
  print("") #for spacing style
  print("The rules are simple:")
  print("There is a five-letter word that you must guess.")
  print("You will be asked to type in the word.")
  print("a) A "+LIGHT_GRAY+" LIGHT GRAY "+ LIGHT_PURPLE+ "letter will indicate that the letter is not in the word at all.")
  print("b) A "+LIGHT_GREEN+" LIGHT GREEN "+ LIGHT_PURPLE + "letter will indicate that the letter is in the word at the right position! ")
  print("c) A "+YELLOW+" YELLOW "+ LIGHT_PURPLE + "letter will indicate that the letter is in the word, but at the wrong position! ")
  print("If you are able to guess the word correctly, you WIN!"+LIGHT_GRAY)
  print("") #for spacing style
  
#-------------------------------USER INPUT FOR THE MENU------------------------------------
while userMenuInput!=3: 
  #-------------------------------MENU STYLE----------------------------
  print(bold+CYAN+"------------------------------------------")
  print("What would you like to do? ") 
  print("1. ✨ Play the game! ✨")
  print("2. 🌻 Game Instructions/Help! 🌻 ")
  print("3. 😿 Quit the program!  😿 ")
  print("------------------------------------------"+LIGHT_GRAY)
  print("") #for spacing style
  userMenuInput=int(input(LIGHT_BLUE+"Enter your option here: \n"+LIGHT_GRAY)) #get input for the menu options
  #============================================PLAY THE GAME==============================================
  if userMenuInput==1: 
    randomIndex=random.randint(0, wordAnswers.size-1) # generate a random integer between 0 and the length of valid words file -1 
    word=validWords[randomIndex] #generate random answer word 
    lettersWord=list(word) #create an array of letters from word 
    row1=[] #set row 1 to empty array 
    displayLetters="" #reset display letters to empty string (this concatonates the output)
      
    #--------------------------GOING THROUGH EACH GUESSED WORD--------------------
    for x in range (0, 5, 1): #5 tries is the maximum 
      displayLetters="" # Reset the display letters to empty string 
      wordUser=input(LIGHT_PURPLE+"What is the 5-letter word you would like to enter? "+LIGHT_GRAY)
      while wordUser.lower() not in validWords or len(wordUser) != 5:   #check if word is in valid words list or it its length is 5 
        wordUser=input(LIGHT_RED+"Word is not valid. Try again! "+LIGHT_GRAY)  #prompt for a valid word entry 
      if wordUser==word: # if the user is correct 
        print(LIGHT_GREEN+"Correct! The correct word was in fact "+word+LIGHT_GRAY); 
        break #break from the loop 
  
    #--------------------------GOING THROUGH 5 LETTERS IN THE WORD GUESSED-------------------
      wordUser = wordUser.lower()
      for y in range(0, 5, 1): # for 5 letters total 
        if wordUser[y]==lettersWord[y]: #if the letters at the position match, make them green 
          displayLetters=displayLetters+LIGHT_GREEN+wordUser[y].upper()+LIGHT_GRAY 
          
        elif word.count(wordUser[y])>0: #See if the number of same letters in the word the user guesses are greater than or equal to the number of letters given in the word 
          
          displayLetters=displayLetters+YELLOW+wordUser[y].upper()+LIGHT_GRAY #set the letters to yellow for the word  
        
        else: #if the number of letters in the guessed letter is 0 
           displayLetters=displayLetters+LIGHT_GRAY+wordUser[y].upper()+LIGHT_GRAY #set the letters to gray for the word        
      print(displayLetters) # print all of the letters in the word 
    print(LIGHT_PURPLE+"Oops! Sorry, but the correct answer was "+LIGHT_BLUE+word.upper()+LIGHT_PURPLE+". Hope you had fun playing! \n"+LIGHT_GRAY)  # print if they cannot get the word 
  #============================================GET THE INSTRUCTIONS==============================================
  elif userMenuInput==2:  
    help() #call the help function so that user can get instructions 
  elif userMenuInput==3: 
    print(LIGHT_CYAN+"Exiting the program. Have a nice day!! 🥳") #Exit program + message 
  #=======================================EXIT THE PROGRAM=============================================
  else: #ask for valid user input if they enter in anything else 
    print(LIGHT_RED+"Please enter in a valid input (1-3): "+LIGHT_GRAY) 
  











