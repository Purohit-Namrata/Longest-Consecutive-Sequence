from typing import List
class Solution:
    def longestConsecutive(self,nums:List[int])->int:
        nums=set(nums)
        output=0
        for i in nums:
            if i-1 not in nums:
                first=i
                while first in nums:
                    first+=1
                output=max(output,first-i)
        return output

s=Solution()
n=[100,4,200,1,3,2]

answer=s.longestConsecutive(n)
print("Longest consecutive sequence is: ",answer)


