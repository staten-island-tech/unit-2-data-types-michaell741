accounts = [["1", "2", "3"], ["5", "6", "7"], ["1", "2"]]
def maxMoney(accounts):
    int_accounts = [[int(x) for x in i] for i in accounts]
    total = [sum(y) for y in int_accounts]
    wealthiest = max(total)
    print(wealthiest)