def calcFloor() -> list: 
    with open("01-input.txt", "r") as file: return [1 if x=="(" else -1 for x in file.readline()]

def findBasement(l:list) -> int:
    for i in range(1, len(l)):
        if sum(l[:i]) < 0: return i

print(sum(calcFloor()))
print(findBasement(calcFloor()))
