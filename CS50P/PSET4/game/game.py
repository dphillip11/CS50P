import random

while True:
    try:
        n = int(input("Level: "))
        if n > 0:
            break
    except:
        pass

# avoid zero range
if n > 1:
    r = round(random.randrange(1,n))
else:
        r = 1
#dummy guess to avoid equality
guess = 'a'

while guess != r:
    try:
        #ensure guess is an integer
        guess = int(input("Guess: "))
        if guess < 1 or guess > n:
            # force error
            int(a)
        elif guess < r:
            print("Too small!")
        elif guess > r:
            print("Too large!")
        else:
            print("Just right!")
            break
    except:
        pass


