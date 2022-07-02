

def maxProfit(prices):
    min = prices[0] # minimum till date
    x = len(prices)
    max_profit = 0
    profit_today = 0 # today's price
    start, end = 0, 0
    for i in range(1, x):
        if prices[i] < min:
            min = prices[i]
            start = i
            continue
        profit_today = prices[i] - min
        if profit_today > max_profit:
            max_profit = profit_today
            end = i
    return [max_profit, start, end]

prices = [7,6,4,3,1]
op = maxProfit(prices)
print(op[0])
if op[1] < op[2]: 
    print("Buy on day {} and sell on day {}".format(op[1]+1, op[2]+1))
else:
    print('Not possible')
        
