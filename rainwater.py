def solution(height):
    size = len(height);
    maxHeight = 0;
    maxHeightPos = 0;
    realSum = 0;
    for i in range(size):
        if (height[i] > maxHeight):
            maxHeightPos = i;
            maxHeight = height[i];
        realSum += height[i];
    
    i = 0;
    j = size - 1;
    maxPossibleSum = 0;
    maxLeft = 0;
    maxRight = 0;
    while (i <= maxHeightPos or j > maxHeightPos):
        if (height[i] > maxLeft and i <= maxHeightPos):
            maxLeft = height[i];
        if (height[j] > maxRight and j > maxHeightPos):
            maxRight = height[j];
        if (i <= maxHeightPos):
            maxPossibleSum += maxLeft;
        if (j > maxHeightPos):
            maxPossibleSum += maxRight;
        i += 1;
        j -= 1;
        
    return maxPossibleSum - realSum

print(solution([10,1,1,2,1,1,1,1,1,1,1,10]))
