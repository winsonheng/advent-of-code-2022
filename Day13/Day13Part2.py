import json

with open("13.in") as file:
    lines = [line.rstrip() for line in file]

lines1 = [json.loads(line) for line in lines[0::3]]
lines2 = [json.loads(line) for line in lines[1::3]]

# returns (TerminateFlag, RightOrderFlag)
def compareLists(l1, l2):
    if len(l1) == 0:
        if len(l2) == 0:
            return (False, False)
        else:
            return (True, True)
    elif len(l2) == 0:
        return (True, False)
    checkItem = (False, False)
    if isinstance(l1[0], list) and isinstance(l2[0], list):
        checkItem = compareLists(l1[0], l2[0])
    elif isinstance(l1[0], int) and isinstance(l2[0], int):
        if l1[0] != l2[0]:
            return (True, l1[0] < l2[0])
    elif isinstance(l1[0], list) and isinstance(l2[0], int):
        checkItem = compareLists(l1[0], [l2[0]])
    else: # int and List
        checkItem = compareLists([l1[0]], l2[0])
    
    if checkItem[0]:
        return checkItem
    return compareLists(l1[1:], l2[1:])

fullList = lines1 + lines2 + [[[2]], [[6]]]

for i in range(len(fullList) - 1):
    for j in range(len(fullList) - 1 - i):
        if not compareLists(fullList[j], fullList[j + 1])[1]:
            temp = fullList[j]
            fullList[j] = fullList[j + 1]
            fullList[j + 1] = temp

ans = 1

for i in range(len(fullList)):
    if fullList[i] == [[2]]:
        ans *= (i + 1)
    elif fullList[i] == [[6]]:
        ans *= (i + 1)

print(ans)