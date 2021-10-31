# -*- coding: utf-8 -*-
# @Time    : 2021/10/30 14:52
# @Author  : knox.chan
# @FileName: Link_list.py
# @Software: PyCharm

import names
import random


# 链表相关

# 节点对象定义
class Student:
    def __init__(self):
        self.name = ''
        self.score = 0
        self.next = None


class SinglyLinkList:
    # 遍历单项链表
    def traverse_singly_link(self, header):
        ptr = header.next  # 设置存取指针从链表的头不开始
        while ptr != None:
            print(f"姓名是:{ptr.name},分数是:{ptr.score}")
            # 将ptr移向下一个元素的位置
            ptr = ptr.next

    # 建立一个链表 -
    def bulid_singly_link(self):
        header = Student()
        ptr = header
        select = 0

        while select != 2:
            try:
                select = int(input('1.新增一个节点 2.退出'))
            except ValueError as e:
                print('输入错误', e)
                continue
            if select == 1:
                new_data = Student()
                new_data.name = input('姓名：')
                new_data.score = eval(input('分数:(输入字符串或是数字，没有做错误检测)'))
                ptr.next = new_data
                ptr = new_data

        return header

    # 建立一个长度为num的单项链表
    def bilid_random_singly_link(self, num: int):
        header = Student()
        ptr = header

        for i in range(num):
            new_data = Student()
            new_data.name = names.get_first_name()
            new_data.score = random.randint(0, 100)
            ptr.next = new_data
            ptr = new_data
        return header

    # 插入在指定位置后面插入一个新的的节点
    def insert_new_node(self, header, num):
        ptr = header
        for i in range(num):
            ptr = header.next
        new_data = Student()
        new_data.name = names.get_first_name()
        new_data.score = random.randint(0, 100)

        print(f'在{num}位置插入一个新的节点')
        print('链表插入前')
        self.traverse_singly_link(header)
        print('------------------')
        print('插入节点后')
        new_data.next = ptr.next
        ptr.next = new_data
        self.traverse_singly_link(header)

    # 在指定位置删除一个节点
    def delete_node(self, header, num):
        print(f'在{num}位置删除一个新的节点')
        print('链表删除前')
        self.traverse_singly_link(header)
        print('------------------')
        print('删除节点后')
        ptr = header
        for i in range(num):
            ptr = header.next
        ptr.next = ptr.next.next
        self.traverse_singly_link(header)




if __name__ == '__main__':
    s = SinglyLinkList()
    header = s.bilid_random_singly_link(3)
    s.reverse_singly_link(header)
