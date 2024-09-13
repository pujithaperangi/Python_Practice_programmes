import random
import hangman_man

words=["touch","smell","light","taste","sound"]
x=random.choice(words)
choice=5
blank=len(x)

g=["_" for _ in range(len(x))]

print("welcome to Hangman Game")


#-->we can't use the for loop as there will be definite number of iterations for i in range(6):
game_over=False
while not game_over:
    guess = input("guess letter >").lower()
    for i in range(0,len(x)):
        if x[i] == guess :
            g[i]=guess

    print(g)

    if guess not in x:   # termination condition with resoect to choices left
        choice-=1
        if choice==0:
            game_over=True
            print("you lost!!")

    if "_" not in g:  # termination condition with respect to the blanks left
        game_over=True
        print("You win!!")
    print(hangman_man.man[choice])






















