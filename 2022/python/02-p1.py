import sys

# ROCK, PAPER, SCISSCORS
choices = [("A", "B", "C"), ("X", "Y", "Z")]
score = 0

with open(sys.argv[1], mode="r") as file:
    rounds = [(x.rstrip("\n")).split(" ") for x in file.readlines()]
    

for i in range(0, len(rounds)):
    p1 = choices[1].index(rounds[i][1])
    p2 = choices[0].index(rounds[i][0])
    
    ## draw
    if p1 == p2:
        score += (p1+1) + 3

    # lose
    elif p1 == (p2-1 % len(choices[0])) or p1 == (p2+2 % len(choices[0])):
        score += (p1+1)
        
    # win
    else:  # p1 == (p2+1 % len(choices[0])) or p1 == (p2-2 % len(choices[0])):
        score += (p1+1) + 6


print(score)

