def twoSum(i,nums):
    ans = []
    l = 0
    r = len(nums)-1
    while l<r:
        k = nums[l] + nums[r]
        if k == i:
            a = [nums[l],nums[r]]
            if not a in ans:
                ans.append(a)
            r = r -1
        elif k < i :
            l = l + 1
        else:
            r = r -1
    return ans

nums = [-1,0,1,2,-1,-4]
nums.sort()
ans = []
for i in range(len(nums)):
    a = twoSum(-(nums[i]),nums[i+1:len(nums)])
    for j in a:
        j.append(nums[i])
        j.sort()
        if not j in ans:
            ans.append(j)

print(ans)