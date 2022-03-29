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
        
        if player_input == "help":
            print("You asked for help, but nobody came")
        
        elif player_input == "quit" or player_input == "exit":
            print(quit_message)
            play_again()
        else:
            print(unknown_input)


def play_again():
    yn = input("Play again? (yes/no) -> ")
    if yn == "yes":
        game_loop()
    else:
        print("Until next time, adverturer")
        exit(0)
