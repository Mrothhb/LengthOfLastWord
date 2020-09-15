class Solution:
    def lengthOfLastWord(self, s: str) -> int:
       if(s.isspace() == True or s == ""):
        return 0
       l = s.split()
       l.reverse()
       return len(l[0])
