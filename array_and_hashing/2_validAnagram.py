# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         # dist={}
#         if(len(s)!=len(t)):
#             return False
#         # for i in s:
#         s=sorted(s)
#         t=sorted(t)
#         if(s==t):
#             return True
#         else:
#             return False


# var isAnagram = (s, t) => s.split('').sort().join('') === t.split('').sort().join('') ? true : false


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dist1={}
        if(len(s)!=len(t)):
            return False
        for i in s:
            if i in dist1:
                dist1[i]+=1
            else:
                dist1[i]=1
        for i in t:
            if i in dist1:
                dist1[i]-=1
            else:
                return False
        return max(dist1.values())==0

s="anagram"
t="nagaram"
obj = Solution()
print(obj.isAnagram(s,t))
