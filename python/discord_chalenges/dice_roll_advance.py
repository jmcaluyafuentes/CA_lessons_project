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

    # Get int equivalent of s in ones, tens, hundreds and so on
    new_s = ''
    for num in s:

        # Check if s is valid
        try:
            num = int(num)
        except ValueError:
            print("s is invalid. Please follow nds format.")
            return None

        if int(s[0]) == 0:
            print("s is invalid. Please follow nds format.")
            return None

        new_s += str(num)

    s = int(new_s)

    # A list of random roll for each dice
    counter = 0
    rolls = []
    while counter < n:
        rolls.append(random.randint(1,s))
        counter += 1

    # Place the data of dice rolls in dict
    rolls_data = {}
    rolls_data['dice'] = rolls

    # Calculate sum of rolled dice
    sum_rolls = 0
    for num in rolls:
        sum_rolls += num
    rolls_data['total'] = sum_rolls
    
    # Get the max of rolled dice
    max_roll = 0
    for num in rolls:
        if num > max_roll:
            max_roll = num
    rolls_data['highest'] = max_roll

    print(rolls_data)

roll('2d6')
roll('3d10')
