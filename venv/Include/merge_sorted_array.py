# 给你两个按非递减顺序排列的整数数组nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。
# 
# 请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。
# 
# 注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。
#


# 方案1 直接两个拼接 使用快速排序进行排序
def solue1():
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    nums1[m:] = nums2
    nums1.sort()
    return nums1


# 方案2 归并排序 使用两个指针
def solue2():
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    sorted = []
    p1, p2 = 0, 0
    while p1 < m or p2 < n:
        if p1 == m:
            sorted.append(nums2[p2])
            p2 += 1
        elif p2 == n:
            sorted.append(nums1[p1])
            p1 += 1
        elif nums1[p1] < nums2[p2]:
            sorted.append(nums1[p1])
            p1 += 1
        else:
            sorted.append(nums2[p2])
            p2 += 1
    nums1[:] = sorted
    return sorted


print(solue2())
