strs = ["dog","racecar","car"]

ans = ""
min_len  = 201
for i in strs:
    if len(i) < min_len:
        min_len = len(i)
for i in range(min_len):
    a = strs[0][i]
    YN = True
    for j in strs:
        if a != j[i]:
            YN = False
            break
    if not YN:
        break
    ans = ans + a
print(ans) 