# повторение пройденного
# class Gaz:
#     def __init__(self, types='простая', v=1, forms='цилиндр'):
#         self.types=types
#         self.v=v
#         self.forms=forms
#     def set_type(self, types):
#         self.types=types
#     def set_v(self,v):
#         setf.v=v
#     def set_forms(self, forms):
#         self.forms=forms
#     def __str__(self):
#        return str(self.__dict__)

# test=Gaz('cola', 2, 'коробка')
# print(test)


# def summ(m, target):
#     for i in range(len(m)):
#         for j in range(i+1, len(m)):
#             if m[i]+m[j]==target:
#                 return [i, j]
                
# print(summ([2,7,11,15], 9))
# print(summ([3,3], 6))
# print(summ([3,6,4,1,8,1], 9))

# import json

# l=json.dumps()

# 
# print(poly(121))
# print(poly(122))        
# print(poly(12344321)) 

# def summs(a: int) -> int:
#     bb=list(map(lambda y: int(y)**2-25,str(a)))
#     b=list(filter(lambda x: True if x>0 else False, bb))
#     # return sum(map(lambda x: int(x), b))
#     return sum(b)
# print(summs(1568923))

# class Techniс:
#     def __init__(self,types='auto', model='vaz2106') -> None:
#         self.types=types
#         self.model=model

# a=input('введите числа через пробел: ')
# lst=a.split(' ')
# b=list(map(lambda x: int(x)**3, lst))
# c=sum(filter(lambda x:True if x>0 else False,b))
# print(c)

# def lens(nums,val):
    # i=0
    # while i<len(nums):
    #     if nums[i]==val:
    #         nums.remove(val)
    #     else:
    #         i+=1
    # return len(nums)
#     while val in nums:
#         nums.remove(val)
#     return len(nums)
# print(lens([1,5,3,4,5,6],5))

# class Solution:
#     def longestCommonPrefix(self, strs) -> str:
#         let=''
#         l=[0]*len(strs)
#         for k in range(len(strs)):
#             l[k]=len(strs[k])
#         for j in range(min(l)):
#             for i in strs:
#                 if strs[0][j]!=i[j]:
#                     return let
#             let+=(strs[0][j])
#         return let
# a=Solution()
# print(a.longestCommonPrefix(["dog","racecar","car"]))
# print(a.longestCommonPrefix(["flower","flow","flight"]))

# class Solution:
#     def twoSum(self, nums, target):
#         o = {}
#         for i in range(len(nums)):
#             if nums[i] in o: return[i, o[nums[i]]]
#             o[target - nums[i]] = i
# a=Solution()
# print(a.twoSum([17,2,11,7,15], 9))

# Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end 
# class Node:
#     def __init__(self, data):
#         self.next = None
#         self.data = data
#     def append(self, val):
#         end = Node(val)
#         n = self
#         while (n.next):
#             n = n.next
#         n.next = end
# class ListNode:
#     def __init__(self, val=0, next=None): 
#         self.val = val
#         self.next = next
#     def append(self, val):
#         end = ListNode(val)
#         n = self
#         while (n.next):
#             n = n.next
#         n.next = end
# def swapNodes(head, k):
#     head[k-1], head[-k] = head[-k], head[k-1]
#     for i in range(len(head)):
#         swapHead=ListNode.append(head[i])
#     return swapHead
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.headvalue = None
    def AtEnd(self,newdata):
         NewNode = Node(newdata)
         if self.headvalue is None:
             self.headvalue = NewNode
             return
         last = self.headvalue
         while(last.next):
             last = last.next
         last.next=NewNode
    def listprint(self):
         printvalue = self.headvalue
         while printvalue is not None:
             print (printvalue.data)
             printvalue = printvalue.next

class Solution:
    def swapNodes(self, head: list, k: int):
        a=[0]*k
        temp=self.headvalue
        next1=next2=0
        for i in range(k):
            if temp.next:
                if next2!=0:
                    a[i]=temp
                    if k-i==2:
                        next1=temp
                    elif k-i==1:
                        next2=temp
                temp=temp.next
                i=0
            else:
                next1.next=a[i]
                next2.next=a[i+1]
                a[i].next=next1
                a[i+1].next=next2
            return

lst = [7,9,6,6,7,8,3,0,9,5]
head = Linkedlist()
for i in lst:
    head.AtEnd(i)
k=5
rev=Solution()
rev.swapNodes(head, k )
head.listprint()