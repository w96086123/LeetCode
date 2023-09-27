s ="()[]{}"
current = []
for i in s:
    if i == ")":
        if current[-1] == "(" and len(current) > 0:
            current.pop()
        else:
            print(False)

    elif i == "}":
        if current[-1] == "{" and len(current) > 0:
            current.pop()
        else:
            print(False)
    elif i == "]":
        if current[-1] == "[" and len(current) > 0:
            current.pop()
        else:
            print(False)
    else:
        current.append(i)
if current == []:
    print(True)
else:
    print(False)
