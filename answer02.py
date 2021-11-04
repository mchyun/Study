list = ["data.csv"]

def solution():
    stock_prices = []
    for index in range(1, len(data)):
        stock_info = data[index].split(",")
        stock_prices.append([stock_info[0], float(stock_info[1])])
    best_profit = 0
    purchase_date = ""
    purchase_date_price = 0
    sell_date = ""
    sell_date_price = 0
    for buy in range(len(stock_prices)-1):
        for sell in range(buy+1, len(stock_prices)):
            profit = stock_prices[sell][1] - \
                stock_prices[buy][1]
            if profit > best_profit:
                best_profit = profit
                purchase_date = stock_prices[buy][0]
                purchase_date_price = stock_prices[buy][1]
                sell_date = stock_prices[sell][0]
                sell_date_price = stock_prices[sell][1]

    purchase_date_price = round(purchase_date_price, 2)
    sell_date_price = round(sell_date_price, 2)
    best_profit = round(best_profit, 2)
    value_ratio = round(sell_date_price / purchase_date_price, 3)
    print()
    print("Reading data ...")
    print("****************************************")
    print("The maximum profit is", best_profit,
    "per share")
    print()
    print("Buy on", purchase_date, "at the price of", purchase_date_price)
    print("Sell on", sell_date, "at the price of", sell_date_price)
    print()
    print("Change in value ratio is", value_ratio)
    print("****************************************")
    print()

while True:
    data = []
    file_name = input("Please enter the data file name: ")
    if file_name not in list:
        print()
        print("Error Reading data ...")
        print("The file does not exist. Please check the name and try again.")
    if file_name in list:
        with open(file_name, "r") as file:
            for line in file.readlines():
                data.append(line.strip())
        solution()
    if file_name == "":
        print("Good Bye!")
        break
