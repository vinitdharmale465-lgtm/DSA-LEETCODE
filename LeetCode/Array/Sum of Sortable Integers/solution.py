class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        if(len(nums) == 1):
            return 1;
        def find_factors_fast(n):
            factors = set()
            # Loop up to the square root of n
            for i in range(1, int(n**0.5) + 1):
                if n % i == 0:
                    factors.add(i)      # add the divisor
                    factors.add(n // i) # Add the matching pair
            return sorted(list(factors));


        ans = 0;
        factors = find_factors_fast(len(nums));
        # print(factors)
        newNums = nums[:];
        nums.sort()


        if(nums == newNums):
            return sum(factors);
        
        def check(a, b):
            if not b:
                return True

            n, m = len(a), len(b)

            # Build LPS array for pattern b
            lps = [0] * m
            j = 0

            for i in range(1, m):
                while j > 0 and b[i] != b[j]:
                    j = lps[j - 1]

                if b[i] == b[j]:
                    j += 1
                    lps[i] = j

            # Search pattern b in list a
            i = j = 0

            while i < n:
                if a[i] == b[j]:
                    i += 1
                    j += 1

                    if j == m:
                        return True
                elif j > 0:
                    j = lps[j - 1]
                else:
                    i += 1

            return False
        

            
        for i in range(1,len(factors)):
            n = factors[i];
            # print(n)
            r = 0;
            l = n;
            flag = True;
            while(l <= len(newNums)):
                new = newNums[r:l];
                new += new;
                # print(new)
                letsee = check(new,nums[r:l])
                if(not letsee):
                    flag = False;
                    break;
                r = l;
                l += n;

            # print(n,flag)
            if(flag):
                ans += n;

                
        return ans;