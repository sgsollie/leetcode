"""
https://www.interviewcake.com/question/python/stock-price

First, I wanna know how much money I could have made yesterday if I'd been trading Apple stocks all day.

So I grabbed Apple's stock prices from yesterday and put them in a list called stock_prices, where:

The indices are the time (in minutes) past trade opening time, which was 9:30am local time.
The values are the price (in US dollars) of one share of Apple stock at that time.
So if the stock cost $500 at 10:30am, that means stock_prices[60] = 500.

Write an efficient function that takes stock_prices and returns the best profit I could have made from one purchase and one sale of one share of Apple stock yesterday.

For example:

stock_prices = [10, 7, 5, 8, 11, 9]

get_max_profit(stock_prices)
# Returns 6 (buying for $5 and selling for $11)

Assumptions:
    no shorting of stock.

1. Set pointers at the start and the end of the array.
2. iterate over the array. 
3. For each iteration:
        if left pointer > left[+1] - move left pointer along one
        if right pointer < right[-1] - move right pointer inwards.
4. calculate difference between left and right and return it. - Requirement is only to return the best profit.


"""
stock_prices = [10, 7, 5, 8, 11, 4, 3, 12, 9]

def get_max_profit(stock_prices):
    left = stock_prices[0]
    right = stock_prices[-1]
    profit = 0
    ileft = 1
    iright = len(stock_prices) -2


    while ileft < len(stock_prices):
        if left > stock_prices[ileft]:
            left = stock_prices[ileft]
        ileft += 1
    

    while iright > 0:
        if right < stock_prices[iright]:
            right = stock_prices[iright]
        iright -= 1

    profit = right - left
    return profit

print(get_max_profit(stock_prices))

