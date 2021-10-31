# 给定一个整数数组 nums和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那两个整数，并返回它们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
#
# 你可以按任意顺序返回答案。

'''
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
'''


# 解题方式1 暴力破解
# 双重遍历
# 时间复杂度 O(n^2)
# 空间复杂度 没有使用额外内容
def tow_sum1():
    nums = [2, 7, 11, 15]
    target = 9
    len_nums = len(nums)
    for i in range(len_nums):
        for j in range(i + 1, len_nums):
            if nums[i] + nums[j] == target:
                return [i, j]

# 解题方式2 哈希法 利用哈希表查找速度快的
# 时间复杂度 o(n)
# 空间复杂度 O(N)

def two_sum3():
    nums = [2, 7, 11, 15]
    target = 9
    hashmap = {}
    for i, num in enumerate(nums):
        if hashmap.get(target - num) is not None:
            return [i, hashmap.get(target - num)]
        hashmap[num] = i  # 这句不能放在if语句之前，解决list中有重复值或target-num=num的情况


print(two_sum3())
