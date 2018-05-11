# 1 fl oz = 0.125 cups

# get drink name and create filename
drink_name = input("Drink name: ")
filename = drink_name + ".txt"

# get batch size
try:
    batch_size = float(input("Batch size (in gallons): "))
except:
    print("Batch size must be a float or integer")
# convert to ounces, 1 gal = 128 ounces
batch_ounces = batch_size * 128
# conversion customization
convert_to_cups = input("Convert to cups? 'y/n': ")
if convert_to_cups == 'y':
    conversion = 0.125
    unit = "cups"
else:
    conversion = 1
    unit = "oz"

# dictionary to add ingredients to
ingredients = {}

print("Now let's add the ingredients and amounts (oz) for one drink.")
while True:
    ingredient_name = input("Ingredient name (enter 'q' when done adding): ")
    if ingredient_name == 'q':
        break
    try:
        ingredient_amount = float(input("amount in ounces: "))
    except:
        print("Amount must be a float or integer.")
        continue

    # add to ingredient dict
    ingredients[ingredient_name] = ingredient_amount

# now get total size of one drink
drink_size = 0
for ingredient, amount in ingredients.items():
    drink_size += amount
print("One " + drink_name + " = " + str(drink_size) + " oz")

# how many drinks in one batch
multiplier = batch_ounces / drink_size

# dictionary for final totals
batch_ingredients = {}

for ingredient, amount in ingredients.items():
    new_amount = (amount * multiplier) * conversion
    batch_ingredients[ingredient] = new_amount

with open(filename, 'w') as f:
    f.write(drink_name + "\n\n" + "makes " + str(batch_size) + " gallons\n\n")
    for ingredient, amount in batch_ingredients.items():
        # round to two decimal points
        amount = "{:.2f}".format(amount)
        line = ingredient + "\t" + amount + " " + unit + "\n"
        f.write(line)

print("Batch recipe saved to: " + filename)