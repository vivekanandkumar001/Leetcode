class Solution:
    def sumAndMultiply(self, n: int) -> int:
        num = str (n)
        x_str = ""
        sum = 0
        for i in num:
            if i != '0':
                x_str +=i
                sum += int (i)
        if not x_str:
            return 0 

        x = int(x_str)
        return x*sum
