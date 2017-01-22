class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return(0)
        mins=[prices[0]]*len(prices)
        maxs=[prices[-1]]*len(prices)
        current_min=prices[0]
        current_max=prices[-1]
        for i in range(len(prices)):
            if prices[i]<current_min:
                current_min=prices[i]
            mins[i]=current_min
        for i in range(len(prices)-1,-1,-1):
            if prices[i]>current_max:
                current_max=prices[i]
            maxs[i]=current_max
        diff=max([maxs[0]-mins[0],0])
        for i in range(len(prices)):
            if maxs[i]-mins[i]>diff:
                diff=maxs[i]-mins[i]
        return(diff)
