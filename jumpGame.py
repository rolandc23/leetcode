# You are given an integer array nums.
# You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# https://leetcode.com/problems/jump-game/

Return true if you can reach the last index, or false otherwise.

def solution(array):
    fuel = 0;
    for i in array:
        if (fuel < 0): return False;
        if (i > fuel): fuel = i;
        fuel -= 1;
    return True;

print(solution([3,2,1,0,4]))
