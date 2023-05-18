a = '11'
b = '1'

def addBinary(a: str, b: str):
    def addBinary2(ans ,T):
        if T:
            return "1" + ans
        else:
            return '0' + ans

    maxstring = max(len(a),len(b))
    T = False
    ans = ''
    while len(a) != maxstring:
        a = '0' + a
    while len(b) != maxstring:
        b = '0' + b
    for i in range(maxstring-1,-1,-1):
        if a[i] == b[i]:
            if a[i] == '1':
                ans = addBinary2(ans,T)
                T = True
            else:
                ans = addBinary2(ans,T)
                T = False
        else:
            if T:
                ans = "0" + ans
                T = True
            else:
                ans = "1" + ans
                T = False
    if T:
        ans = '1' + ans
    return ans

print(addBinary(a,b))