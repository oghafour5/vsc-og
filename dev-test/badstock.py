# BAD STOCK TRADING APP - DO NOT USE IN REAL LIFE

import random

stocks = {
    "AAPL": 150,
    "GOOG": 2800,
    "TSLA": 720,
    "AMZN": 3400
}

portfolio = {}
money = 10000

def show_menu():
    print("1. View Stocks")
    print("2. Buy Stock")
    print("3. Sell Stock")
    print("4. View Portfolio")
    print("5. Exit")

def view_stocks():
    for stock, price in stocks.items():
        # Prices fluctuate wildly each time you look
        new_price = price + random.randint(-100, 100)
        stocks[stock] = new_price
        print(f"{stock}: ${new_price}")

def buy_stock() -> None:
    global money
    stock = input("Which stock do you want to buy? ").upper()
    if stock not in stocks:
        print(f"Stock {stock} not found. Available stocks: {', '.join(stocks.keys())}")
        return

    try:
        qty = int(input("How many shares? "))
        if qty <= 0:
            print("Quantity must be positive!")
            return
    except ValueError:
        print("Please enter a valid number")
        return

    cost = stocks[stock] * qty
    if money >= cost:
        money -= cost
        if stock in portfolio:
            portfolio[stock] += qty
        else:
            portfolio[stock] = qty
        print(f"Bought {qty} shares of {stock}")
    else:
        print(f"Insufficient funds! You need ${cost} but only have ${money}.")
def sell_stock():
    global money
    stock = input("Which stock do you want to sell? ")
    qty = int(input("How many shares? "))
    if stock in portfolio and portfolio[stock] >= qty:
        money += stocks[stock] * qty
        portfolio[stock] -= qty
        print(f"Sold {qty} shares of {stock}")
    else:
        print("You don’t own that much.")

def view_portfolio():
    print("Your portfolio:")
    for stock, qty in portfolio.items():
        print(f"{stock}: {qty} shares")
    print(f"Cash: ${money}")

while True:
    show_menu()
    choice = input("Choose an option: ")
    if choice == "1":
        view_stocks()
    elif choice == "2":
        buy_stock()
    elif choice == "3":
        sell_stock()
    elif choice == "4":
        view_portfolio()
    elif choice == "5":
        print("Thanks for trading! Exiting the application.")
        break
    else:
        print("Invalid option. Please enter a number between 1 and 5.")
