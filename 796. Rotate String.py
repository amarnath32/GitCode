
class Solution(object):
    def rotateString(self, s, goal):
        if s == goal:
            return True
        st=s
        for i in range(0,len(s)):
            st+=st[0]
            st=st[1:]
            if st == goal:
                return True
        return False
    

print(Solution().rotateString("abcde","cdeab")) # True
        
        