#This are my second github repo
#Practice gets you one step forward into your goal


import random

actual_number = random.randint(1,10)
print(actual_number)
attempts = 0

while True:
    attempts += 1
    choice = int(input("Please enter your guess number: "))
    if actual_number < choice:
        print("Your guessed was greater than on the actual number")
    elif actual_number > choice:
        print("Your guessed was less than on the actual number")
    else:
        print("The actual number was",str(actual_number)+ ". Your guess is",str(choice)+". You have the actual number")
        print("It takes you",str(attempts)+" times to get the actual number")
        break
print("")
print("Thanks for GUESSING")