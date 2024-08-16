

def productExceptSelf(nums):

        n=len(nums)
        pre=[0]*n
        pre[0]=nums[0]
        prod1=pre[0]
        for i in range(1,len(nums)):
            pre[i]=prod1*nums[i]
            prod1=pre[i]

        prod1=nums[n-1]
        suf=[0]*n
        suf[n-1]=nums[n-1]
        for i in range(len(nums)-2,-1,-1):
            suf[i]=prod1*nums[i]
            prod1=suf[i]

        nums[0]=suf[1]
        nums[n-1]=pre[n-2]

        for i in range(1,len(nums)-1):
            nums[i]=pre[i-1]*suf[i+1]
        return nums





nums=[1,2,3,4]
print(productExceptSelf(nums))