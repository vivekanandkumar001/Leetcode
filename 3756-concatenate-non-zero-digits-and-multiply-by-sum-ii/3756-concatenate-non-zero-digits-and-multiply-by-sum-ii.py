class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        ans = []
        MOD = 10**9 + 7
        n = len(s)
        
        # 1. Powers and running values ko store karne ke liye simple lists
        pow10 = [1] * (n + 1)
        p_sum = [0] * (n + 1)
        p_dig = [0] * (n + 1)
        nz = [0] * (n + 1)
        
        # Ek pass mein data fill kar rahe hain (O(N))
        for i in range(n):
            pow10[i+1] = (pow10[i] * 10) % MOD
            r = int(s[i]) % 10
            if r != 0:
                p_sum[i+1] = (p_sum[i] + r) % MOD
                p_dig[i+1] = (p_dig[i] * 10 + r) % MOD
                nz[i+1] = nz[i] + 1
            else:
                p_sum[i+1] = p_sum[i]
                p_dig[i+1] = p_dig[i]
                nz[i+1] = nz[i]
                
        # 2. Aapka original loop bina 'while' lagaye instantly solve hoga
        for i in queries:
            left, right = i[0], i[1]
            
            # Sum bina loop ke O(1) me
            sum_q = (p_sum[right+1] - p_sum[left] + MOD) % MOD
            
            # Digit bina loop ke O(1) me
            window_nz = nz[right+1] - nz[left]
            left_part = (p_dig[left] * pow10[window_nz]) % MOD
            digit = (p_dig[right+1] - left_part + MOD) % MOD
            
            ans.append((digit * sum_q) % MOD)
            
        return ans