  '''
  https://leetcode.com/problems/find-all-anagrams-in-a-string/
  
  Solution:
  _________
  Keep a frequency map of the character of the maps
  
  Run a loop on original string.
  Keep traversing the characters one by one. and keep decrementing their frequencies in the original array. The idea is to check the count of matching characters
  
  See if all characters are matched in the window - It can happen in two cases
    1. The window is larger than the patterns 
    2. The window is equal to the length of the pattern. - Anagram hit. Store the index in the list.
  
  In the first case or in general case, we keep on sliding the window by one character at a time. However, we need to make sure, the changes done
  for that character in the map should be reverted back. Also, the count of matching characters has to be adjusted accordingly.
  
  '''
  
  class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        x = Counter(p) # hold the map of all the charaters in p with their initial frequencies
        result = []    # Holds the final result
        plen = len(p)
        slen = len(s)
        
        # count keeps the count of matching charcters in the window
        # left talks about the left pointer that keeps on moving 1 character
        
        count = left = 0 
        
        
        # Let's look at the invalid window
        for i in range(slen):
            x[s[i]] -= 1
            if x[s[i]] >= 0:       # we found the matching character because despite decrementing its frequency - it's not negative.
                count += 1
            while (count == plen): # At this moment, we have either a match or a match with extra characters
                if (i - left + 1 == plen): # We found a valid window with the anagram and correct length
                    result.append(left)
                
                x[s[left]] += 1     # We are going to slide the window now, better the character count we decremented while creating the window - we should increment it in the map before proceeding to slide.
                if (x[s[left]] >= 1): # if it was one of the characters in the anagram, then we should decrement the matched character count too, no change to the count otherwise (if it was an extra character or a character in the anagram but more than the number with which it was required)
                    count -= 1
                left += 1           # Slide the window by 1 character
        return result
