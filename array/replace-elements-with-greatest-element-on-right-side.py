class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]
        
        l = []
        currMax = max(arr[1:])
        i = 1

        while i < len(arr):
            l.append(currMax)
            if arr[i] == currMax and i+1 < len(arr):
                currMax = max(arr[i+1:])
            i+=1
        l.append(-1)
        return l
                