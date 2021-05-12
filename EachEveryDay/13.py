class Solution:
    symbols = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000}

    def romanToInt(self, s: str) -> int:
        result = 0
        tmp = 0
        for i in range(len(s) - 1, -1, -1):
            char = s[i]
            curr_num = Solution.symbols[char]
            if curr_num >= tmp:
                result += curr_num
            else:
                result -= curr_num
            tmp = curr_num
        return result
		