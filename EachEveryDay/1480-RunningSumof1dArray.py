class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        current_sum = 0
        running_sum = []
        
        for num in nums:
            current_sum = current_sum + num
            running_sum.append(current_sum)
        return running_sum
    