class Solution:
    def maximum69Number (self, num: int) -> int:
        str_num = str(num)
        if '6' not in str_num:
            return num
            
        for i, n in enumerate(str_num):
            if n == '6':
                str_num = str_num[:i] + '9' + str_num[i+1:]

                return int(str_num)