

n=int(input())
nums=[0]*n

for i in range(n):
    nums[i]=int(input())
def containsDuplicate(nums):
        mp={}
        for i in range(len(nums)):
            if nums[i] not in mp:
                mp[nums[i]]=1
            else:
                mp[nums[i]]+=1

        if len(mp)==len(nums):
            return False
        else:
            return True
        
print(containsDuplicate(nums))