# 买卖股票的最好时机

prices = [7, 1, 5, 3, 6, 4]
prices = [7, 6, 4, 3, 1]
inf = int(1e9)
minprice = inf
maxprofit = 0
for price in prices:
    maxprofit = max(price - minprice, maxprofit)
    minprice = min(price, minprice)
print(maxprofit)
