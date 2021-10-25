# 存在重复元素

'''给定一个整数数组，判断是否存在重复元素。

如果存在一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。
'''

nums = [1, 2, 3, 4, 5]

# return False

nums = [1, 2, 3, 1]

# reutnr True

# 解题思路：
# 1.暴力破解法：双循环 硬便利逐个检查有没有一样的
# 2.取set如果长度变小 表示有重复数据
print(len(set(nums)) < len(nums))
# 3.单循环 pop + in list 【in list 时间复杂度O(n) in set dict 双向链表o(1)】
# 但是这样随着每次pop 数据长度都会变小 【经过查询 pop 时间复杂度O(N)】

# 先list.sort() 再比对list[i] list[i+1] 时间复杂度应该是o(n)logn + o(n) = o(n)logn
