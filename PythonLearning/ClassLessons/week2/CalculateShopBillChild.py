import CalculateShopBillBase

print("Using calculateshopbillbase module via import")
#only positional
print("bill 1 :",CalculateShopBillBase.calculate_bill(500, 2))
#with custom tax
print("bill 2 :",CalculateShopBillBase.calculate_bill(500, 2, tax=0.1))
#with custome discount
print("bill 3 :",CalculateShopBillBase.calculate_bill(500, 2, discount=50))
#with custome tax and discount
print("bill 3:",CalculateShopBillBase.calculate_bill(500, 2, tax = 0.08, discount=100))


