class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        return self.score(s,0,len(s)-1)
    def score(self,s,l,r):
        if r-l == 1:
            return (1)
        count = 0
        for i in range (l,r):
            if s[i] == '(':
                count += 1
            if s[i] == ')':
                count -= 1
            if count == 0:
                return self.score(s,l,i) + self.score(s,i+1,r)
        return 2*self.score(s,l+1,r-1)