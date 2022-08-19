'''
https://leetcode.com/problems/bulls-and-cows/

Solution:
_________

Make frequency map from Secret string
Make frequency map from Guess string
Now, we need to see how many chracters are matching from the Secret string in the Guess string. 
If there is a match, then obviously there are two cases:
  1. The match is a bull match
  2. The match is a cow match.
We also need to take care of the count of the matching character. The minimum of the counts from both secret and guess is the one we need to consider

Once that count is found, we know the total number of matching characters
Now, find the total number of bull matches separately and subtract from the count found above.

'''

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
            bulls=0
            cows=0
            d1=collections.Counter(secret)
            d2=collections.Counter(guess)
            for i in d1:
                if i in d2:
                    cows += min(d1[i],d2[i]) # Notice it's not actual cows count, but it also contains bulls count too
            for i in range(len(secret)):
                if secret[i] == guess[i]:
                    bulls += 1
            return str(bulls) + "A" + str(cows-bulls) + 'B'
