class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for character in s:
            if character not in d:
                d[character] = 1
            else:
                d[character] += 1

        a = 0
        ans = 0
        for k, v in d.items():
            if v %2==0:
                ans += v
            else:
                ans += (v-1)
                a  = 1
        
        return ans + (a + 1) // 2
            
            


            
        
