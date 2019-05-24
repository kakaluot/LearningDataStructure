#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-24 10:57
# @Author  : Allen


class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index
        return


if __name__ == "__main__":
    s = Solution()
    nums = [2, 7, 11, 15]
    assert s.twoSum(nums, 9) == [0, 3]
