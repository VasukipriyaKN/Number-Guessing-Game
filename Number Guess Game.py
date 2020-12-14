import time
import random

def countDown():
    print("\nThe game begins in")
    time.sleep(1)
    print("5")
    time.sleep(1)
    print("4")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("Go\n")
    time.sleep(0.5)

def hintGame(computerNumber,totalTime,score):
    if(computerNumber>=7 and computerNumber<=10):
        print("\nThe number is around to 10")
        userNumber = int(input("Guess the Number!...   "))
    elif(computerNumber>=1 and computerNumber<=4):
        print("\nThe number is around to 1")
        userNumber = int(input("Guess the Number!...   "))
    elif(computerNumber>4 and computerNumber<7):
        print("\nThe number is middle")
        userNumber = int(input("Guess the Number!...   "))

    if(computerNumber==userNumber):
        print("\nWOAH!.. You guessed it right")
        score = score + 5
    else:
        print("\nNO!... That's wrong")
        print("I guessed ",computerNumber,"\n")
        score = score - 5

class start():
    def __init__(self):
        countDown()
    def gameStart(self):
        times = 0
        score = 0
        while(times<5):
            computerNumber = random.randrange(1,11,1)
            beginTime = time.time()
            userNumber = int(input("\nGuess the Number!...   "))
            endTime = time.time()
            totalTime = endTime-beginTime
            if(userNumber==102):
                hintGame(computerNumber,totalTime,score)
                times +=1
            else:
                if(totalTime>10):
                    print("\nTimes up!...")
                    
                else:
                    if(computerNumber==userNumber):
                        print("Woah!.. You guessed it right")
                        score = score + 10
                    else:
                        print("\nNo!... That's wrong")
                        print("I guessed ",computerNumber,"\n")
                        score = score + 0
                
                time.sleep(2)
                times +=1
        if(score<0):
            print("Bursted!...")
            print("\nThe score is ",score)
        elif(score<25):
            print("\nWasted!...")
            print("\nThe score is ",score)
        elif(score==25):
            print("\nYou used lot of hints")
            print("\nThe score is ",score)
        else:
            print("\nGreat Job!...")
            print("\nThe score is ",score)
        print("................................\n")

print("Welcome to Number Guessing Game")
print("................................\n")
i = 0
while (i!=3):
    choiceInput = int(input("\n1. Start\n2. Help\n3. Exit\n"))
    if(choiceInput==1):
        startObject = start()
        startObject.gameStart()
        
    elif(choiceInput==2):
        print("\n...................................INSTRUCTIONS..........................................")
        print("1. This is to guess the number between 1 to 10.\n2. There will be 5 rounds, where you have to win minimum of 3 rounds.\n3. If you guessed the number correcty without hints you will be awarded 10 points.\n4. If you guessed the number correctly with hints, you will be awarded 5 points.\n5. If you guessed the number incorrectly with hints, you will be awarded -5 points.\n6. If you are unable to guess the number correctly you will be awarded 0 points.\n7. There will be 10 seconds to guess the number.\n8. Press '102' for hint.")
        print(".........................................................................................\n")
    
    elif(choiceInput==3):
        exit()