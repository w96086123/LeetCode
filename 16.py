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
    return len(ans)

nums = [-1,2,1,-4]
target = 1

nums.sort()
for i in range(len(nums)):
    ans += twoSum(target - nums[i] ,nums[i+1:len(nums)+1])
print(ans)