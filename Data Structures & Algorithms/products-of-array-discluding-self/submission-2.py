class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #leftProds
        lp = [1]
        curProd = 1
        for num in nums: 
            curProd *= num
            lp.append(curProd)
        
        print(lp)

        #rightProds
        curProd = 1
        rp = [1]
        for num in nums[::-1]: 
            curProd *= num
            rp.append(curProd)
        
        print(rp)
        ans = []
        for i in range(len(nums)): 
            ans.append(lp[i]*rp[len(nums)-1 - i])

        return (ans)