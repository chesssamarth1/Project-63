snack_name   = "Chips" 
price        = 1.50 
quantity     = 10 
is_available = True 

print(type(snack_name))
print(type(price)) 
print(type(quantity)) 
print(type(is_available))

price    = 1.50
quantity = 10

total = price * quantity
print("Total value: $", total)
print("Sale price: $", price - 0.25)
print("Double stock:", quantity * 2)


price    = 1.50
quantity = 10

print("Is price under $2?", price < 2)
print("More than 5 in stock?", quantity > 5)
print("Is price exactly $1.50?", price == 1.50)

snack_name = "Chips"

shop_name = "Quick" + " " + "Bites"
print("Shop name:", shop_name)
print("Letters in snack name:", len(snack_name))
print("First letter:", snack_name[0])

price_a = 1.50
price_b = 3.00

temp    = price_a
price_a = price_b
price_b = temp

print("After swap:", price_a, "and", price_b)