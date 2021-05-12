class Solution:
    def isPalindrome(self, x: int) -> bool:
    
        listX = str(x)
        rvX = listX [::-1]

        if listX == rvX:
            return True
        else:
            return False
    
            