import random
#Create lists
programming_languages = ["Python", "JavaScript", "C++", "Ruby", "Java"]
difficulty_levels = [1,2,3,4,5]
quiz_data = list(zip(programming_languages, difficulty_levels))
random.shuffle(quiz_data)
score = 0
for language, difficulty in quiz_data:
    guess = input(f"What is the difficulty level of {language}? Enter a number from 1 to 5")
    if guess == difficulty:
        print('Correct!')
        score +=1
    else:
        print(f"Incorrect you fucking idiot the right difficulty level of {language} is {difficulty}")
        print("\nQuiz Complete you stupid fuck. Final score:", score)    