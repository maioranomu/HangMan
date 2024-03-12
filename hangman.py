import pandas as pd
import random
import os
import time

attempts = 6
game = True
wordtheme = None
word = [""]
lettersused = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_word():
    global wordtheme
    global lettersused
    global word
    wordlist = pd.read_csv("Codes/PY/HangMan/wordlistbr.csv")
    wordindex = random.randint(0, len(wordlist) - 1)
    currentword = wordlist.iloc[wordindex, 0]
    wordtheme = wordlist.iloc[wordindex, 1]
    word = [currentword, wordtheme]
    
def check_attempts():
    global attempts
    attempts -= 1
    if attempts > 0:
        print(f"You have {attempts} attempts left")
    elif attempts == 0:
        clear_screen()
        hang_man()
        print(f"You have {attempts} attempts left. GAME OVER")
        print(f"The word was {word[0]}!")
        game_over()

def show_word():
    global word
    if word[0] == "":
        get_word()
    print("Word:")
    print("\n")
    for i in word[0]:
        if i.lower() not in lettersused:
            print("_", end = "")
        elif i.lower() in lettersused:
            print(i, end = "")
        else:
            print("ERROR")
    print("\n")
    print(f"Theme: {word[1]}")
    print("\n")
    print(f"Letters used: {lettersused}")

def get_try():
    loss = False
    guess = input("Guess a letter: ").lower()
    while guess in lettersused or len(guess) > 1 or guess == "":
        guess = input("Guess another letter: ")
    lettersused.append(guess)
    if guess.lower() not in word[0].lower():
        check_attempts()
        time.sleep(0.5)            
        

def game_over():
    global again
    global word
    global lettersused
    global game
    global attempts
    again = input("Do you want to play again? [y/n]: ").lower()
    word[0] = ""
    lettersused = []
    if again == "n":
        game = False
    else:
        attempts = 6


def check_if_won():
    global game
    global name
    global word
    global lettersused
    global points
    global attempts
    points = 1
    for i in word[0]:
        if i in lettersused:
            points += 1
            if points == len(word[0]):
                clear_screen()
                print("You Won!")
                print(f"The Word was {word[0]}")
                print(r"""
                        😎/  
                        /|
                        / \
                      
                        """)
                game_over()    

def hang_man():
    global attempts
    if attempts == 6:
        print(r"""
          
            ------|
            |     |
            |     |
            |    🙂
            |    /|\
            |    / \
            |
            |     
                
""")
    elif attempts == 5:
        print(r"""
          
            ------|
            |     |
            |     |
            |    🙁
            |    /|\
            |    / 
            |
            |     
                
""")
    elif attempts == 4:
        print(r"""
          
            ------|
            |     |
            |     |
            |    😥
            |    /|\
            |    
            |
            |     
                
""")
    elif attempts == 3:
        print(r"""
          
            ------|
            |     |
            |     |
            |    😓
            |    /|
            |    
            |
            |     
                
""")
    elif attempts == 2:
        print("""
          
            ------|
            |     |
            |     |
            |    😰
            |     |
            |    
            |
            |     
                
""")

    elif attempts == 1:
        print("""
          
            ------|
            |     |
            |     |
            |    😨
            |    
            |     
            |
            |     
                
""")
    elif attempts == 0:
        print("""
          
            ------|
            |     |
            |     |
            |     
            |    
            |    
            |
            |     
                
""")                


def game():
    clear_screen()
    show_word()
    # print(word[0])
    hang_man()
    get_try()
    check_if_won()
    time.sleep(0.2)
    clear_screen()


while game:
    game()
    
    
input("")