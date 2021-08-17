#!/usr/bin/env python
# coding: utf-8

# # Assignment 1

# # Hangman

# In[10]:


import random
loop=1
while loop==1:
    print("Welcome To The Word Guessing Game \nEnjoy Your Game \n")
    heart = '\u2764\uFE0F'
    print("CHOICE:- \nPress 1 For 1 Players \nPRESS 2 for 2 Player\n")
    choice = int(input())
    if choice == 2:#player vs player game
        word = input("Player 1 Enter Your Word \n")
    elif choice == 1:#player vs computer game
        words=['computer','whiteboard','programmer','python','import','variable','keywords','datatype','dictionary','mapping','strings','operators','functions','regression','methods','random','comments']
        word=random.choice(words)
    else:
        print("You had made a wrong choice")
        break
    space=['_']*len(word)
    print(space)

    # create a function
    def get_letter(guess,word,space):  
        index = -2
        while index != -1:
            if guess in word:
                index=word.find(guess)
                remove='*'
                word=word[:index]+remove+word[index+1:]
                space[index] = guess
            else:
                index=-1 


        return(word,space)


    # create a function to check if the user guess all the letters in the word

    def win():
        for i in range(0,len(space)):
            if space[i] == '_':
                return -1
        return 1

    # choose some number of turn for the user to guess the word 
    turn= 9
    while turn>0:
        print('lives left :- '+ heart*turn)
        turn = turn-1
        guess = input("guess the character : ")
        if(turn == 1):
            print("This is your last turn" )
        if guess in word:
            word,space=get_letter(guess,word,space)
            print(space)
        else:
            print('sorry letter not found in word')

        if win()==1:
            print('congratulations! you won the game')
            break

        print()
    if(turn == 0):
        print('You Lost the game, Better Luck Next Time')
    print("Do you want to play game again or quit \nPress :- \n1 for YES \n2 for NO")
    loop=int(input())
print('Thankyou for playing this game \nWe Hope You Enjoy Your Game')

