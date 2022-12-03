import sys

elfCalories = []
calories = 0

with open(sys.argv[1], mode="r") as file:
    data = [False if x == '\n' else int(x.rstrip('\n')) for x in file.readlines()]
    


### part one
for i in range(0,len(data)):
    if not data[i]:
        elfCalories.append(calories)
        calories = 0
    calories += data[i]


elfCalories.sort(key=lambda a: a, reverse=True)
print(f"{elfCalories[0]}\n{sum(elfCalories[0:3])}")
### end


# ### part two
# sumofthree = elfCalories[0][1] + elfCalories[1][1] + elfCalories[2][1]
# print(f"top three: {sumofthree}")
# ### end

#icomplete