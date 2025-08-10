class Solution(object):
    def vowelStrings(self, words, queries):
        
        if words and queries is None:
            return 0
            
        res=[]
        vowels = set('aeiou')
        counter =[]
        counter = [1 if word[0] in vowels and word[-1] in vowels else 0 for word in words]


        for q in queries:
            res.append((sum(counter[q[0]:q[1]+1])))

        return res

print(Solution().vowelStrings(["aba","bcb","ece","aa","e"], [[0,2],[1,4],[1,1]]))