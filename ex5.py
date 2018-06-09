name = 'Zed A. Shaw'
age = 35     # years
height = 74  # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
height_cm = 74 * 2.54           # height in centimeters
weight_kg = 180 * 0.45359237    # weight in kilograms

print(f"Let's talk about {name}.")
print(f"He's {height_cm} centimeters tall.")
print(f"He's {height} inches tall.")
print(f"He's {weight_kg} kilograms heavy.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

total = age + height_cm + weight_kg
print(f"If I add {age}, {height_cm}, and {weight_kg} I get {total}.")
