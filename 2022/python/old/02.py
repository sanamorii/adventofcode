import sys

with open(sys.argv[1], mode="r") as file:
    rounds = [(x.rstrip("\n")).split(" ") for x in file.readlines()]
    
    for i in range(0,len(rounds)):
        for j in range(0,len(rounds[i])):
            if rounds[i][j] == "A" or rounds[i][j] == "X": 
                rounds[i][j] = "R"

            elif rounds[i][j] == "B" or rounds[i][j] == "Y": 
                rounds[i][j] = "P"

            else: 
                rounds[i][j] = "S"


