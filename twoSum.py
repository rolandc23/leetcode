# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# https://leetcode.com/problems/two-sum/

def solution(array, target):
    dict = {}
    for index, num in enumerate(array):
        if array[index] in dict:
            return (dict[array[index]][0], index)
        dict[target - array[index]] = (index, num)
    return "not found"

print(solution([2,-7,11,15], -5))
