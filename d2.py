from typing import List, Union

fileName = "input1.txt"


with open(fileName, "r") as file:
    lines = [line.rstrip() for line in file]

def toListOfInt(l: List[str]):
    return [int(i) for i in l]

def solve(lines: List[str]) -> Union[str, int]:
    pos = [0, 0, 0] # horizonal, depth, aim
    for line in lines:
        command, number = line.split(" ")
        number = int(number)
        if command == "forward":
            pos[0] += number
            pos[1] += pos[2] * number
        elif command == "down":
            pos[2] += number
        elif command == "up":
            pos[2] -= number
    return pos[0] * pos[1]

print(solve(lines))
