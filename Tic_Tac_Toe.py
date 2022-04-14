from itertools import count
import random
import datetime
from typing import Counter

#tabe chaaap safheye bazi
def show_game_board():
    for i in range(3):
        for j in range(3):
            print(game[i][j],end=" ")
        print()

#tabe check shart bord
def check():
    #bazikon aval...
    #barresi satr ha
    for i in range(3):
        if game[i][0]==game[i][1]==game[i][2]=='❌':
            print("Player1 wins!")
            endTime=datetime.datetime.now()
            print("Time is:",endTime-start_time)
            exit()

    #barresi sotun ha
    for i in range(3):
        if game[0][i]==game[1][i]==game[2][i]=='❌':
            print("Player1 wins!")
            endTime=datetime.datetime.now()
            print("Time is:",endTime-start_time)
            exit()

    #barresi qotrha
    if game[0][0]=='❌' and game[1][1]=='❌' and game[2][2]=='❌':
        print("Player1 wins!")
        endTime=datetime.datetime.now()
        print("Time is:",endTime-start_time)
        exit()
    if game[0][2]=='❌' and game[1][1]=='❌' and game[2][0]=='❌':
        print("Player1 wins!")
        endTime=datetime.datetime.now()
        print("Time is:",endTime-start_time)
        exit()
    
    #bazikon dovom...
    #barresi satr ha
    for i in range(3):
        if game[i][0]==game[i][1]==game[i][2]=='⭕':
            print("Player2 wins!")
            endTime=datetime.datetime.now()
            print("Time is:",endTime-start_time)
            exit()

    #barresi sotun ha
    for i in range(3):
        if game[0][i]==game[1][i]==game[2][i]=='⭕':
            print("Player2 wins!")
            endTime=datetime.datetime.now()
            print("Time is:",endTime-start_time)
            exit()

    #barresi qotrha
    if game[0][0]=='⭕' and game[1][1]=='⭕' and game[2][2]=='⭕':
        print("Player2 wins!")
        endTime=datetime.datetime.now()
        print("Time is:",endTime-start_time)
        exit()
    elif game[0][2]=='⭕' and game[1][1]=='⭕' and game[2][0]=='⭕':
        print("Player2 wins!")
        endTime=datetime.datetime.now()
        print("Time is:",endTime-start_time)
    
    #shart tasavi
    elif Count==9:
        print("no ones win!")
        endTime=datetime.datetime.now()
        print("Time is:",endTime-start_time)
        exit()
    
###########

print("choose one the options:\n1.Single player\n2.Double player")
choice=int(input("-->"))

#chaap safheye bazi
game = [['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']]

Count=0

#single Player
if choice==1:
    start_time=datetime.datetime.now()
    show_game_board()

    while True:

         #ta zamani ke bazikon entekhab dorost dashte bashad
        while True:
            #entekhab bazikon 
            print("Player")
            row=int(input("row:"))
            col=int(input("col:"))

            #check mojaz budan shomareye satr va sotun
            if 0<=row<=2 and 0<=col<=2:
                #check khali budn khane
                if game[row][col]=='-':
                    game[row][col]='❌'
                    Count+=1
                    break
                else:
                    print("Not empty! try again.")
            else:
                print("Out of range(0,2)!")

        show_game_board()
        check()
        

        #ta zamani ke Computer entekhab dorost dashte bashad
        while True:
            #entekhab Computer
            print("Computer")
            row=random.randint(0,2)
            col=random.randint(0,2)

            #check khali budn khane
            if game[row][col]=='-':
                game[row][col]='⭕'
                Count+=1
                break
            else:
                print("Not empty! try again.")
        
        show_game_board()
        check()
        

#Double Player
elif choice==2:
    start_time=datetime.datetime.now()
    show_game_board()
    while True:

        #ta zamani ke bazikon entekhab dorost dashte bashad
        while True:
            #entekhab bazikon aval
            print("Player1")
            row=int(input("row:"))
            col=int(input("col:"))

            #check mojaz budan shomareye satr va sotun
            if 0<=row<=2 and 0<=col<=2:
                #check khali budn khane
                if game[row][col]=='-':
                    game[row][col]='❌'
                    Count+=1
                    break
                else:
                    print("Not empty! try again.")
            else:
                print("Out of range(0,2)!")

        show_game_board()
        check()
        

        #ta zamani ke bazikon entekhab dorost dashte bashad
        while True:
            #entekhab bazikon dovom
            print("Player2")
            row=int(input("row:"))
            col=int(input("col:"))

            #check mojaz budan shomareye satr va sotun
            if 0<=row<=2 and 0<=col<=2:
                #check khali budn khane
                if game[row][col]=='-':
                    game[row][col]='⭕'
                    Count+=1
                    break
                else:
                    print("Not empty! try again.")
            else:
                print("Out of range(0,2)!")

        show_game_board()
        check()