print("===== STOCK PORTFOLIO TRACKER =====")

portfolio = []

n = int(input("Enter number of stocks: "))

for i in range(n):
    print("\nStock", i + 1)

    name = input("Enter stock name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per share: "))

    total = quantity * price

    portfolio.append((name, quantity, price, total))

print("\n===== PORTFOLIO SUMMARY =====")

grand_total = 0

for stock in portfolio:
    name, quantity, price, total = stock

    print("Stock:", name)
    print("Quantity:", quantity)
    print("Price:", price)
    print("Total:", total)
    print("--------------------")

    grand_total += total

print("Total Portfolio Value:", grand_total)
print("\nThank you for using Stock Portfolio Tracker!")