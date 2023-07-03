import random

option = ['rock' , 'paper' , 'scissor']
scores = {'user':0 , 'computer':0}
def win_check(user , computer):
    if (user == 'rock' and computer == 'scissor') or (user == 'paper' and computer == 'rock') or (user == 'scissor' and computer == 'paper'):
        print("you win!")
        scores['user']+=1
    elif user == computer:
        print("Tie!")
    else:
        print("computer wins!")
        scores['computer']+=1

def score():
    if scores['user'] > scores['computer']:
        print('you win all! total wins: ' , scores['user'])
    elif scores['computer'] > scores['user']:
        print('computer wins all! total wins: ' , scores['computer'])
    else:
        print("Tie! no one wins")

def main():
    print("game begins!")

    while True :
        user_choice = input("what's your choice? ")
        if user_choice == 'exit':
            score()
            print("thanks for playing!")
            exit()
        else:
            comp_choice = random.choice(option)
            win_check(user_choice,comp_choice)


print("welcome to Rock,Paper,Scissor! for exiting the program just type exit.")
main()