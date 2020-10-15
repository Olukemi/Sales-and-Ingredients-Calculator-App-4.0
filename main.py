#Olukemi Odujinrin
#Wednesday January 17th 2018

from datetime import datetime
now = datetime.now()

print "Welcome to 241Pizza Sales and Ingredients Calculator App."
print "Let's get started!"
print "These are your products and their prices in dollars."

products = {'Small pizza' : 6.99 , 'Medium pizza' : 8.99, 'Large pizza' : 11.99, 'X-Large pizza' : 13.99, 'Party Size pizza' : 19.99, 'Slice pizza' : 3.99, 'Beverages' : 1.29,'6pc wings' : 5.99, '10pc wings' : 8.99, '15pc wings' : 12.99,  '20pc wings' : 16.99, 'Garlic Bread' : 4.29, '6pc knots' : 4.99, '5 donuts' : 3.99, '10 donuts' : 6.99, 'Deliveries' : 2.99}

ingredients = {'Flour' : 10, 'Sugar' : 10, 'Tomato Sauce' : 24, 'Cheese' : 100, 'Pepperoni' : 75, 'Pepper' : 50, 'Ham' : 70, 'Bacon' : 70, 'Mushrooms' : 70, 'Pineapples' : 10, 'Sausage' : 60, 'Onion' : 40, 'Olives' : 30, 'Tomatoes' : 55, 'Drinks' : 160, 'Chicken topping' : 50,'Chicken Wings' : 30}

print products

print "The list below is a list of all the ingredients used to make your product, how much of each you started the week with and their stock numbers in (kg,quanity(4))"

print ingredients
  
while True:
  print "PIZZAS"
  try:
    smpizza = int(raw_input("Small pizzas sold this week:"))
  except:
    print "Invaild Answer"
    smpizza = 0
    print "Small pizzas sold this week: 0"
  try:
    mepizza = int(raw_input("Medium pizzas sold this week:"))
  except:
    print "Invaild Answer"
    mepizza = 0
    print "Medium pizzas sold this week: 0"
  try:
    lrpizza = int(raw_input("Large pizzas sold this week:"))
  except:
    print "Invaild Answer"
    lrpizza = 0
    print "Large pizzas sold this week: 0"
  try:
    xlpizza = int(raw_input("X-Large pizzas sold this week:"))
  except:
    print "Invaild Answer"
    xlpizza = 0
    print "X-Large pizzas sold this week: 0"
  try:
    pspizza = int(raw_input("Party Size pizzas sold this week:"))
  except:
    print "Invaild Answer"
    pspizza = 0
    print "Party Size pizzas sold this weel: 0"
  try:
    slpizza = int(raw_input("Slice pizzas sold this week:"))
  except:
    print "Invaild Answer"
    slpizza = 0
    print "Slice pizzas sold this week 0"
  print "BEVERAGES"
  try:
    drink = int(raw_input("Drinks sold this week:"))
  except:
    print "Invaild Answer"
    drink = 0
    print "Drinks sold this week: 0"
  print "SIDES"
  try:
    chick6 = int(raw_input("6pc chicken wings sold this week:"))
  except:
    print "Invaild Answer"
    chick6 = 0
    print "6pc chicken wings sold this week: 0"
  try:
    chick10 = int(raw_input("10pc chicken wings sold this week:"))
  except:
    print "Invaild Answer"
    chick10 = 0
    print "10pc chicken wings sold this week: 0"
  try:
    chick15 = int(raw_input("15pc chicken wings sold this week:"))
  except:
    print "Invaild Answer"
    chick15 = 0
    print "15pc chicken wings sold this week: 0"
  try:
    chick20 = int(raw_input("20pc chicken wings sold this week:"))
  except:
    print "Invaild Answer"
    chick20 = 0
    print "20pc chicken wings sold this week: 0"
  try:
    gabrd = int(raw_input("Garlic breads sold this week:"))
  except:
    print "Invaild Answer"
    gabrd = 0
    print "Garlic breads sold this week: 0"
  print "SWEETS"
  try:
    knots6 = int(raw_input("6pc knots sold this week:"))
  except:
    print "Invaild Answer"
    knots6 = 0
    print "6pc knots sold this week: 0"
  try:
    donut5 = int(raw_input("5pc donuts sold this week:"))
  except:
    print "Invaild Answer"
    donut5 = 0
    print "5pc donuts sold this week: 0"
  try:
    donut10 = int(raw_input("10pc donuts sold this week:"))
  except:
    print "Invaild Answer"
    donut10 = 0
    print "10pc donuts sold this week: 0"
  print "DELIVERIES"
  try:
    delivery = int(raw_input("Deliveries this week:"))
  except:
    print "Invaild Answer"
    delivery = 0
    print "Deliveries this week: 0"
  print "TIPS"
  t = raw_input("Were there any tips this week? yes/no:")
  if t in ['yes', 'y', 'Y', 'YES']:
    try:
      tips = (float(raw_input("How much were tips e.g(2.00):")))
    except:
      print "Invaild Answer"
      tips = 0
  else:
    tips = 0
  
  def pro_cost(quantity, price):
    return quantity * price
   
  sm_cost = pro_cost(smpizza, products['Small pizza'])
  me_cost = pro_cost(mepizza, products['Medium pizza']) 
  lr_cost = pro_cost(lrpizza, products['Large pizza']) 
  xl_cost = pro_cost(xlpizza, products['X-Large pizza']) 
  ps_cost = pro_cost(pspizza, products['Party Size pizza']) 
  sl_cost = pro_cost(slpizza, products['Slice pizza'])
  dr_cost = pro_cost(drink, products['Beverages'])
  c6_cost = pro_cost(chick6, products['6pc wings']) 
  c10_cost = pro_cost(chick10, products['10pc wings'])
  c15_cost = pro_cost(chick15, products['15pc wings']) 
  c20_cost = pro_cost(chick20, products['20pc wings']) 
  ga_cost = pro_cost(gabrd, products['Garlic Bread'])
  k6_cost = pro_cost(knots6, products['6pc knots']) 
  d5_cost = pro_cost(donut5, products['5 donuts'])
  d10_cost = pro_cost(donut10, products['10 donuts'])
  de_cost = pro_cost(delivery, products['Deliveries'])
  
  def pizza_cost(small, medium, large, xlarge, party, slices):
    return small + medium + large + xlarge + party + slices
     
  totalpizza_cost = pizza_cost(sm_cost, me_cost, lr_cost, xl_cost, ps_cost, sl_cost)
  
  def sides_cost(drinks, chick_6, chick_10, chick_15, chick_20, garlic):
    return drinks + chick_6 + chick_10 + chick_15 + chick_20 + garlic
    
  totalsides_cost = sides_cost(dr_cost, c6_cost, c10_cost, c15_cost, c20_cost, ga_cost)
  
  def sweets_cost(knots, donuts_5, donuts_10):
    return knots + donuts_5 + donuts_10
    
  totalsweets_cost = sweets_cost(k6_cost, d5_cost, d10_cost)
    
  def extra_cost(delivery, tip):
    return delivery + tip
   
  totalextra_cost = extra_cost(de_cost, tips)
  
  def semi_total(pizza, sides, sweets, extra):
    return pizza + sides + sweets + extra 
    
  semitotal = semi_total(totalpizza_cost, totalsides_cost, totalsweets_cost, totalextra_cost)
  
  def taxes(part, thirteen):
    return part * thirteen
    
  tax = taxes(semitotal, 0.13)
  
  def total(part1, part2):
    return part1 + part2
    
  grand_total = total(semitotal, tax)

  ingredients = {'Flour' : 10, 'Sugar' : 10, 'Tomato Sauce' : 24, 'Cheese' : 100, 'Pepperoni' : 75, 'Pepper' : 50, 'Ham' : 70, 'Bacon' : 70, 'Mushrooms' : 70, 'Pineapples' : 10, 'Sausage' : 60, 'Onion' : 40, 'Olives' : 30, 'Tomatoes' : 55, 'Drinks' : 160, 'Chicken topping' : 50,'Chicken Wings' : 30}
  
  print ingredients
  
  print "The list above is a list of all the ingredients used to make your product, how of each you started the week with and their stock numbers in (kg,quanity(4))"
  
  def leftover(original, used):
    return original - used
  
  def invaild(leftover_any):
    if leftover_any <= -1:
      print "Invaild. You used more than you had in stock"
      correct = int(raw_input("Re-enter another number for this ingredient"))
    return invaild
    
  print "INGREIDENTS"
  try:
    flour = int(raw_input("Number of bags of flour used this week:"))
  except:
    print "Invaild Answer"
    flour = 0
    print "Number of bags of flour used this week: 0"
  leftover_flour = leftover(ingredients['Flour'], flour)
  invaild(leftover_flour)
  try:
    sugar = int(raw_input("Number of bags of sugar used this week:"))
  except:
    print "Invaild Answer"
    sugar = 0
    print "Number of bags of sugar used this week: 0"
  leftover_sugar = leftover(ingredients['Sugar'], sugar)
  invaild(leftover_sugar)
  try:
    tomato_sauce = int(raw_input("Number of packets of tomato sauce used this week:"))
  except:
    print "Invaild Answer"
    tomato_sauce = 0
    print "Number of packets of tomato sauce used this week: 0"
  leftover_tomato_sauce = leftover(ingredients['Tomato Sauce'], tomato_sauce)
  invaild(leftover_tomato_sauce)
  try:
    cheese = int(raw_input("Number of kilograms of cheese used this week"))
  except:
    print "Invaild Answer"
    cheese = 0
    print "Number of kilograms of cheese used this week: 0"
  leftover_cheese = leftover(ingredients['Cheese'], cheese)
  invaild(leftover_cheese)
  try:
    pepperoni = int(raw_input("Number of kilograms of pepperoni used this week:"))
  except:
    print "Invaild Answer"
    pepperoni = 0
    print "Number of kilograms of pepperoni used this week: 0"
  leftover_pepperoni = leftover(ingredients['Pepperoni'], pepperoni)
  invaild(leftover_pepperoni)
  try:
    peppers = int(raw_input("Number of kilograms of peppers used this week:"))
  except:
    print "Invaild Answer"
    peppers = 0
    print "Number of kilograms of peppers used this week: 0"
  leftover_pepper = leftover(ingredients['Pepper'], peppers)
  invaild(leftover_pepper)
  try:
    ham = int(raw_input("Number of kilograms of ham used this week:"))
  except:
    print "Invaild Answer"
    ham = 0
    print "Number of kilograms of ham used this week: 0"
  leftover_ham = leftover(ingredients['Ham'], ham)
  invaild(leftover_ham)
  try:
    bacon = int(raw_input("Number of kilograms of bacon used this week:"))
  except:
    print "Invaild Answer"
    bacon = 0
    print "Number of kilograms of bacon used this week: 0"
  leftover_bacon = leftover(ingredients['Bacon'], bacon)
  invaild(leftover_bacon)
  try:
    mushrooms = int(raw_input("Number of kilograms of mushrooms used this week:"))
  except:
    print "Invaild Answer"
    mushrooms = 0
    print "Number of kilograms of mushrooms used this week: 0"
  leftover_mushrooms = leftover(ingredients['Mushrooms'], mushrooms)
  invaild(leftover_mushrooms)
  try:
    sausage = int(raw_input("Number of kilograms of sausage used this week:"))
  except:
    print "Invaild Answer"
    sausage = 0
    print "Number of kilograms of sausage used this week: 0"
  leftover_sausage = leftover(ingredients['Sausage'], sausage)
  invaild(leftover_sausage)
  try:
    pineapple = int(raw_input("Number of large cans of pineapple used this week:"))
  except:
    print "Invaild Answer"
    pineapple = 0
    print "Number of large cans of pineapple used this week: 0"
  leftover_pineapple = leftover(ingredients['Pineapples'], pineapple)
  invaild(leftover_pineapple)
  try:
    onion = int(raw_input("Number of kilograms of onions used this week:"))
  except:
    print "Invaild Answer"
    onion = 0
    print "Number of kilograms of onions used this week: 0"
  leftover_onions = leftover(ingredients['Onion'], onion)
  invaild(leftover_onions)
  try:
    olives = int(raw_input("Number of kilograms of olives used this week:"))
  except:
    print "Invaild Answer"
    olives = 0
    print "Number of kilograms of olives used this week: 0"
  leftover_olives = leftover(ingredients['Olives'], olives)
  invaild(leftover_olives)
  try:
    tomato = int(raw_input("Number of kilograms of tomatoes used this week:"))
  except:
    print "Invaild Answer"
    tomato = 0
    print "Number of kilograms of tomato used this week: 0"
  leftover_tomatoes = leftover(ingredients['Tomatoes'], tomato)
  invaild(leftover_tomatoes)
  try:
    chicken = int(raw_input("Number of kilograms of chicken used this week:"))
  except:
    print "Invaild Answer"
    chicken = 0
    print "Number of kilograms of chicken used this week: 0"
  leftover_chicken_topping = leftover(ingredients['Chicken topping'], chicken)
  invaild(leftover_chicken_topping)
  try:
    chickwg = int(raw_input("Number of large boxes of chicken wings used this week:"))
  except:
    print "Invaild Answer"
    chickwg = 0
    print "Number of large boxes of chicken wings used this week: 0"
  leftover_chicken_wings = leftover(ingredients['Chicken Wings'], chickwg)
  invaild(leftover_chicken_wings)
    
  leftover_drinks = leftover(ingredients['Drinks'], drink)
    
  
  if leftover_flour <= 4:
    print "You have %d bags of flour left"  % (leftover_flour)
    print "You need to restock at least 6 bags of flour"
  
  if leftover_sugar <= 4:
    print "You have %d bags of sugar left"  % (leftover_sugar)
    print "You need to restock at least 6 bags of sugar"
  
  if leftover_tomato_sauce <= 16:
    print "You have %d packets of tomato sauce left"  % (leftover_tomato_sauce)
    print "You need to restock at least 8 packets of tomato sauce"
    
  if leftover_cheese <= 75:
    print "You have %d kilograms of cheese left"  % (leftover_cheese)
    print "You need to restock at least 25kg of cheese"
  
  if leftover_pepperoni <= 50:
    print "You have %d kilograms of pepperoni left"  % (leftover_pepperoni)
    print "You need to restock at least 25kg of pepperoni"
    
  if leftover_pepper <= 30:
    print "You have %d kilograms of peppers left"  % (leftover_pepper)
    print "You need to restock at least 20kg of peppers"
  
  if leftover_ham <= 50:
    print "You have %d kilograms of ham left"  % (leftover_ham)
    print "You need to restock at least 20kg of ham"
  
  if leftover_bacon <= 40:
    print "You have %d kilograms of bacon left"  % (leftover_bacon)
    print "You need to restock at least 30kg of bacon"
  
  if leftover_mushrooms <= 40:
    print "You have %d kilograms of mushrooms left"  % (leftover_mushrooms)
    print "You need to restock at least 30kg of ham"
  
  if leftover_pineapple <= 6:
    print "You have %d large cans of pineapple left"  % (leftover_pineapple)
    print "You need to restock at least 4 large cand of pineapple"
  
  if leftover_sausage <= 30:
    print "You have %d kilograms of sausage left"  % (leftover_sausage)
    print "You need to restock at least 30kg of sausage"
  
  if leftover_onions <= 20:
    print "You have %d kilograms of onions left"  % (leftover_onions)
    print "You need to restock at least 20kg of onions"
  
  if leftover_olives <= 20:
    print "Your have %d kilograms of olives left"  % (leftover_olives)
    print "You need to restock at least 10kg of olives"
  
  if leftover_tomatoes <= 35:
    print "You have %d kilograms of tomatoes left"  % (leftover_tomatoes)
    print "You need to restock at least 20kg of tomatoes"
  
  if leftover_drinks <= 90:
    print "Your have %d cans of drinks left"  % (leftover_drinks)
    print "You need to restock at least 70 cans of drinks"
  
  if leftover_chicken_topping <= 30:
    print "Your have %d kilograms of chicken left"  % (leftover_chicken_topping)
    print "You need to restock at least 20kg of chicken"
  
  if leftover_chicken_wings <= 15:
    print "Your have %d large boxes of chicken wings left"  % (leftover_chicken_wings)
    print "You need to restock at least 15 large boxes of chicken wings"

  print "These are your sales this week"
  print "Today is %s-%s-%s" % (now.year, now.month, now.day)
  print "You made $%.2f this week" % (grand_total)
  
  exit = raw_input("Would you like to exit the app? yes/no:")
  if exit in ['yes', 'y', 'Y', 'YES']:
    print "HAVE A NICE DAY!"
    break
  else:
    print "Let's Continue."
    continue
    