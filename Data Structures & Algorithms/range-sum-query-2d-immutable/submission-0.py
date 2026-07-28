from collections import defaultdict
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.d = {}
        for r, row in enumerate(matrix):
            for c,val in enumerate(row):
                up = self.d.get((r-1,c),0)
                left = self.d.get((r,c-1),0)
                rep = self.d.get((r-1, c-1),0)
                self.d[(r,c)] = val + up+left - rep
        print(self.d)

                    

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        matrix = self.matrix
        d = self.d
        return d.get((row2, col2),0) - d.get((row1-1,col2), 0 )- d.get((row2,col1-1), 0) + d.get((row1-1, col1-1),0)
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)