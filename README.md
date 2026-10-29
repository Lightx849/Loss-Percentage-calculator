# Loss-Percentage-calculator

def loss_per():
    cost_price = 0
    sell_price = 0

    while sell_price <= 0:
        print("sell price not less or equal to 0")
        sell_price = int(input("enter the sell price:"))

        if sell_price <=0:
            print("sell price not less and not equal to 0")
            continue

    while cost_price <=0:
        print("cost price not less or equal to 0")
        cost_price = int(input("enter the cost price:"))

        if cost_price <= 0:
            print("cost price not less or equal to 0")
            continue

    loss = cost_price - sell_price
    percentage = (loss / cost_price) * 100
    return percentage

total_loss = loss_per()

print(f"the total loss percentage is:{total_loss}%")
