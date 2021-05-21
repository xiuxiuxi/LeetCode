class Solution:
    def isMonotonic(self, A:List[int]) -> bool:
        ## check increasing and decreasing
        if sorted(A)== A or sorted(A, reverse=True) == A:
            return True
        return False
        