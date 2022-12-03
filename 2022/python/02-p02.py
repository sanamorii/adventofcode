import sys


score = 0

with open(sys.argv[1], mode="r") as file:
    # nightmare line of code
    rounds = [ (x.rstrip("\n")).split(" ") for x in file.readlines() ]
    rounds = [ (["A", "B", "C"].index(rounds[x][0]), (["X", "Y", "Z"].index(rounds[x][1]))) 
              for x in range(0, len(rounds)) ]

for i in range(0, len(rounds)):
    # 0 - lose
    # 1 - draw
    # 2 - win
    state = rounds[i][0]  # player 2's state
    cond = rounds[i][1]   # win condition
    
    # win
    if cond == 0: 
        score += ((state-1) % 3) + 1

    # draw
    elif cond == 1: 
        score += (state+1) + 3
    
    # win
    elif cond == 2: 
        score += ((state+1) % 3) + 1 + 6
    
print(score)

