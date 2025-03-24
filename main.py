import random

lower_bound = 1
upper_bound = 100
number_of_guesses = 0

random_number = random.randint(lower_bound, upper_bound)

guess = int(input("Guess the number: "))

while guess != random_number:
    if guess < random_number:
        print("The number is higher!")
    else:
        print("The number is lower!")
        
    number_of_guesses += 1
    guess = int(input("Guess the number: "))

print("Congratulations! You guessed the number correctly in", number_of_guesses, "attempts.")


Guess the number: 50
The number is higher!
Guess the number: 75
The number is lower!
Guess the number: 60
The number is higher!
Guess the number: 65
The number is higher!
Guess the number: 69
The number is lower!
Guess the number: 68
The number is lower!
Guess the number: 67
Congratulations! You guessed the number correctly in 6 attempts.
