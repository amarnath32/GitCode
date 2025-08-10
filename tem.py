class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:

        # binary search for biggest possible prefix, -1 if none are possible
        def bs(x: int) -> str:
            L=-1
            R=x
            while R>L:
                m = (L+R+1)>>1
                if m*(10**len(s))+int(s)>x: R=m-1
                else: L=m
            return str(L)
        
        # X is a string which is the biggest possible prefix.
        # already_less tells if we have already made a choice less than X
        def f(X: str, already_less: bool) -> int:
            if X=='-1':  return 0 
            if len(X)==0:  return 1
            
            if already_less: # whatever you do here you will still be less, so limit+1 choices
                return (limit+1)*f(X[1:],True)
            else:                     # so far we are equal to X, so either:  
                if int(X[0])<=limit:  # the digit is <= limit (digit choices <, 1 choice equal)
                    return int(X[0])*f(X[1:],True) + f(X[1:],False) 
                else:                 # or the digit is > limit (limit+1 choices, all less than X)
                    return (limit+1)*f(X[1:],True)
    
        return f(bs(finish),False) - f(bs(start-1),False)
    
print(Solution().numberOfPowerfulInt(20,1159,5,20)) # 10