def calculate_profit_loss(cost_price, selling_price):
    if selling_price > cost_price:
        profit = selling_price - cost_price
        profit_percent = (profit / cost_price) * 100
        return f"Profit: ₹{profit:.2f} ({profit_percent:.2f}%)"
    
    elif cost_price > selling_price:
        loss = cost_price - selling_price
        loss_percent = (loss / cost_price) * 100
        return f"Loss: ₹{loss:.2f} ({loss_percent:.2f}%)"
    
    else:
        return "No Profit, No Loss"

# Example usage
cp = float(input("Enter Cost Price: "))
sp = float(input("Enter Selling Price: "))

print(calculate_profit_loss(cp, sp))
