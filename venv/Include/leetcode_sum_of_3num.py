nums = [-1, 0, 1, 2, -1, -4]

# 3数之和


n = len(nums)
nums.sort()
ans = []

for i in range(n):
    # 需要和上一次枚举的数不相同
    if i > 0 and nums[i] == nums[i - 1]:
        continue
    # c 对应的指针指向数组的最右端
    k = n - 1
    target = -nums[i]
    # 枚举b
    for j in range(i + 1, n):
        # 需要和上一次枚举的数不相同
        if j > i + 1 and nums[j] == nums[j - 1]:
            continue
        # 需要保证b的指针在c的左侧
        while j < k and nums[j] + nums[k] > target:
            k -= 1
        # 如果b c 重合则已经计算了所有不重复的情况，推出循环
        if j == k:
            break
        if nums[j] + nums[k] == target:
            ans.append([nums[i],nums[j],nums[k]])
print(ans)
