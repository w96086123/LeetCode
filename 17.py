digits = "23"
# def
key = {"2":["a","b","c"],
       "3":["d","e","f"],
       "4":["g","h","i"],
       "5":["j","k","l"],
       "6":["m","n","o"],
       "7":["p","q","r","s"],
       "8":["t","u","v"],
       "9":["w","x","y","z"]}

ans = []
# function
def dfs(key,temp,index):
    if len(temp) == len(digits):
        ans.append(temp)
    else:
        for i in key[digits[index]]:
            dfs(key,temp+i,index+1)
# main
if(digits != ""):
    dfs(key,"",0)
print(ans)

