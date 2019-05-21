#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-21 21:51
# @Author  : Allen


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:

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
        cur = self.__head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def add(self, data):
        """
        头插法不需要判断是否为空链表
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

    def remove(self, data):
        count, _ = self.search(data)
        if count == 0:
            self.__head = self.__head.next
        else:
            cur = self.__head
            for i in range(0, count-1):
                cur = cur.next
            cur.next = cur.next.next

    def search(self, data):
        cur = self.__head
        count = 0
        while cur is not None:
            if cur.data == data:
                return count, True
            else:
                cur = cur.next
                count += 1
        return False


if __name__ == "__main__":
    ...
