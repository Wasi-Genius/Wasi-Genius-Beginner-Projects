import random
import climage
from Util import point_grammar
import warnings

warnings.filterwarnings("ignore")

Rock_Image = climage.convert(r'C:\PythonProjectsWasiG\RockPaperScissorsGame\rock_image.png', False, True, False)
scissors_Image = climage.convert(r'C:\PythonProjectsWasiG\RockPaperScissorsGame\sciccors_image.png', False, True, False)
Paper_Image = climage.convert(r'C:\PythonProjectsWasiG\RockPaperScissorsGame\paper_image.png', False, True, False)

print('Welcome to the rock, paper, scissors game! Lets get started!')
name = input('What is your name?: ')


def check_if_tied(user_selection, opp_choice):
    if (user_selection == 'rock' or user_selection == 'ROCK' or user_selection == 'Rock') and opp_choice == 1:
        return True
    elif (user_selection == 'scissors' or user_selection == 'SCISSORS' or user_selection == 'Scissors') and opp_choice == 2:
        return True
    elif (user_selection == 'paper' or user_selection == 'PAPER' or user_selection == 'Paper') and opp_choice == 3:
        return True
    else:
        return False


def check_if_won(user_selection, opp_choice):
    if (user_selection == 'rock' or user_selection == 'ROCK' or user_selection == 'Rock') and opp_choice == 2:
        return True
    elif ( user_selection == 'scissors' or user_selection == 'SCISSORS' or user_selection == 'Scissors') and opp_choice == 3:
        return True
    elif (user_selection == 'paper' or user_selection == 'PAPER' or user_selection == 'Paper') and opp_choice == 1:
        return True
    else:
        return False


def get_user_image(user_selection):
    if user_selection == 'rock' or user_selection == 'ROCK' or user_selection == 'Rock':
        return Rock_Image
    elif user_selection == 'scissors' or user_selection == 'SCISSORS' or user_selection == 'Scissors':
        return scissors_Image
    else:
        return Paper_Image


def get_robot_image(robot_selection):
    if robot_selection == 1:
        return Rock_Image
    elif robot_selection == 2:
        return scissors_Image
    else:
        return Paper_Image


rounds = 0
score = 0
robot_score = 0
while rounds < 3:
    user_choice = input(f'Okay {name}, rock, paper, or scissors?: ')
    opponent_choice = random.randint(1, 3)
    if check_if_tied(user_choice, opponent_choice):
        print(get_user_image(user_choice))
        print('Vs\n')
        print(get_robot_image(opponent_choice))
        print("You tied!")
        rounds += 1
    elif check_if_won(user_choice, opponent_choice):
        print(get_user_image(user_choice))
        print('Vs\n')
        print(get_robot_image(opponent_choice))
        print("You win!")
        rounds += 1
        score += 1
    else:
        print(get_user_image(user_choice))
        print('Vs\n')
        print(get_robot_image(opponent_choice))
        print("You lose!")
        rounds += 1
        robot_score += 1

if score > robot_score:
    print(f'You won! You got {score} {point_grammar(score)} while the robot got {robot_score} {point_grammar(robot_score)}.')
elif score == robot_score:
    print(f'You tied with the robot. Both of you had {score} {point_grammar(score)}')
else:
    print(f"Wump, wump, you lost! You scored {score} {point_grammar(score)} while the robot scored {robot_score} {point_grammar(robot_score)}. Better luck next time!")
