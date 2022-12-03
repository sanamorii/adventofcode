import sys

score01 = 0
score02 = 0

with open(sys.argv[1], mode="r") as file:
    rounds = [ ((["A", "B", "C"].index(x[0])), (["X", "Y", "Z"].index(x[1]))) for x in [ (x.rstrip("\n")).split(" ") for x in file.readlines() ] ]
    
for i in range(0, len(rounds)):

    p1 = ["X", "Y", "Z"].index(rounds[i][1])
    p2 = ["A", "B", "C"].index(rounds[i][0])

    # draw
    if p1 == p2:  
        score01 += (p1+1) + 3
    # lose
    elif p1 == (p2-1 % 3) or p1 == (p2+2 % 3):
        score01 += (p1+1)
    # win
    else:  
        score01 += (p1+1) + 6

    # lose
    if p1 == 0: 
        score02 += ((p2-1) % 3) + 1
    # draw
    elif p1 == 1: 
        score02 += (p2+1) + 3
    # win
    elif p1 == 2: 
        score02 += ((p2+1) % 3) + 7
    

print(f"part 1: {score01}\npart 2: {score02}")

