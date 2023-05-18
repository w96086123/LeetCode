def check(s: str, p: str):
    if(len(p) == 0):
        if (len(s) != 0):
            return False
        else:
            return True
    if(p[0] == '.'):
        return check(s[1:], p[1:])
    elif(p[0] == '*'):
        for i in range(1, len(s)):
            if s[i] == p[1]:
                if check(s[i:], p[1:]) == True:
                    return True
        if (len(p) == 1):
            return True
        return check(s, p[1:])
    else:
        if s[0] == p[0]:
            return check(s[1:], p[1:])
        else:
            for i in range(1, len(p)):
                if s[0] == p[i]:
                    return check(s, p[i:])
                elif p[i] == '.' or p[i] == '*':
                    return check(s, p[i:])
            return False


print(check("mississippi", "mis*is*p*."))
