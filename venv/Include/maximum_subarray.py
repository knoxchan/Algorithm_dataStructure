# leetcode 53 最大子序和

nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [-1]

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