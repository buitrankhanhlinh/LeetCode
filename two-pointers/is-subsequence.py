class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # if len(t) < len(s):
        #     return False

        # dict1 = {}
        # dict2 = {}

        # for character in s:
        #     if character not in t:
        #         return False
        #     if character not in dict1:
        #         dict1[character] = 1
        #     else:
        #         dict1[character] += 1
            
        # for character in t:
        #     if character not in dict2:
        #         dict2[character] = 1
        #     else:
        #         dict2[character] += 1
        
        # for key in dict1: 
        #     if key in dict2:
        #         if dict1[key] > dict2[key]:
        #             return False
        

        # if s in t:
        #     return True

        # i = []
        # for character in s:           
        #     i.append(t.index(character))
        # return i == sorted(i)

        start2 = 0
        if s== "":
            return True
        if t== "":
            return False

        for start1 in range(len(t)):
            if t[start1] == s[start2]:
                start2 += 1
            if start2 == len(s):
                return True

        return False