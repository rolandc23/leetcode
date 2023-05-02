def solution(array):
    fuel = 0;
    for i in array:
        if (fuel < 0): return False;
        if (i > fuel): fuel = i;
        fuel -= 1;
    return True;

print(solution([3,2,1,0,4]))
