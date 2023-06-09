# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length

class Solution(object):

    def maxVowels(self, s, k):
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = 0
        for letter in s[0: k]:
            if letter in vowels:
                count += 1
        max = count
        left, right = 0, k
        while right < len(s):
            if s[left] in vowels:
                count -= 1
            if s[right] in vowels:
                count += 1
            if max < count:
                max = count
            left += 1
            right += 1

        return max
