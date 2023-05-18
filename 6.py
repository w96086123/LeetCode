# def recursive(s: str, numRows: int):
#     ans = ""
#     if (numRows == 1):
#         ans += s
#     else:
#         temp = []
#         temp.append(s)
#         for i in range(numRows, 0, -1):
#             common = i*2-2
#             if (common == 0):
#                 common = 1
#             for j in range(0, len(temp)):
#                 s = temp.pop(0)
#                 index = 0
#                 while(index < len(s)):
#                     ans += s[index]
#                     index += common
#                     if (index != 0):
#                         if (s[index-common+1:index] != ''):
#                             temp.append(s[index-common+1:index])
#     return ans

# 第二解法
from numpy import common_type
from sympy import false


def recursive(s, numRows):
    ans = ""
    common = numRows*2-2
    i = 0
    j = 0
    while(i < numRows):
        if (j >= len(s)):
            i += 1
            j = i
            if (i == numRows):
                break

        if((j % common) == i or (j % common)-common == i*-1):
            ans += s[j]

        if ((j % common)-common == i*-1 and (j % common) != 0):
            j = j + i*2
        else:
            if (common - i*2 == 0):
                j = j+i
            else:
                j = j + common - i*2

    return ans


print(recursive("PAYPALISHIRING", 4))
# PINALSIGYAHRPI
# PINALYAPSIHRIG
# PINALIGYAIHRN
