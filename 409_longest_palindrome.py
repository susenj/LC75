'''
https://leetcode.com/problems/longest-palindrome/

Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
Solution:
________

Keep a map of letters and their frequencies


'''
class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        # if the string is made of only one letter, then it itself is a palindrome
        if len(set(s)) == 1:
            return len(s)
        
        # build a map of all letters along with their frequencies
        freq = {}
        for i in s:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        
        # length of the palindrome
        length = 0
        
        # This flag is necessary to see if we can feed one character at the middle
        # of the palindrome
        singleFrequencyFound = False
        
        # Iterate through the frequencies in the map
        # if even number is found, add it to the length
        # else, just make it even and then add it to the length
        # The catch is, we now know that there is a single character left
        # that can be fed at the middle of the palindrome.
        for i in list(freq.values()):
            if i % 2 == 0:
                length += i
            else:
                length += i - 1
                singleFrequencyFound = True
                
        if singleFrequencyFound:
            return length + 1
        else:
            return length
