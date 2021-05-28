class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ls = len(s)
        lp = len(p)
        
        # Counter会计算每个字符出现的次数:Counter({'a': 3, 'b': 2, 'c': 1, 'd': 1})
        p = Counter(p) #变成hash table
        ans = []
        
        window = None
        
        #开始设置window
        for i in range(0, ls-lp+1):
            if i == 0:
                window = Counter(s[:lp]) # [ start: stop: step]; 选取从零开始到p的长为初始窗口作为并计算字符频率（因为忽略顺序）
            else: 
                window[s[i-1]] -= 1       #向右移一步:1.把窗口左侧字符去除
                window[s[i+lp-1]] +=1      #          2.把窗口右侧字符加上
            if len(window - p) == 0:       #如果窗口字符频率与p相等，就是解(无法直接比较counter)
                ans.append(i)             #把解添加到答案a列表里  
        return ans