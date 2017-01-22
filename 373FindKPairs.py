class KMinQueue(object):
    def __init__(self,k):
        self.hp=[(2**30,2**30)]*k
        
    def heapify(self):
        current=0
        while(True):
            left,right=2*current+1,2*current+2
            largest=current
            if (left<len(self.hp)) and (sum(self.hp[left])>sum(self.hp[current])):
                largest=left
            if (right<len(self.hp)) and (sum(self.hp[right])>sum(self.hp[largest])):
                largest=right
            if largest==current:
                return
            self.hp[largest],self.hp[current]=self.hp[current],self.hp[largest]
            current=largest
            
    def push(self,x):
        if sum(x)>sum(self.hp[0]):
            return
        self.hp[0]=x
        self.heapify()
        
    def peek(self):
        return(self.hp[0])
        
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if (not nums1) or (not nums2):
            return([])
        queue=KMinQueue(k)
        maximum=queue.peek()
        for a in nums1:
            for b in nums2:
                maximum=queue.peek()
                #print(a,b,maximum,queue.hp)
                if (maximum[1]<b) and (maximum[0]<a):
                    break
                queue.push((a,b))
        return([x for x in queue.hp if x[0]!=2**30])
