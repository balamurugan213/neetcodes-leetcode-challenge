from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dist={}
        flag=False
        for i in nums:
            if i in dist:
                flag=True
                break
            else:
                dist[i]=1
        return flag

nums =[1,2,3,1]
obj = Solution()
print(obj.containsDuplicate(nums))