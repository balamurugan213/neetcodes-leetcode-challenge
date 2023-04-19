# link https://leetcode.com/problems/valid-palindrome/description/ 

#solution 1
class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=s.lower()
        st2=''
        for i in  st:
            if(i.isnumeric()):
                st2=st2+i
            elif  ord(i)>=97 and ord(i)<=122:
                st2=st2+i
        return st2==st2[::-1]

s="A man, a plan, a canal: Panama"
# obj = Solution()
# print(obj.isPalindrome(s))

'''
Runtime: 49 ms
Memory Usage 14.6 MB
------------------------------------------------
'''

#solution 2
class Solution2:
    def isPalindrome(self, s: str) -> bool:
        st=s.lower()
        x=0
        y=len(s)-1
        while(x<y):
            while(((ord(st[x])<97 or ord(st[x])>122) and(not st[x].isnumeric()) and x<len(st)-1)):
                x+=1
            while((( ord(st[y])<97 or ord(st[y])>122 ) and (not st[y].isnumeric()) and y>0)):
                y-=1
            if(x>y):
                continue
            if(st[x]!=st[y]):
                return False
            
            x+=1
            y-=1
        return True

s2="race a car"
obj2 = Solution2()
print('solution 2 answer for input \n',s,':',obj2.isPalindrome(s2))

'''
Runtime: 58 ms
Memory Usage: 14.7 MB
------------------------------------------------
'''

class Solution3:
    def isPalindrome(self, s: str) -> bool:
        x=0
        y=len(s)-1
        while(x<y):
            while x<y and not self.alphaNum(s[x]):
                x+=1
            while y>x and not self.alphaNum(s[y]):
                y-=1
            if(x>y):
                continue
            if(s[x].lower()!=s[y].lower()):
                return False
            
            x+=1
            y-=1
        return True

    def alphaNum(self,c):
        return ('A'<=c<='Z' or
        'a'<=c<='z' or
        '0'<=c<='9'
        )
    
s3=' '
obj3 = Solution3()
print('solution 3 answer for input \n',s3,':',obj3.isPalindrome(s3))

'''
Runtime: 62 ms
Memory Usage: 14.8 MB
------------------------------------------------
'''

#solution 4
import re

class Solution4(object):
    def isPalindrome(self, s):
        new_s = re.sub(r"[^a-zA-Z0-9\\s+]", "", s).lower()
        return new_s == new_s[::-1]


obj=Solution4()
print('solution 4 answer for input \n',s,':',obj.isPalindrome(s))

'''
Runtime: 40 ms
Memory Usage: 15.6 MB
------------------------------------------------
'''