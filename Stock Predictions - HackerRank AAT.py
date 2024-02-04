import numpy as np

def printTransactions(m, k, d, name, owned, prices):
    transactions = []

    for i in range(k):
        current_stock = {
            "name": name[i],
            "owned": owned[i],
            "prices": prices[i]
        }

        mean_price = np.mean(current_stock["prices"])
        std_dev = np.std(current_stock["prices"])

        if current_stock["prices"][-1] > mean_price + std_dev:
            transactions.append((current_stock["name"], "SELL", current_stock["owned"]))
            current_stock["owned"] = 0
        elif current_stock["prices"][-1] < mean_price - std_dev and m > 0:
            num_shares_to_buy = min(int(m / current_stock["prices"][-1]), 5 - current_stock["owned"])
            transactions.append((current_stock["name"], "BUY", num_shares_to_buy))
            current_stock["owned"] += num_shares_to_buy

    print(len(transactions))
    for transaction in transactions:
        print(f"{transaction[0]} {transaction[1]} {transaction[2]}")

m, k, d = 90, 2, 400
name = ["iStreet", "HR"]
owned = [10, 0]
prices = [
    [4.54, 5.53, 6.56, 5.54, 7.60],
    [30.54, 27.53, 24.42, 20.11, 17.50]
]

printTransactions(m, k, d, name, owned, prices)
