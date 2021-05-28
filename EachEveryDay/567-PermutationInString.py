class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # same alg with #438
        ls1 = len(s1)
        ls2 = len(s2)
        window = None
        s1 = Counter(s1)
        
        for i in range(0, ls2-ls1+1):
            if i == 0:
                window = Counter(s2[:ls1])
            else:
                window[s2[i-1]] -= 1
                window[s2[i+ls1-1]] += 1
            if len(window - s1) == 0:
                return True
        return False
                