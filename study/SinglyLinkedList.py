#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-21 21:51
# @Author  : Allen
"""
单链表
"""


class Node:
    """
    节点
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    """
    链表
    """
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        return self.__head is None

    def length(self):
        cur = self.__head  # 游标
        count = 0  # 计数
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """
        遍历
        :return:
        """
        cur = self.__head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def add(self, data):
        """
        头插法，不需要判断是否为空链表
        :param data:
        :return:
        """
        node = Node(data)
        node.next = self.__head
        self.__head = node

    def append(self, data):
        """
        链表尾部添加元素，尾插法，需要判断是否为空链表
        :param data: 是数据元素，不是节点
        :return:
        """
        node = Node(data)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, index, data):
        """
        :param index: 插入的位置，第一个为0
        :param data: 插入的数据
        :return:
        """
        if index <= 0:
            self.add(data)

        elif index > self.length()-1:
            self.append(data)
        else:
            node = Node(data)
            cur = self.__head
            count = 0
            while count < index - 1:
                cur = cur.next
                count += 1
            node.next = cur.next
            cur.next = node

    def search_remove(self, data):
        """
        这里的删除是使用查找方法找到数据前一个位置后再删除
        :param data:
        :return:
        """
        count = self.search(data)
        if count == -1:
            return
        if count == 0:
            self.__head = self.__head.next
        else:
            cur = self.__head
            for i in range(0, count-1):
                cur = cur.next
            cur.next = cur.next.next

    def remove(self, data):
        """删除节点"""
        cur = self.__head
        pre = None
        while cur is not None:
            # 找到了指定元素
            if cur.data == data:
                # 如果第一个就是删除的节点
                if not pre:
                    # 将头指针指向头节点的后一个节点
                    self.__head = cur.next
                else:
                    # 将删除位置前一个节点的next指向删除位置的后一个节点
                    pre.next = cur.next
                break
            else:
                # 继续按链表后移节点
                pre = cur
                cur = cur.next

    def search(self, data):
        """
        查找
        :param data: 要查找的数据
        :return:如果为-1，代表不存在，否则返回元素所在的索引位置
        """
        cur = self.__head
        count = 0
        while cur is not None:
            if cur.data == data:
                return count
            else:
                cur = cur.next
                count += 1
        return -1


if __name__ == "__main__":
    l = SinglyLinkedList()
    l.append("a")
    l.append("b")
    l.append("c")
    l.append("d")
    l.travel()
    l.search_remove("c")
    l.travel()
