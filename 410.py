nums = [1, 2, 3, 4, 5]
m = 2


def subsplitArray(nums, m):
    if m == 1:
        ans = 0
        for i in nums:
            a = 0
            for j in i:
                a += j
            if ans < a:
                ans = a
        return ans

    for i in range(0, len(nums)):
        for j in range(0, len(nums[i])):
            a = nums[i][0:j+1]
            b = nums[i][j+1:len(nums[i])+1]

            subsplitArray()
