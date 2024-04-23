import random

def roll(nds):
    n, d, *s = nds

    # Check if n is valid
    if not n.isdigit():
        print("n is invalid. Please follow nds format.")
        return None

    # Check if n and d are valid
    n = int(n)
    if n == 0 or d != 'd':
        print("n or d is invalid. Please follow nds format.")
        return None

    new_s = ''
    for num in s:

        try:
            num = int(num)
        except ValueError:
            print("s is invalid. Please follow nds format.")
            return None

        new_s += str(num)

    s = int(new_s)

    counter = 0
    rolls = []
    while counter < n:
        rolls.append(random.randint(1,s))
        counter += 1

    print(rolls)

roll('2d6')
roll('3d10')
