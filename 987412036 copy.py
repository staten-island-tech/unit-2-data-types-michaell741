import random
random_number = random.randint(1, 100)
guess_history = []

while True:
    guess = int(input('what is your guess?')) 
    guess_history.append(guess)
    if guess == random_number:
            print ('Congrats, your guess was correct!')
    else:
            if guess > random_number:
                print ('guess lower')
            else:
                print ('guess higher')  
    print (f'this is your guess history {guess_history}')