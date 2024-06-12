class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 1:
            return [[1]]
        
        if numRows == 2:
            return [[1], [1,1]]

        l = []
        prev = self.generate(numRows-1)
        # print(prev)
        for i in range(len(prev[-1])-1):
            a = prev[-1][i] + prev[-1][i+1]
            l.append(a)
        l = [1]+l+[1]

        return prev + [l]
        
        