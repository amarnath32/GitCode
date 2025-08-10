class Solution(object):
    def vowelStrings(self, words, queries):

        vowels = set('aeiou')
        
        sum=0

        prefix = [0]*(len(words)+1)
        ans =[0]*len(queries)
        for i in range(len(words)):
            current_word = words[i]
            if current_word[0] in vowels and current_word[-1] in vowels:
                sum+=1
            
            prefix[i+1] = sum
            
        for i in range(len(queries)):
            l,r = queries[i]
            ans[i] = prefix[r+1]-prefix[l]

        return ans
    

print(Solution().vowelStrings(["aba","bcb","ece","aa","e"], [[0,2],[1,4],[1,1]])) # [1,2,0]
