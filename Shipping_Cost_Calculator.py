#Shipping_cost_calculator

#input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms = "))
rate = float(input("Enter the shipping rate per kilograms = "))

#CALCULATE THE SHIPPING COST
shipping_cost = weight * rate

#Display results
print(f"Shipping cost : {shipping_cost} USD")
