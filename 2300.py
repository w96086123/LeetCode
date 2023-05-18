spells = [3,1,2]
potions = [8,5,8]
success = 16

def BinarySearch(potions,target):
    l = 0
    r = len(potions) - 1
    while l < r:
        middle = (l + r) // 2
        if potions[middle] >= target:
            r = middle - 1
        else:
            l = middle + 1
    return l

ans = [] 
potions.sort()
for spell in spells:
    temp = success / spell
    i = BinarySearch(potions,temp)
    if potions[i] < temp:
        i += 1
    ans.append(len(potions)- i)
print(ans)
