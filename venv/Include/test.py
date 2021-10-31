# -*- coding: utf-8 -*-
# @Time    : 2021/10/30 14:00
# @Author  : knox.chan
# @FileName: test.py
# @Software: PyCharm
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
sp = 0
for i in range(1, len(nums)):
    if nums[i] != nums[sp]:
        sp += 1
        nums[sp] = nums[i]
sp += 1
print(sp)

s = set()
s.add()