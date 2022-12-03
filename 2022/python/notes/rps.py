# too lazy to write out all possible outcomes

choices = [("A", "B", "C"), ("X", "Y", "Z")]

c = [["Rock", "Paper", "Scissors"], ["Rock", "Paper", "Scissors"]]

with open("possibilities.txt", "w+") as f:
    for i in range(0, 3):
        for j in range(0, 3):
            string = f"'{choices[0][i]}': '{choices[1][j]}',\n"

            f.write(string)

    for i in range(0, 3):
        for j in range(0, 3):
            string = f"'{i+1}': '{j+1}',\n"

            f.write(string)


with open("outcomes.txt", "w+") as f:
    for i in range(0, 3):
        for j in range(0, 3):
            string = c[0][i] + " " + c[1][j] + "\n"

            f.write(string)

print("done")