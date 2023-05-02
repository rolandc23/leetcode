# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
# (you may want to display this pattern in a fixed font for better legibility)

# https://leetcode.com/problems/zigzag-conversion/

def solution(s, numRows):
    if numRows == 1:
        return s;
    realRemainder = 0;
    remainder = len(s) % (2 * (numRows - 1));
    quotient = (len(s) // (2 * (numRows - 1))) * (numRows - 1);
    if remainder <= numRows:
        realRemainder = 1;
    else:
        realRemainder = remainder - (numRows - 1);
    numCols = quotient + realRemainder;
    x= [['' for i in range(numCols)] for j in range(numRows)];
    currRow = 0;
    currCol = 0;
    currLetter = 0;
    counter = 0;
    for currLetter in s:
        if counter % (2 * (numRows - 1)) < numRows - 1:
            x[currRow][currCol] = currLetter;
            currRow += 1;
        else:
            x[currRow][currCol] = currLetter;
            currRow -= 1;
            currCol += 1;
        counter += 1;
    resString = ''
    for i in range(numRows):
        for j in range(numCols):
            if x[i][j].isalpha():
                resString += x[i][j];
    return resString

print(solution("A", 2))
