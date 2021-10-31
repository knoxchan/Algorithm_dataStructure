# leetcode 53 最大子序和

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# nums = [-1]

# return 6 [4,-1,2,1]

# 解法1 贪心算法
# 若当前指针所指元素之前的和小于0 则丢弃当前元素的数列

i_sum = 0
max_sum = nums[0]

for i in nums:
    i_sum += i
    if i_sum > max_sum:
        max_sum = i_sum
    if i_sum <= 0:
        i_sum = 0

print(max_sum)

# 解法2 动态规划
# 若前一个元素大于0 将其加到当前元素上

nums = [-1]
max_sum = nums[0]

for i in range(1, len(nums)):
    if nums[i - 1] > 0:
        nums[i] += nums[i - 1]
    if nums[i] > max_sum:
        max_sum = nums[i]

print(max_sum)
