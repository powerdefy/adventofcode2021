from typing import List, Union
from collections import Counter

fileName = "input1.txt"

with open(fileName, "r") as file:
    lines = [line.rstrip() for line in file]

def toListOfInt(l: List[str]):
    return [int(i) for i in l]

def findMostCommon(l: List[str]) -> str:
    return Counter(l).most_common(1)[0][0]

def toDecimal(s: str) -> int:
    return int(s, 2)

def flipBits(s: str) -> str:
    r = ""
    for c in s:
        if c == "1":
            r += "0"
        else:
            r += "1"
    return r

def solveP1(lines: List[str]) -> Union[str, int]:
    # gamma rate, epsilon rate
    gammaRate = ""
    epsilonRate = ""
    col = len(lines[0])
    for c in range(col):
        p = []
        for line in lines:
            p.append(line[c])
        epsilonRate += findMostCommon(p)
    return toDecimal(epsilonRate) * toDecimal(flipBits(epsilonRate))

def flipped(flip: bool, value: str):
    if not flip:
        return value

    if value == "1":
        return "0"
    return "1"


def filterOut(lines: List[str], col: int, flip=False) -> List[str]:
    counter = Counter(line[col] for line in lines)
    zero = counter.get("0", 0)
    one = counter.get("1", 0)

    value = None
    if one > zero:
        value = flipped(flip, "1")
    elif zero > one:
        value = flipped(flip, "0")
    else:
        value = flipped(flip, "1")
    return [line for line in lines if line[col] == value]

def solveP2(lines: List[str]) -> Union[str, int]:
    # oxygen generator rating
    # co2 scrub rating
    width = len(lines[0])
    ox = ""
    co = ""

    xLines = lines
    yLines = lines
    for w in range(width):
        xLines = filterOut(xLines, w, False) 
        yLines = filterOut(yLines, w, True)
        if len(xLines) == 1:
            ox = xLines[0]
        if len(yLines) == 1:
            co = yLines[0]
        if len(xLines) == 1 and len(yLines) == 1:
            break

    return toDecimal(ox) * toDecimal(co)


solve = solveP2
print(solve(lines))
