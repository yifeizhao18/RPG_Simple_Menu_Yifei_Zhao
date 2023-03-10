#######################################################################################################
# Title: RPG Simple Menu

# Class: Computer Science 30 P1 S2                                                                                                                   
# Date: March 7th, 2023

# Coder's Name: Yifei Zhao                                                                                                            
# Version: 001                                                                                        
#######################################################################################################
'''
This program creates a small game menu. 
This program will ask for the user's name first. 
The program will print  print options for each category for user to choose from.
The user can choose to break/quit at any time, because quit is an option for all of the categories. \
If the user typed in something invalid, there will be instructions to guid the user to retype in a valid response.
It will use the if-elif-else, for, and while loops.
This program will run as along as the condition is True. 
'''
print("Welcome to the field.")
# possible selections under each categories the player can choose from
category = ["directions", "actions", "fight", "quit"]
directions = ["forward", "backward", "left", "right", "quit"]
actions = ["heal with medicine", "eat food", "build your own space", "move items around", "walk around", "quit"]
fight = ["shoot", "physical attack", "battle", "quit"]
# the statements that will be printed to the screen to ask for the user input 
categorySelection2 = ("Which category would you like to select? ")
directionSelection2 = ("Which direction would you like to go? ")
actionSelection2 = ("Which action would you like to perform? ")
fightSelection2 = ("Which fight movement would you like to perform? ")
endingStatement = ("Bye! See you soon! ")
# asks for the player and name and greeting the player 
characterName = input("What's your character name? ")
print('\n')
print(f"Hello {characterName}!")
# loop through the statements as long as the the condition is true
while True:
  print('\n')
  print("Possible Categories: ")
  # prints the main menu. The main menu includes the categories the user can choose from
  for option in category:
    print(f"- {option}")
    print('\n')
  categorySelection = input(categorySelection2)
  # prints the sub menu for directions if the user picked directions under the category. 
  if categorySelection == "directions":
    print('\n')
    print("Possible Directions:")
    # for each option in directions, do the following
    for selections in directions:
      print(f"- {selections}")
      print('\n')   
    directionSelection = input(directionSelection2)
    # it is going to do the following depending on what the user put down
    if directionSelection == "forward":
      print('\n')
      print("Go forward!")
    elif directionSelection == "backward":
      print('\n')
      print("Move backward!")
    elif directionSelection == "left":
      print('\n')
      print("Move to the left!")
    elif directionSelection == "right":
      print('\n')
      print("Move to the right!")
    elif directionSelection == "quit":
      print('\n')
      print(endingStatement)
      break
    else:
      print('\n')
      print("Invalid Action!")
      print("Please copy the word letter for letter under the possible choices!")
  # prints the sub menu for actions if the user chose actions under the category. 
  elif categorySelection == "actions":
    print('\n')
    print("Possible Actions: ")
    for action in actions:
      print(f"- {action}")
      print('\n')
    actionSelection = input(actionSelection2)
    # it is going to do the following depending on what the user put down
    if actionSelection == "heal with medicine":
      print('\n')
      print("Healing right now!")
    elif actionSelection == "eat food":
      print('\n')
      print("Eating!")
    elif actionSelection == "move items around":
      print('\n')
      print("Moving and collecting objects right now!")
    elif actionSelection == "build your own space":
      print('\n')
      print("Building your own house right now!")
    elif actionSelection == "walk around":
      print('\n')
      print("Walking around!")
    elif actionSelection == "quit":
      print('\n')
      print(endingStatement)
      break 
    else:
      print('\n')
      print("INVALID ACTION!")
      print("Please copy the word letter for letter under the possible choices!")
  # prints the sub menu for fight if the user picked fight under the category
  elif categorySelection == "fight":
    print('\n')
    print("Possible fight movements:")
    for attack in fight:
      print(f"- {attack}")
      print('\n')
    fightSelection = input(fightSelection2)
    # it is going to do the following depending on what the user put down
    if fightSelection == "shoot":
      print('\n')
      print("Shooting right now")
    elif fightSelection == "physical attack":
      print('\n')
      print("Physical attacking right now")
    elif fightSelection == "battle":
      print('\n')
      print("Currently battling with an enemy right now")
    elif fightSelection == "quit":
      print('\n')
      print(endingStatement)
      break
    else:
      print('\n')
      print("INVALID ACTION!")
      print("Please copy the word letter for letter under the possible choices!")
  # if the user answered 'quit' under the category section, do the following
  elif categorySelection == "quit":
    print('\n')
    print(endingStatement)
    break
  # if the user printed something invalid, do the following
  else:
    print('\n')
    print("INVALID ACTION!")
    print("Please copy the word letter for letter under the possible choices!")