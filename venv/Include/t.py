class Node(object):
    """创建单个结点的类"""

    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkdeList():
    '''创建一个单链表'''

    def __init__(self):
        self.head = None

    def is_empty(self):
        '''判断链表是否为空'''
        return self.head.next is None

    def lenght(self):
        '''获取链表长度'''
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def add_first(self, data):
        '''在链表头部添加数据'''
        node = Node(data)
        node.next = self.head
        self.head = node

    def add_last(self, data):
        '''在链表尾部添加数据'''
        node = Node(data)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert_node(self, index, data):
        '''在指定位置添加元素'''
        # node = Node(data)
        if index < 0 or index > self.lenght():
            return False
        elif index == 0:
            self.add_first(data)
        elif index == self.lenght():
            self.add_last(data)
        else:
            node = Node(data)
            cur = self.head
            count = 0
            while count < index - 1:
                cur = cur.next
                count += 1
            node.next = cur.next
            cur.next = node

    def remove_node(self,data):
        '''删除指定节点'''
        cur = self.head  #指针指向的节点
        pre = None # 指针指向节点的前一个
        if self.head == data:
            self.head.next = self.head
