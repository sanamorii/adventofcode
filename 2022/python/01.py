import sys

elfCalories = []
calories = 0


with open(sys.argv[1], mode="r") as file:
    data = file.readlines()
    data = [False if x == '\n' else int(x.rstrip('\n')) for x in data]

### part one
for i in range(0,len(data)):
    if not data[i]:
        elf = (i+1, calories)
        elfCalories.append(elf)
        calories = 0
    calories += data[i]

elfCalories.sort(key=lambda a: a[1], reverse=True)
print(f"elf: {elfCalories[0][0]} at {elfCalories[0][1]} calories")
### end


### part two
sumofthree = elfCalories[0][1] + elfCalories[1][1] + elfCalories[2][1]
print(f"top three: {sumofthree}")
### end