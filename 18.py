nums = [-3,-2,-1,0,0,1,2,3]
target = 0

def fourSum(nums,target):
    def FindTwoSum(nums,N,target):
        ans = []
        if N < 2:
            return []
        elif N == 2:
            l = 0
            r = len(nums)-1
            while l < r:
                if nums[l]+nums[r] == target:
                    ans.append([nums[l],nums[r]])
                    l += 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
            return ans
        else:
            for i in range(len(nums)):
                a = FindTwoSum(nums[i+1:len(nums)],N-1,target-nums[i])
                for j in a:
                    j=j+[nums[i]]
                    j.sort()
                    if not j in ans:
                        ans.append(j)
            return ans
    
    nums.sort()
    return FindTwoSum(nums,4,target)
    
print(fourSum(nums,target))