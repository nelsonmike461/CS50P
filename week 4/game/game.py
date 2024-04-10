import random

while True:
    try:
        level = int(input("Level: "))
        guess = random.randint(1, level)
        while True:
            play = int(input("Guess: "))
            if play > guess:
                print("Too large!")
            elif play < guess:
                print("Too small!")
            else:
                print("Just right!")
                raise EOFError
    except ValueError:
        pass
    except EOFError:
        break
