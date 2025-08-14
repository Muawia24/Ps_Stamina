class Solution:
    def largestGoodInteger(self, num: str) -> str:
        good_nums = [
            "999","888","777", "666", "555",
            "444", "333", "222", "111", "000"
        ]
        for number in good_nums:
            if number in num:
                return number
            
        return ""