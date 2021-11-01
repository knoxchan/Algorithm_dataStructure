# 给定两个数组，编写一个函数来计算它们的交集。

# 输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2,2]

# 解法一 哈希法
# 使用一个字典 将较短数组中的数字做一个计数
# 遍历第二个列表时，如果有该数字 计数减1 将该数字输出到结果列表

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]

import collections

result = []
m = dict(collections.Counter(nums1))
for n in nums2:
    if n in m and m[n] != 0:
        m[n] -= 1
        result.append(n)
print(result)

# 解法二 双重指针
# 先对两个数组进行排序 然后使用两个指针遍历两个数组

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
nums1.sort()
nums2.sort()

index1 = 0
index2 = 0

len_1, len_2 = len(nums1), len(nums2)

result = []
while index1 < len_1 and index2 < len_2:
    if nums1[index1] < nums2[index2]:
        index1 += 1
    elif nums1[index1] > nums2[index2]:
        index2 += 1
    else:
        result.append(nums1[index1])
        index1 += 1
        index2 += 1
print(result)
