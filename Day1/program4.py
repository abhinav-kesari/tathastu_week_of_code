cost_price = float(input("Enter Cost price :"))
selling_price = float(input("Enter Selling price :"))

profit = selling_price - cost_price

print("Profit from this sell : ",profit )

newselling_price = 0.05 * profit + selling_price

print("Selling price after profit increse by 5% :",newselling_price)