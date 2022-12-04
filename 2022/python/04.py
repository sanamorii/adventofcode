import sys

with open(sys.argv[1], mode="r") as file: 
    data = file.read().splitlines()
    pairs = [ (x[0].split("-"), x[1].split("-")) for x in [x.split(",") for x in data] ]
    assigned = [ ([*range(int(x[0][0]), int(x[0][1])+1)], [*range(int(x[1][0]), int(x[1][1])+1)]) for x in pairs]

score01 = score02 = 0
for i in assigned:
    # part 1
    if not (set(i[0]) - set(i[1])) or not (set(i[1]) - set(i[0])):
        score01 += 1
    # part 2
    if len(list(set(i[0]) & set(i[1]))) != 0:
        score02 += 1
print(f"{score01}\n{score02}")