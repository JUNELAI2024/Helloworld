# Assignment 2 Exercise 1
class Solution:
    def isAangram(self, s:str, t:str) -> bool:
        #Create a hash map to store char frequency.
        count = {}
        #iterate each character in s, for each char x, count[x]++
        for char in s:
            count[char]=count.get(char,0)+1
        #iterate each character in t, for each char t, count[x]--
        for char in t:
            count[char]=count.get(char,0)-1
        #iterate each key-value pair in count, if count[x] !=0 return false
            for freq in count.values():
                if freq != 0:
                    return False
        #return true
                return True

# Assignment 2 Exercise 2
class solution:
    def containDuplicate(self, nums: List[int])->bool:
        n=len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if nums[i] == nums[j]:
                    return True
        return False

# Assignment 2 Exercise 3
class Solution:
    def twosum(self, nums: List[int], target: int)-> List[int]:
        prevMap = {} #val:index
        for i,n in enumerate(nums):
            diff=target-n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n]=i
            return

# Assignment 2 Exercise 4
class Solution:
    def isValid(self, s: str) -> bool:
        # Create a pair of opening and closing parrenthesis...
        opcl = dict(('()', '[]', '{}'))
        # Create stack data structure...
        stack = []
        # Traverse each charater in input string...
        for idx in s:
            # If open parentheses are present, append it to stack...
            if idx in '([{':
                stack.append(idx)
            # If the character is closing parentheses, check that the same type opening parentheses is being pushed to the stack or not...
            # If not, we need to return false...
            elif len(stack) == 0 or idx != opcl[stack.pop()]:
                return False
        # At last, we check if the stack is empty or not...
        # If the stack is empty it means every opened parenthesis is being closed and we can return true, otherwise we return false...
        return len(stack) == 0

# Assignment 2 Exercise 5
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    # Method to check if a linked list has a cycle
    def hasCycle(self, head: ListNode) -> bool:
        # If the list is empty or contains only one or two nodes, it cannot have a cycle
        if not head or not head.next or not head.next.next:
            return False
        
        # Initialize two pointers, ptr1 and ptr2, both starting from the head of the list
        ptr1 = head
        ptr2 = head
        
        # Iterate through the list until ptr2 reaches the end (ptr2.next is None)
        while ptr2.next:
            # Move ptr1 one step forward
            ptr1 = ptr1.next
            # Move ptr2 two steps forward
            ptr2 = ptr2.next.next
            
            # If ptr1 and ptr2 meet (i.e., they point to the same node), there is a cycle
            if ptr1 == ptr2:
                return True
            
            # If ptr2 becomes None (reached the end of the list), there is no cycle
            if not ptr2:
                return False
        
        # If ptr2 reached the end of the list, return False (no cycle found)
        return False
