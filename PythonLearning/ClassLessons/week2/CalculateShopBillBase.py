def calculate_bill(item_cost, quantity, tax=0.05, discount=0):
 total=(item_cost * quantity) + (item_cost * quantity * tax) - discount
 return total

if __name__ == "__main__":
 print("using calculateshopbillbase function directly")
#only positional
 print("bill 1 :",calculate_bill(500, 2))
#with custom tax
 print("bill 2 :", calculate_bill(500, 2, tax=0.1))
#with custome discount
 print("bill 3 :", calculate_bill(500, 2, discount=50))
#with custome tax and discount
 print("bill 3:", calculate_bill(500, 2, tax = 0.08, discount=100))
 

