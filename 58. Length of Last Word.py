class Solution(object):
    def lengthOfLastWord(self, s):

        s=s.strip()
        if not s:
            return 0
        else:
            return len(s.split()[-1])
        


a=Solution()
print(a.lengthOfLastWord("Hello World")) #5
print(a.lengthOfLastWord("  fly me   to   the moon   ")) #5
print(a.lengthOfLastWord("luffy is still joyboy  ")) #5