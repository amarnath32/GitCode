class Solution(object):
    def numberOfPowerfulInt(self, start, finish, limit, s):
        """
        :type start: int
        :type finish: int
        :type limit: int
        :type s: str
        :rtype: int
        """
        def check_digits(number):
        # Take the absolute value to handle negative numbers
            n=1
            num = int(number)
            if num<10:
                return 1
            while(True):
                if 10**n <= num < 10**(n+1):
                    return n
                n+=1

        s=int(s)
        #print(s+(limit*10**(check_digits(finish))))
        limit_power = int(10**(check_digits(finish)))
        ulmit = int(min(int(finish),int(s+(limit*limit_power))))
        power =check_digits(s)
        sum=0
        prefix =1
        nums =[]
        new_sum = s
        while(ulmit>=new_sum):
            if new_sum >=start:
                if new_sum in range(start,ulmit+1):
                    nums.append(new_sum)
                else:
                    break
            power_sum = prefix*10**(power+1)
            new_sum = s+power_sum
            prefix+=1
            if prefix >limit:
                prefix = 10
                limit = limit*10
        

        print(nums)
        leng = len(nums)
        return leng
        

  # Output: "Not a 2-digit or 3-digit number"

print(Solution().numberOfPowerfulInt(1,6000,4,124)) # 10
print(Solution().numberOfPowerfulInt(15,215,6,10)) # 10
print(Solution().numberOfPowerfulInt(20,1159,5,20)) # 10
print(Solution().numberOfPowerfulInt(20,1159,5,24)) # 10