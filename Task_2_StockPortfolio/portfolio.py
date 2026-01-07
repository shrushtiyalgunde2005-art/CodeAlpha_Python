# Stock Portfolio Tracker
# CodeAlpha Python Programming Internship - Task 2


stock_prices = {
    "TCS": 3900,
    "WIPRO": 1900,
    "INFY": 2800,
    "ACCEN": 1550,
    "RELIANCE": 4100
}

portfolio_total = 0                        #totsl investment value

print("📈 Welcome to Stock Portfolio Tracker")
print("Available tocks and Prices:")

for company, price in stock_prices.items():
    print(f"{company} : ₹{price}")

while True:
    stock_name = input("\nEnter stock name (or type 'exit' to finish): ").upper()

    if stock_name == "EXIT":                          #user type exit
        break

    if stock_name in stock_prices:
        units = int(input("Enter number of shares: "))
        investment = units * stock_prices[stock_name]     #multiplies
        portfolio_total += investment
        print(f"Added investment value: ₹{investment}")  #how much value was added
    else:
        print("⚠ Stock not found. Please choose from the list.")

print("\n💰 Total Portfolio Value: ₹", portfolio_total)   #final investment value
