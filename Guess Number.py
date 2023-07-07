# First game
# Concept : TO Guess A Random Number In Some Range
import random,time

def fun():
    a,b=input('Enter a range of numbers in which you are going to guess ( Example: 1 100): ').split()
    a,b=int(a),int(b)
    r=random.randint(a,b)
    
    for i in range(3,0,-1):
        print(i)
        time.sleep(1)
    
    print('\nSTART !!!!')
        
    
    print('\nGuess a number between',a,"-",b,"\nNOTE:End points are included")
    while True:
        x=int(input("Take a guess : "))
        if (r==x):
            break
        elif (x>r):
            print("Your Guess is HIGH than required !")
        else:
            print("Your Guess is LOW than required !")
    print("YOU WON THE GAME !!!!!!\n\n")
    s=input("Enter 'Y' to play again : ")
    if s== "y" or "Y":
        fun()
    else:
        exit()
    

n=input("HELLO!, Your Good Name Please :")
print("Hi "+n+". Good luck !")
fun()
