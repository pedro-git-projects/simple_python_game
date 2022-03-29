separator = "                                               "
welcome_text = """
The village of Honeywood has been terrorized by strange, deadly creatures for months now. Unable to endure any 
longer, the villagers pooled their wealth and hired the most skilled adventurer they could find: you. After
listening to their tale of woe, you agree to enter the labyrinth where most of the creatures seem to originate,
and destroy the foul beasts. Armed with a longsword and a bundle of torches, you descend into the labyrinth, 
ready to do battle....

""" 
unknown_input ="I'm, not sure what you mean... type help for help." 
quit_message = "Overcome with terror, you flee the dungeon and are forever branded a coward."
help_text = """Enter a command: 
    - n/s/e/w - move in a direction
    - map - show a map of the labyrinth
    - look - look around and describe your environment
    - equip <item> - use an item from your inventory
    - unequip <item> - stop using an item from your inventory
    - fight - attack a foe
    - examine <object> - examine an object more closely
    - get <item> - pick up an item
    - drop <item> - drop an item
    - rest - restore some health by resting
    - inventory - show your inventory
    - status - show current player status
    - quit - end the game"
"""

def welcome():
    print(separator, "DUNGEON")
    print(welcome_text)


def game_loop():
    welcome()
    input("Press ENTER to continue:")
    explore_labirynth()


   
def explore_labirynth():
    while True:
        player_input = input("-> ")
        player_input = sanitize_input(player_input)
        
        if player_input == "help":
            show_help()
        
        elif player_input == "quit" or player_input == "exit":
            print(quit_message)
            play_again()
        else:
            print(unknown_input)


def show_help():
    print(help_text)


def sanitize_input(user_input:str) -> str:
   return user_input.lower().strip() 



def get_yn(question:str) -> str:
    while True:
        awnser = input(question + " (yes/no) -> ")
        awnser = sanitize_input(awnser)
        if awnser not in ["yes", "no", "y", "n"]:
            print("Please enter yes or no.")
        else:
            if awnser == "y":
                awnser = "yes"
            elif awnser == "n":
                awnser = "no"
        return awnser


def play_again():
    yn = get_yn("Play again?") 
    if yn == "yes":
        game_loop()
    elif yn == "no":
        print("Until next time, adverturer")
        exit(0)

