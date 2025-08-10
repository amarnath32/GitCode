class Solution(object):
    def strStr(self, haystack, needle):

        if needle == "":
            return 0
        counter =0
        for i in range(len(haystack)-len(needle)+1):
            counter=0
            for j in range(len(needle)):
                if haystack[i]!= needle[j]:
                    break    
                else:
                    print("counter",counter)
                    i+=1 
                    counter+=1
                    if counter == len(needle):
                        return i-len(needle)
                        break
                

        return -1





print(Solution().strStr("aaasadbutsad","sad")) # 2