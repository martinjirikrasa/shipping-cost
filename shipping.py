weight = 4.8

#Ground shipping
flat_charge = 20.00
cost = 0
if weight <= 2:
  cost += (flat_charge + weight * 1.50)
  print(cost)
elif 2 <= weight <= 6:
  cost += (flat_charge + weight * 3.00)
  print(cost)
elif 6 <= weight <= 10:
  cost += (flat_charge + weight * 4.00)
  print(cost)
elif 10 <= weight:
  cost += (flat_charge + weight * 4.75)
  print(cost)

# premium shipping

premium_flat_charge = 125.00

if weight <= 2:
  cost = (premium_flat_charge + weight * 4.50)
  print(cost)
elif 2 <= weight <= 6:
  cost = (premium_flat_charge + weight * 9.00)
  print(cost)
elif 6 <= weight <= 10:
  cost = (premium_flat_charge + weight * 12.00)
  print(cost)
elif 10 <= weight:
  cost = (premium_flat_charge + weight * 14.50)
  print(cost) 

# drone shipping 
base_charge_drone = 0
if weight <= 2:
  cost = (weight * 4.50 + base_charge_drone)
  print(cost)
elif 2 <= weight <= 6:
  cost = (weight * 9.00 + base_charge_drone)
  print(cost)
elif 6 <= weight <= 10:
  cost = (weight * 12.00 + base_charge_drone)
  print(cost)
elif 10 <= weight:
  cost = (weight * 14.50 + base_charge_drone)
  print(cost) 