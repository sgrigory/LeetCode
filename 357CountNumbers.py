class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        return_value=0
        for i in range(n+1):
            p=1
            if i>0:
                p=9
            for k in range(i-1):
                p=p*(9-k)
            return_value+=p
        return(return_value)
