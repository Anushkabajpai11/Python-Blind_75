


n=int(input())
prices=[0]*n
for i in range(n):
    prices[i]=int(input())
    
def maxProfit(prices):
        buy=prices[0]
        prof=0
        for i in range(1,len(prices)):
            prof=max(prof,prices[i]-buy)
            if buy>prices[i]:
                buy=prices[i]

        return prof
    
print(maxProfit(prices))