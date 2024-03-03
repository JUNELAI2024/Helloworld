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
