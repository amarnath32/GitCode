class Solution(object):
    def isCircularSentence(self, sentence):
        if sentence is None:
            return False
        
        if len(sentence)==1:
            return True
    
        for i in range(len(sentence)):
            if sentence[i]==" " and sentence[i-1]!= sentence[i+1]:
                return False
        return sentence[0]==sentence[-1]
        



print(Solution().isCircularSentence("leetcode exercises sound delightful")) # True