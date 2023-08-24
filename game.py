def display_game(game_list):
    print("Here is the current list:")
    print(game_list)


def position_choice():
    choice = 'wrong'
    while choice not in ['0', '1', '2']:
        choice = input("Please pick a position (0,1,2):")

        if choice not in ['0', '1', '2']:
            print("Wrong Input!")

    return int(choice)
    
def replacement_choice(game_list, position):
    user_placement = input("Type a string to replace in the position:")

    game_list[position] = user_placement

    return game_list


def game_on_choice():
    choice = 'wrong'

    while choice not in ['Y', 'N']:
        choice = input("Keep Playing? Y or N:")

        if choice not in ['Y', 'N']:
            print("Wrong Input!")

    if choice == 'Y':
        return True
    else:
        False


game_on = True
game_list = [0, 1, 2]

while game_on:

    display_game(game_list)
    position = position_choice()
    game_list = replacement_choice(game_list, position)
    display_game(game_list)
    game_on = game_on_choice()
