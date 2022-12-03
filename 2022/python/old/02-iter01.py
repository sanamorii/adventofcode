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
    ply1Choice = choices[0].index(rounds[i][0])
    ply2Choice = choices[1].index(rounds[i][1])

    ## if draw
    #print(f"{ply1Choice} : {ply2Choice}")
    if ply1Choice == ply2Choice:
        #score += (ply1Choice+1) + 3
        # print(f"{ply1Choice} {key[ply1Choice]} - {ply1Choice+1}, 3, {(ply1Choice+1)+3}")
        # print(f"draw {key[ply1Choice]} - {key[(ply1Choice % len(choices[0]))]}\n")
        draw += 1

    # lose
    elif ply1Choice == (ply2Choice-1 % len(choices[0])):
        lose += 1
    elif ply1Choice == (ply2Choice+2 % len(choices[0])):
        
        lose += 1

    # win
    elif ply2Choice == (ply1Choice+1 % len(choices[0])):
        win += 1
    elif ply1Choice == (ply2Choice-2 % len(choices[0])):
        lose += 1
    
    else:
        print(f"{c+1}: {ply1Choice} {key[ply1Choice]} - {ply2Choice} {key[ply2Choice]}")
        counter += 1
    c += 1

# print(score)
# print(counter)
print("\n")
print(draw)
print(lose)
print(win)
