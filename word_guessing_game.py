import random

#Creating a word bank
hardware_list = ["CPU", "RAM", "Monitor", "Keyboard", "Mouse"]
software_list = ["Application", "Database", "Compiler", "Debugger", "Plugin"]
ai_list = ["Automation", "Inference", "Dataset", "Algorithm", "ChatGPT"]

#Creating a dictionary
hardware_dict = {"CPU": "The main unit where processing takes place.", "RAM": "Temporary storage for active tasks.", 
                 "Monitor": "Displays visual output from a computer.", "Keyboard": "Used to enter characters and commands",
                 "Mouse": "A pointing device used for navigation."}
software_dict = {"Application": "Software for performing specific functions.", "Database": "A structured collection of information.",
                 "Compiler": "Transforms code into executable programs", "Debugger": "Tool used to identify and fix errors in code.",
                 "Plugin": "An add-on that extends the functionality of software."}
ai_dict = {"Automation": "The use of technology to perform tasks with minimal human intervention.",
           "Inference": "The process of deriving conclusions from data or models.",
           "Dataset": "A collection of data used for analysis or training.",
           "Algorithm": "A set of rules or steps designed to perform a specific task.",
           "ChatGPT": "A conversational model developed for generating text-based responses."}
#Asking the user's name
name = input("What is your name? ")

#Specify the degree of difficulty of the game by the user
x = 3
while x > 0:
      x -= 1
      difficulty = int(input("\nSpecify the difficulty level of the game %s.\n Easy(1)\t Medium(2)\t Hard(3)\n Enter your difficulty number: " %name))
      if difficulty == 1:
            numـofـguesses = 16
            break
      elif difficulty == 2:
            numـofـguesses = 12
            break
      elif difficulty == 3:
            numـofـguesses = 8
            break
      else:
            print("\n\tPlease select one of the specified numbers!!!")
      if x == 0:
            exit()

#Specify the word category
y = 3
while y > 0:
      y -= 1
      category = int(input("\nPlease select your desired category for word guess %s.\n Computer Hardware(1)\t Computer Software(2)\t Computer AI(3)\n Enter your desired category number: " %name))
      if category == 1:
            word = hardware_list[random.randint(0, len(hardware_list)-1)]
            dict = hardware_dict
            break
      elif category == 2:
            word = software_list[random.randint(0, len(software_list)-1)]
            dict = software_dict
            break
      elif category == 3:
            word = ai_list[random.randint(0, len(ai_list)-1)]
            dict = ai_dict
            break
      else:
            print("\n\tPlease select one of the specified numbers!!!\n")
      if x == 0:
            exit()

#This variable is for counting the allowed number of guesses
counter = 0
#This is our made up word
made_up_word = ''

#Adding underlines and spaces for each letter of the word
i = 0
while i < len(word):
      made_up_word += '_'
      i += 1
made_up_word = ' '.join(made_up_word)

#This is a string to compare the guessed word with the selected word
Comparison_word = ' '.join(word)

print("\nThis is the word you have to guess:", made_up_word)

#This variable is for the guide
only_one_guide = 0

#Main
while counter < numـofـguesses:
      counter += 1
      if (counter % 4) == 0 and only_one_guide == 0:
            guide = int(input("Do you need any help?\t YES(1) or NO(0): "))
            if guide == 1:
                  only_one_guide += 1
                  print("\n\t", dict[word])

      guess = input("\nGuess the character: ")
      flag = False
      location=0
      #b for lower while
      b=0
      #c for upper while
      c=0
      right_counter = 0
      for char in word:
            if guess.lower() == char:
                  while b < len(word):
                        flag = True
                        location = (Comparison_word[location:].find(guess.lower())) + location
                        made_up_word = made_up_word[0:location] + guess.lower() + made_up_word[location+1:]
                        location += 1
                        b +=1
                  right_counter += 1
            elif guess.upper() == char:
                  while c < len(word):
                        flag = True
                        location = Comparison_word.find(guess.upper())
                        made_up_word = made_up_word[0:location] + guess.upper() + made_up_word[location+1:]
                        location += 1
                        c +=1
                  right_counter += 1
      print("You guessed %s word(s) right.\n" %right_counter)
      print(made_up_word)
      if flag == False:
            if counter < numـofـguesses:
                  print("WRONG! Please try again.")
            else:
                  print("YOU LOST THE GAME %s." %name)
      elif made_up_word == Comparison_word:
            print("Yes! You win the game %s." %name)
            break