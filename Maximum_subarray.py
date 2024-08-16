def maxSubArray(nums) :
        sums,maxi=0,(float('-inf'))
        if len(nums)==0:
            return -1
        for i in range(len(nums)):
            sums+=nums[i]
            maxi=max(maxi,sums)
            if sums<0:
                sums=0
        return maxi
    
    
nums=[-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))