class Solution:
    def checkValidString(self, s: str) -> bool:
        # * is the wild card, which can represent (, empty , )
        # two situations leading to invalid parenthesis:
        #1. not enough left parenthesis
        #2. not enough right parenthesis
        
        
        # first situation: we count left or wild, if we meet one right, we consume one left or wild. we return false if there isn't enough left or wild
        leftwild = 0
        for char in s:
            if char == ')':
                if leftwild  == 0:
                    return False
                leftwild -= 1
            else:
                leftwild += 1
                
        # second situation: we count right or wild, if we meet one left, we consume one right or wild. we return false if there isn't enough right or wild
                
        rightwild = 0
        for char in reversed(s):
            
            if char == '(':
                
                if rightwild == 0:
                    return False
                rightwild -= 1
            else:
                rightwild += 1
                
        return True