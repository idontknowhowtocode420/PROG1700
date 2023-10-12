import random


randomnum = random.randint(1,10)
name = None 

while True:
    name = input('Hello! What is your name!:')
    if name.isdigit():
        print("Please enter a valid name")

    else:
    
        break



while True:
    if name.isalpha():    
        trys = 1

    guess = int(input(f'Hi {name} Please guess a number between 1 and 10:'))

    while trys < 5:
        guess = int(input(f'{name} You have used {trys} guesses out of 5! Please enter another guess: '))
    if trys == 5:
        print(f'{name} You ran out of guesses! The number was: {randomnum}')
        break   
    if guess == randomnum:
        print(f' Congrats {name} guessed the number {randomnum} in {trys} tries!') 
        break   
    if guess < randomnum:
        print("The Number is higher")
        trys += 1
        if trys == 5:
            print(f'{name} You ran out of guesses! The number was: {randomnum}')
    else:
        print('The number is lower')
        trys += 1
        if trys == 5:
            print(f'{name} You ran out of guesses! The number was: {randomnum}')
else:
    
    print("Please enter valid name")           