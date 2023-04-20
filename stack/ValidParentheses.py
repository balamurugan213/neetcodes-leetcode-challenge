# link: https://leetcode.com/problems/valid-parentheses/



# solution 1
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if(i=='(' or i=='{' or i=='['):
                stack.append(i)
            elif(i==')' or i=='}' or i==']'):
                if(len(stack)==0):
                    return False
                if(i==')' and stack[-1]!='('):
                    return False
                if(i=='}' and stack[-1]!='{'):
                    return False
                if(i==']' and stack[-1]!='['):
                    return False
                stack.pop()
        if(len(stack)==0):
            return True
        return False
    
s="()[]{}"
obj = Solution()
print(obj.isValid(s))



'''
Runtime: 36 ms
Memory Usage: 14 MB
------------------------------------------------
'''
import sys
# tell interpreter where to look
sys.path.insert(0,".")

from modules.stack_ds import MyStack

# solution 2
class Solution2:
    def isValid(self, s: str) -> bool:
        obj = MyStack()
        for i in s:
            # print(obj.display(),"---",i)
            if i in ['(','[','{']:
                obj.push(i)
            else:
                if(obj.empty()):
                    return False
                k=obj.pop()
                if( (k=='(' and i!=')') or
                (k=='[' and i!=']') or
                (k=='{' and i!='}')):
                    return False
        return obj.empty()

s2="()[]{}"
obj2 = Solution2()
print(obj2.isValid(s2))

'''
Runtime: 26 ms
Memory Usage: 14.3 MB
------------------------------------------------
'''
        






