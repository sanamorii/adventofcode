import sys

with open(sys.argv[1], mode="r") as file:
    r = [ ((["A", "B", "C"].index(x[0])), (["X", "Y", "Z"].index(x[1]))) for x in [ (x.rstrip("\n")).split(" ") for x in file.readlines() ] ]
    score01 = sum([ r[z][1]+4 if r[z][1] == r[z][0] else r[z][1]+1 if r[z][1] == (r[z][0]-1 % 3) or r[z][1] == (r[z][0]+2 % 3) else (r[z][1]+1) + 6 for z in range(0, len(r)) ])
    score02 = sum([ ((r[z][0]-1) % 3) + 1 if r[z][1] == 0 else (r[z][0]+1) + 3 if r[z][1] == 1 else ((r[z][0]+1) % 3) + 7 for z in range(0, len(r)) ])
    print(f"part 1: {score01}\npart 2: {score02}")

# nightmare