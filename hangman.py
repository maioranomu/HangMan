import pandas as pd
import random
import os
import time

language = "BR"
listpath = f"HangMan\wordlists\wordlist{language}.csv"

game = True
wordtheme = None
word = [""]
lettersused = []
difficulty = ""

def ask_difficulty():
    global difficulty
    global attempts
    global maxattempts
    difficultylist = ["1", "2", "3"]
    if difficulty == "":
        
        while difficulty not in difficultylist:
            
            difficulty = input("What difficulty would you like to play? [1 | 2 | 3] ")
            if difficulty == "1":
                attempts = 10
                maxattempts = attempts
            elif difficulty == "2":
                attempts = 6
                maxattempts = attempts
            elif difficulty == "3":
                attempts = 2
                maxattempts = attempts


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_word():
    global wordtheme
    global lettersused
    global word
    wordlist = pd.read_csv(listpath)
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
        print(f"You have {attempts} attempts left.")
        print(f"The word was {word[0]}!")
        print("\n")
        game_over()

def show_word():
    global word
    if word[0] == "":
        get_word()
    print("Word:")
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
    capitallettersused = [char.upper() for char in lettersused]
    print(f"Attempts left: {attempts}")
    print(f"Letters used: {("  ".join(capitallettersused))}")
    print("\n")

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
    global difficulty
    global attempts
    again = " "
    againlist = ["", "c", "q"]
    word[0] = ""
    lettersused = []
    
    while again not in againlist:
        again = input("[PRESS ENTER TO CONTINUE] [PRESS C TO CHANGE DIFFICULTY] [PRESS Q TO QUIT]").lower()

    if again == "":
        attempts = maxattempts
        
    elif again == "q":
        game = False
        
    elif again == "c":
        clear_screen()
        difficulty = ""
        ask_difficulty()

def check_if_won():
    global game
    global name
    global word
    global lettersused
    global points
    global attempts
    points = 0
    for i in word[0]:
        if i.lower() in lettersused:
            points += 1
        if points == len(word[0]):
            clear_screen()
            print("You Won!")
            print(f"The Word was {word[0]}")
            print("\n")
            print(r"""
                    😎/  
                    /|
                    / \
                    
                    """)
            game_over()    

def hang_man():
    global attempts
    attemptsafter6 = attempts - 6
    printextra = "*" * attemptsafter6
    
    if attempts > 6: #🙂
        print(r"""
              
            _________
            | /     |    
            |/      |
            |      🙂  {0}
            |      /|\
            |      / \     
            |          
            |
                          
""".format(printextra))
        
    elif attempts == 6: #🙂
        print(r"""
              
            _________
            | /     |    
            |/      |
            |      🙂
            |      /|\
            |      / \     
            |          
            |
                 
""")
    elif attempts == 5: #🙁
        print(r""" 
              
            _________
            | /     |    
            |/      |
            |      🙁 
            |      /|\
            |      /   
            |          
            |
                
""")
    elif attempts == 4: #😥
        print(r"""
              
            _________
            | /     |    
            |/      |
            |      😥 
            |      /|\
            |      
            |          
            |
        
""")
    elif attempts == 3: #😓
        print(r"""
              
            _________
            | /     |    
            |/      |
            |      😓 
            |      /|
            |        
            |          
            |
         
""")
    elif attempts == 2: #😰
        print(r"""
              
            _________
            | /     |    
            |/      |
            |      😰 
            |       |
            |        
            |          
            |
          
""")

    elif attempts == 1: #😨
        print(r"""
              
            _________
            | /     |    
            |/      |
            |      😨 
            |      
            |        
            |          
            |
         
""")
    elif attempts == 0: #💀
        print(r"""
          
              
            _________
            | /     |    
            |/      |
            |      
            |      
            |       
            |          
            |
                   💀 
            
                Game Over!
                
""")
    else:
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
    show_word()


def game():
    clear_screen()
    ask_difficulty()
    clear_screen()
    hang_man()
    print(word[0])
    get_try()
    check_if_won()
    time.sleep(0.2)
    clear_screen()


while game:
    game()
    
    
input("")
