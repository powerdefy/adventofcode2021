from typing import List, Union

fileName = "input1.txt"


with open(fileName, "r") as file:
    data = [line.rstrip() for line in file]

def toListOfInt(l: List[str]):
    return [int(i) for i in l]

def solve(data: List[str]) -> Union[str, int]:
    data = toListOfInt(data)
    threeItems = []
    c = 0
    for item in data:
        if len(threeItems) == 3:
            if item > threeItems[0]:
                c += 1
            threeItems = threeItems[1:] + [item]
        else:
            threeItems.append(item)
    return c

print(solve(data))
