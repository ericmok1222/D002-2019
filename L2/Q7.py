#L2 Q6: Banana Guessing game

#Step 1: Import necessary modules
import random
#Step 2: Welcome Message
print('''Welcome to the Banana Guessing Game
Dave hid some bananas. Your task is to find out the number of bananas he hid.''')
#Step 3: Choose a random number between 1-100
n = random.randint(1,100)
print ("shhh, Dave hides %s bananas" % n)
# define a flag for found/not found and counter on how many trials

#Step 4: Give three chances to the players 
while True:
    guess=int(input("Player1 input a number between 1 and 100\n"))
    if guess>100:
        print("wrong input")
    elif guess==n:
        found=1
        break
    if guess<n:
        print("you guess too low")
    elif guess>n:
        print("you guess too high")
    guess=int(input("Player2 input a number between 1 and 100\n"))
    if guess>100:
        print("wrong input")
    elif guess==n:
        found=2
        break
    if guess<n:
        print("you guess too low")
    elif guess>n:
        print("you guess too high")
    
            

#Step 5: Display a message
if found == 1:
        print('player1 got the correct guess ' )
        print('Dave\'s banana are now all yours!')
else:
        print('player2 got the correct guess' )
        print('Dave\'s banana are now all yours!')
