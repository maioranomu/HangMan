import pandas as pd
import random
import os
import time
from hangsprites.hangdict import greater_6, sprites

language = "BR"
listpath = f"E:\Importante\Codes\MyCodes\PY\PROJECTS\HangMan\wordlists\wordlist{language}.csv"
datapath = "E:\Importante\Codes\MyCodes\PY\PROJECTS\HangMan\data\data.txt"
losses = 0
wins = 0
game = True
wordtheme = None
word = [""]
lettersused = []
difficulty = ""



def dataup(result):
    global losses
    global wins
    with open(datapath, "r") as f:
        lines = f.readlines()
        for line in lines:
            if "Losses" in line:
                losses = int(line.split(":")[1].strip())
            elif "Wins" in line:
                wins = int(line.split(":")[1].strip())
    
    if result == "win":
        wins += 1
    elif result == "lose":
        losses += 1
    
    with open(datapath, "w") as f:
        f.write(f"""
Losses: {losses}
Wins: {wins}
""")
    return losses, wins

def ask_difficulty():
    global difficulty
    global attempts
    global maxattempts
    difficultylist = ["1", "2", "3", "4"]

    while difficulty not in difficultylist:
        clear_screen()
        difficulty = input(f"""What difficulty would you like to play?  [1 | 2 | 3 | 4] 
                                          (10, 8, 6, 1)\n
                            """)
        
    if difficulty == "1":
        attempts = 10
    
    elif difficulty == "2":
        attempts = 8
    
    elif difficulty == "3":
        attempts = 6
    
    elif difficulty == "4":
        attempts = 1
        
    maxattempts = attempts


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_word():
    global lettersused
    global word
    wordlist = pd.read_csv(listpath)
    wordindex = random.randint(0, len(wordlist) - 1)
    currentword = wordlist.iloc[wordindex, 0]
    wordtheme = wordlist.iloc[wordindex, 1]
    word = [currentword, wordtheme]
    
def check_attempts():
    global attempts
    global maxattempts
    attempts -= 1

    if attempts == 0:
        clear_screen()
        hang_man()
        print(f"You have {attempts} attempts left.")
        print(f"The word was {word[0]}!")
        dataup("lose")
        print("\n")
        game_over()
    
    if attempts < 0:
        attempts = maxattempts


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
    global datapath
    global lettersused
    global game
    global difficulty
    global attempts
    again = " "
    againlist = ["", "c", "q", "i"]
    word[0] = ""
    lettersused = []
    
    while again not in againlist:
        again = input("[PRESS ENTER TO CONTINUE] [PRESS C TO CHANGE DIFFICULTY] [PRESS Q TO QUIT] [I INFO]\n").lower()

    if again == "":
        attempts = maxattempts
        
    elif again == "q":
        game = False
        
    elif again == "c":
        clear_screen()
        difficulty = ""
        ask_difficulty()
        
    elif again == "i":
        attempts = maxattempts
        clear_screen()
        ask_difficulty()
        attempts = maxattempts            
        with open (datapath, "r") as f:
            lines = f.readlines()
            for line in lines:
                if "Losses" in line:
                    losses = int(line.split(":")[1].strip())
                    print("Losses:", losses)
                elif "Wins" in line:
                    wins = int(line.split(":")[1].strip())
                    print("Wins:", wins)
        input("")
        attempts = maxattempts
               

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
            dataup("win")
            print(f"The Word was {word[0]}")
            print("\n")
            print(sprites["10"])
            game_over()    

def hang_man():
    global attempts
    attemptsafter6 = attempts - 6
    printextra = "*" * attemptsafter6
    
    if attempts > 6: #😁
        greater_6(printextra)
        
    elif attempts == 6: #🙂
        print(sprites["6"])
        
    elif attempts == 5: #🙁
        print(sprites["5"])
        
    elif attempts == 4: #😥
        print(sprites["4"])
        
    elif attempts == 3: #😓
        print(sprites["3"])
        
    elif attempts == 2: #😰
        print(sprites["2"])
        
    elif attempts == 1: #😨
        print(sprites["1"])      
        
    elif attempts <= 0: #💀
        print(sprites["0"])       
            
    show_word()



import pandas as pd
import random
import os
import time
from hangsprites.hangdict import greater_6, sprites

language = "BR"
listpath = f"E:\Importante\Codes\MyCodes\PY\PROJECTS\HangMan\wordlists\wordlist{language}.csv"
datapath = "E:\Importante\Codes\MyCodes\PY\PROJECTS\HangMan\data\data.txt"
losses = 0
wins = 0
game = True
wordtheme = None
word = [""]
lettersused = []
difficulty = "3"



def dataup(result):
    global losses
    global wins
    with open(datapath, "r") as f:
        lines = f.readlines()
        for line in lines:
            if "Losses" in line:
                losses = int(line.split(":")[1].strip())
            elif "Wins" in line:
                wins = int(line.split(":")[1].strip())
    
    if result == "win":
        wins += 1
    elif result == "lose":
        losses += 1
    
    with open(datapath, "w") as f:
        f.write(f"""
Losses: {losses}
Wins: {wins}
""")
    return losses, wins

def ask_difficulty():
    global difficulty
    global attempts
    global maxattempts
    difficultylist = ["1", "2", "3", "4"]

    while difficulty not in difficultylist:
        clear_screen()
        difficulty = input(f"""What difficulty would you like to play?  [1 | 2 | 3 | 4] 
                                        (10, 8, 6, 1)\n
                            """)
        
    if difficulty == "1":
        attempts = 10
    
    elif difficulty == "2":
        attempts = 8
    
    elif difficulty == "3":
        attempts = 6
    
    elif difficulty == "4":
        attempts = 1
        
    maxattempts = attempts


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_word():
    global lettersused
    global word
    wordlist = pd.read_csv(listpath)
    wordindex = random.randint(0, len(wordlist) - 1)
    currentword = wordlist.iloc[wordindex, 0]
    wordtheme = wordlist.iloc[wordindex, 1]
    word = [currentword, wordtheme]
    
def check_attempts():
    global attempts
    global maxattempts
    attempts -= 1

    if attempts == 0:
        clear_screen()
        hang_man()
        print(f"You have {attempts} attempts left.")
        print(f"The word was {word[0]}!")
        dataup("lose")
        print("\n")
        attempts -= 1
        game_over()
    
    if attempts < 0:
        attempts = maxattempts

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
    global datapath
    global lettersused
    global game
    global difficulty
    global attempts
    again = " "
    againlist = ["", "c", "q", "i"]
    word[0] = ""
    lettersused = []
    
    while again not in againlist:
        again = input("[PRESS ENTER TO CONTINUE] [PRESS C TO CHANGE DIFFICULTY] [PRESS Q TO QUIT] [I INFO]\n").lower()

    if again == "":
        attempts = maxattempts
        
    elif again == "q":
        game = False
        
    elif again == "c":
        clear_screen()
        difficulty = ""
        ask_difficulty()
        
    elif again == "i":
        clear_screen()
        with open (datapath, "r") as f:
            lines = f.readlines()
            for line in lines:
                if "Losses" in line:
                    losses = int(line.split(":")[1].strip())
                    print("Losses:", losses)
                elif "Wins" in line:
                    wins = int(line.split(":")[1].strip())
                    print("Wins:", wins)
        input("")  
        attempts = maxattempts

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
            dataup("win")
            print(f"The Word was {word[0]}")
            print("\n")
            print(sprites["10"])
            game_over()    

def hang_man():
    global attempts
    attemptsafter6 = attempts - 6
    printextra = "*" * attemptsafter6
    
    if attempts > 6: #😁
        greater_6(printextra)
        
    elif attempts == 6: #🙂
        print(sprites["6"])
        
    elif attempts == 5: #🙁
        print(sprites["5"])
        
    elif attempts == 4: #😥
        print(sprites["4"])
        
    elif attempts == 3: #😓
        print(sprites["3"])
        
    elif attempts == 2: #😰
        print(sprites["2"])
        
    elif attempts == 1: #😨
        print(sprites["1"])      
        
    elif attempts <= 0: #💀
        print(sprites["0"])       
            
    show_word()

def game():
    clear_screen()
    
    ask_difficulty()
    game_over()
    clear_screen()
    
    while game:
        clear_screen()
        hang_man()
        print(word[0])
        get_try()
        check_if_won()
        if not game:
            break
    
    input("")

game()
