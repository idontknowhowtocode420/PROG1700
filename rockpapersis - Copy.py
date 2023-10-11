import random
Rock = 1
Paper = 2 
Scissors = 3

while True:
    user_input = input("1 for rock 2 for paper 3 for scissors:")
    if user_input.isalpha():
        print('Please input a valid number')
    
        if user_input.isdigit():  
            user_input = int(user_input)
            if user_input <=3 and user_input >=1:
                rng_value = random.randrange(1,4,1)
            
                if user_input == rng_value:

                    print("It's a tie!")

                elif ((user_input == 1 and rng_value == 3) or (user_input == 2 and rng_value == 1) or (user_input == 3 and rng_value == 2)):

                    print("You win")

                else:

                    print("BOT wins!")

              