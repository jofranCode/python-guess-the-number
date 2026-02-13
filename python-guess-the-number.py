import random

attempt_count = 0
secret_number = random.randint(1, 20)

print("What is your name?")
user_name = input('-->')

print(f"Well, {user_name}, I'm thinking of a number between 1 and 20")

while attempt_count < 6:
    guess = int(input("Enter your guess\n-->"))
    attempt_count += 1
    
    if guess < secret_number:
        print("Your guess is too low")
    elif guess > secret_number:
        print("Your guess is too high")
    
    if guess == secret_number:
        break
        
if guess == secret_number:
    print(f"Good job, {user_name}! You guessed my number ({secret_number}) in {attempt_count} attempts")
elif guess != secret_number:
    print(f"Nope! The number I was thinking of was {secret_number}")