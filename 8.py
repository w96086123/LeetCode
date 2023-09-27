s = "   -42"
ans = ""
isInt = True
s = s.replace(" ",'',len(s))

for i in s:
    if 48 <= ord(i) <= 57 or ord(i) == 45:
        ans = ans + i
        # -
        if ord(i) == 45:
            isInt = False
    else:
        break
if ans == "":
    print(0)

print(int(ans))