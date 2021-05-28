class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ## using sliding windows
        sum = 0
        min_size = float('inf')
        i = -1 ## left pointer; j is right pointer
        
        ##pointer向右移动增加sum直到sum达到target值
        for j, number in enumerate(nums):
            sum += number
            ##达到target值以后移动左侧pointer缩小windows范围
            while (sum >= target):
                min_size = min (min_size, j - i)
                i +=1
                sum -= nums[i]
                
        if min_size == float('inf'):
            ##no solution
            return (0)
        else:
            return (min_size)
            
                