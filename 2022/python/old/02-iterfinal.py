import sys


# ROCK, PAPER, SCISSCORS
choices = [("A", "B", "C"), ("X", "Y", "Z")]
key = ["Rock", "Paper", "Scissors"]


with open(sys.argv[1], mode="r") as file:
    rounds = [(x.rstrip("\n")).split(" ") for x in file.readlines()]

score = 0
counter = 0
c = 0

win = lose = draw = 0


for i in range(0, len(rounds)):
    p1 = choices[1].index(rounds[i][1])
    p2 = choices[0].index(rounds[i][0])
    

    ## draw
    #print(f"{ply1Choice} : {ply2Choice}")
    if p1 == p2:
        print(f"draw - {key[p1]} : {key[p2]}")
        draw += 1
        score += (p1+1) + 3

    # lose
    elif p1 == (p2-1 % len(choices[0])) or p1 == (p2+2 % len(choices[0])):
        print(f"lose - {key[p1]} : {key[p2]}")
        lose += 1
        score += (p1+1)
    
    elif p1 == (p2+1 % len(choices[0])) or p1 == (p2-2 % len(choices[0])):
        print(f"win - {key[p1]} : {key[p2]}")
        win += 1
        score += (p1+1) + 6
    
    else:
        print(f"missing - {key[p1]} : {key[p2]}")
    c += 1


# print(counter)
print("\n" + str(score))
print("\n")
print(draw)
print(lose)
print(win)
