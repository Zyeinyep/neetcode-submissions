class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
    
        
        for n in range(1, numRows+1):
        
            if n == 1:
                triangle.append([1])
                continue
            curr = [1]*n
           
            for i in range(1, n-1):
                

                curr[i] = triangle[n-2][i-1] + triangle[n-2][i]
                
            triangle.append(curr)
        return triangle
          
            

        