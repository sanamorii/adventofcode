import sys
from string import ascii_letters as chars

score01 = score02 = 0

with open(sys.argv[1], mode="r") as file: data = file.read().splitlines()

rucksacks = [ (x[:int(len(x)/2)], x[-int(len(x)/2):]) for x in data ]
groups = [ data[z:z+3] for z in range(0, len(data), 3) ]

# part 1
for rucksack in rucksacks:
    # returns all instances - only concenered if there is a duplicate - hence [0]
    # result = [ chars.index(c)+1 for c in rucksack[1] if c in rucksack[0] ][0]  
    # print(result)

    # i could've used sets instead of whatever nightmare i thought of before :^) - MSC1
    result = list(set(rucksack[0]) & set(rucksack[1]))[0]
    score01 += chars.index(result)+1
# end

# part 2
for group in groups:
    result = list(set(group[0]) & set(group[1]) & set(group[2]))[0]
    score02 += chars.index(result)+1
#end 

print(f"{score01}\n{score02}")


