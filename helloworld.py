class Solution:
    def isAangram(self, s:str, t:str) -> bool:
        return True
    
s= "aragram", t "nangram"
sorted_s ="aaagmnr", sorted_t = "aaagmnr"
s==t

s="rat" , t="car"
sorted_s = "art", sorted_t="acr"
s !=t

class Solution:
    def isAnagram(self, s: str, t:str)->bool:
        sorted_s=sorted(s)
        sorted_t=sorted(t)
        return sorted_s == sorted_t


class solution:
    def containDuplicate(self, nums: List[int])->bool:
        n=len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if nums[i] == nums[j]:
                    return True
        return False
    
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


class Solution:
    def twosum(self, nums: List[int], target: int)-> List[int]:
        prevMap = {} #val:index
        for i,n in enumerate(nums):
            diff=target-n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n]=i
            return