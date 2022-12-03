import sys
s1 = s2 = 0
with open(sys.argv[1], mode="r") as f: 
    r = [ (["A", "B", "C"].index(x[0]), (["X", "Y", "Z"].index(x[1]))) for x in [ (x.rstrip("\n")).split(" ") for x in f.readlines() ] ]
for i in range(0, len(r)):
    if r[i][1] == r[i][0]: s1 += (r[i][1]+1) + 3
    elif r[i][1] == (r[i][0]-1 % 3) or r[i][1] == (r[i][0]+2 % 3): s1 += (r[i][1]+1)
    else: s1 += (r[i][1]+1) + 6
    if r[i][1] == 0: s2 += ((r[i][0]-1) % 3) + 1
    elif r[i][1] == 1: s2 += (r[i][0]+1) + 3
    elif r[i][1] == 2: s2 += ((r[i][0]+1) % 3) + 7
print(f"part 1: {s1}\npart 2: {s2}")

####
# this is a horrible idea and completely unnecessary 
####