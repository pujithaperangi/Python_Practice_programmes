# rock paper scissors
import random


def game(user,agent):
    if user==agent:
        print("draw")
    elif (user==0 and agent==2):
        print("you win")
    elif (user==2 and agent==0):
        print("agent win")
    elif user>agent:
        print("you win")
    elif user<agent:
        print("agent win")
    else:
        print("invalid input")
user=int(input(" enter o->rocks ,1-> papers ,2-> scissros\n>"))
agent=random.randint(0,2)
print(f'agent choice{agent}')
game(user,agent)
