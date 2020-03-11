#Create a RPS game where player can type r,p,s


import random

wins = 0
losses = 0
ties = 0

choices = ['r','p','s']

def compare_moves(user, cpu):
    wins = {"r":"s","s":"p","p":"r"}
    key,value = user, cpu
    if user == cpu:
        print("Tie!")
        return 0
    elif key in wins and value == wins[key]:
        print("Winner Winner Chicken Dinner!")
        return 1
    else:
        print("Losser!")
        return -1

#LOOP
while True:
    #Print
    print(f"Score: Wins:{wins} / Losses:{losses} / Ties:{ties}")
    #READ
    cmd = input("->")

    cpu_cmd = random.choice(choices)

    if cmd == "q":
        print("Goodbye!")
        break
    elif cmd in choices:
        result = compare_moves(cmd, cpu_cmd)
        if result == 1:
            wins += 1
        elif result == 0:
            ties += 1
        else:
            losses += 1
    else:
        print("Can not compute")

print("Thanks for Playing!")