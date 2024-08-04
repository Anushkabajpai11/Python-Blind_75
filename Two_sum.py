


n=int(input("Enter number "))
nums=[0]*n
for i in range(n):
    nums[i]=int(input())
    
target=int(input())

def solve(nums, target):
    
    mp={}
    for i in range(len(nums)):
        if target-nums[i] in mp:
            return [i,mp[target-nums[i]]]
        else:
            mp[nums[i]]=i

    
print(solve(nums,target))






