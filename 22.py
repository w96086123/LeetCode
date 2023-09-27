n = 3

ans = []
template = "()"
def parenthesis(n,temp):
    index = 0
    if n == 0:
        if not (temp in ans):
            ans.append(temp)
    else:
        while (temp.find(")",index,len(temp)) != -1):
            a = temp.find(")",index,len(temp))
            parenthesis(n-1,temp[0:a]+template+temp[a:len(temp)])
            index = a + 1
        parenthesis(n-1,temp+template)

def parenthesis2(ln,rn,temp):
    if rn == ln == 0:
        ans.append(temp)
    elif ln <= rn:
        if ln > 0:
            parenthesis2(ln-1,rn,temp+"(")
        parenthesis2(ln,rn-1,temp+")")

# parenthesis(n-1,"()")
parenthesis2(n,n,"")
print(ans)