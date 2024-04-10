import random


def main():
    questions = 10
    score = 0
    chances = 3
    lvl = get_level()
    while questions != 0:
        if chances == 3:
            x, y = generate_integer(lvl)
        try:
            player_answer = int(input(f"{x} + {y} = "))
            answer = x + y
            if player_answer == answer:
                questions = questions - 1
                score = score + 1
                chances = 3
                continue
            else:
                raise ValueError
        except (ValueError, NameError):
            print("EEE")
            chances = chances - 1
        if chances == 0:
            print((f"{x} + {y} = {answer}"))
            chances = 3
            questions = questions - 1
            continue
    print(f"Score: {score}")



def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if 1 <= n <= 3:
                return n
        except:
            pass



def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y



if __name__ == "__main__":
    main()

