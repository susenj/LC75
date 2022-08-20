'''
https://leetcode.com/problems/decode-string/

Solution:
_________
Use stack
'''

class Solution:
    def decodeString(self, s: str) -> str:
        
        stak = []           # To hold the actua stack
        phrase = []         # To hold the intermediate strings inside brackets
        output = ""         # To convert the phrase into string
        intstak = ""        # Stack to carry numeric characters, example "100"
        for char in s:
            if char != ']':
                stak.append(char)
            else:
                # Unless an opening bracket is met, keep creating another stack of characters
                while(stak[-1] != '['):
                    phrase.append(stak.pop())
                
                # Pop the useless opening bracket now.
                stak.pop()
                
                # Now, need to check the number. It could be more than 1 digit...so
                # keep the digits appended into a string intstak which will be read
                # backwards and converted to int by using int()
                while((len(stak) > 0) and stak[-1].isnumeric()):
                    intstak += stak.pop()
                multiplier = int(intstak[::-1])
                intstak = ""
                
                # Join the phrases multiplier times
                for i in range(1, multiplier+1):
                    output += "".join([str(i) for i in phrase[::-1]])
                phrase = []
                
                # Once joined, append to the original stack
                stak.append(output)
                
                # Clear the phrase
                output = ""

        return "".join([str(i) for i in stak])
 
