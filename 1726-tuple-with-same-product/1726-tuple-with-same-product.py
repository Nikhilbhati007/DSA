class Solution(object):
    def tupleSameProduct(self, nums):
        #brute force O(n^4)
        '''
        n=len(nums)
        cnt=0
        for a in range(n):
            for b in range(n):
                for c in range(n):
                    for d in range(n):
                        if a != b and a != c and a != d and b != c and b != d and c != d:
                            if nums[a]*nums[b]==nums[c]*nums[d]:
                                cnt+=1
        return cnt
        '''
        # optimal O(n^2)
        freq={}
        n=len(nums)
        cnt=0
        for i in range(n):
            for j in range(i+1,n):
                prod=nums[i]*nums[j]
                cnt+=8*freq.get(prod,0)
                freq[prod]=freq.get(prod,0)+1
        return cnt


                