def stock_tracker():
    stock_prices = {
        "AAPL": 180, 
        "TSLA": 250, 
        "GOOGL": 150
    }
    print("--- Stock Portfolio Tracker ---")
 
    stock_name = input("Enter stock name (AAPL, TSLA, GOOGL): ").strip().upper()
    
    if stock_name in stock_prices:
        try:
            quantity = int(input(f"How many shares of {stock_name} do you have? "))
            
            total_value = quantity * stock_prices[stock_name]
            
            print("\n--- Portfolio Summary ---")
            print(f"Stock Symbol: {stock_name}")
            print(f"Current Price: ${stock_prices[stock_name]}")
            print(f"Total Investment Value: ${total_value}")
        except ValueError:
            print("Error: Please enter a whole number for the quantity.")
    else:
        print(f"Sorry, '{stock_name}' is not in our records.")

stock_tracker()