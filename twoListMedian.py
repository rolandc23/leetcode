# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

# https://app.coderpad.io/sandbox

def solution(arr1, arr2):
    totalLength = len(arr1 + arr2)
    half = totalLength // 2

    A, B = arr1, arr2
    if len(arr1) > len(arr2):
        A, B = B, A
    
    l, r = 0, len(A) - 1
    while True:
        i = (l + r) // 2
        j = half - i - 2
        ALeft = A[i] if i >= 0 else float("-infinity")
        ARight = A[i + 1] if i + 1 <= len(A) - 1 else float("infinity")
        BLeft = B[j] if j >= 0 else float("-infinity")
        BRight = B[j + 1] if j + 1 <= len(B) - 1 else float("infinity")

        if ALeft <= BRight and BLeft <= ARight:
            if totalLength % 2:
                return min(ARight, BRight)
            else:
                return (max(ALeft, BLeft) + min(ARight, BRight)) / 2
        else:
            l = i + 1

def check(arr1, arr2):
    newArray = arr1 + arr2
    newArray.sort()
    totalLength = len(newArray)
    return ((newArray[(totalLength - 1) // 2] + newArray[(totalLength) // 2]) / 2)

print(solution([1, 3, 9], [2, 7, 8, 9, 10]))
print(check([1, 3, 9], [2, 7, 8, 9, 10]))
