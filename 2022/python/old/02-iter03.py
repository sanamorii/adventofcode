import sys


# ROCK, PAPER, SCISSCORS
choices = [("A", "B", "C"), ("X", "Y", "Z")]
key = ["Rock", "Paper", "Scissors"]

outcomes = {'1': '3', '2': '1', '3': '2'}

with open(sys.argv[1], mode="r") as file:
    rounds = [(x.rstrip("\n")).split(" ") for x in file.readlines()]


score = 0
counter = 0

win = lose = draw = 0


for i in range(0, len(rounds)):
    p1 = (choices[0].index(rounds[i][0])) + 1
    p2 = (choices[1].index(rounds[i][1])) + 1

    ## draw
    #print(f"{ply1Choice} : {ply2Choice}")
    if p1 == p2:
        score += (p1) + 3
        draw += 1
    elif p1 == outcomes[str(p2)]:
        score += (p1) + 6
        win += 1
    else:
        score += (p1)
        lose += 1


# print(counter)
print("\n" + str(score))
print("\n")
print(draw)
print(lose)
print(win)
