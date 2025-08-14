class Solution:
    def largestGoodInteger(self, num: str) -> str:
        good_nums = []
        for i in range(len(num) - 2):
            if num[i] == num[i+1] == num[i+2]:
                good_int = num[i] * 3
                good_nums.append(good_int)
            else:
                continue
        if len(good_nums) == 0:
            return ""
        return max(good_nums)