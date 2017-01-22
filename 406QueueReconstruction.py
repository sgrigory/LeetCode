class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        lst=[]
        people=sorted(people,key=lambda x: (-x[0],x[1]))
        for x in people:
            lst=lst[:x[1]]+[x]+lst[x[1]:]
        return(lst)
