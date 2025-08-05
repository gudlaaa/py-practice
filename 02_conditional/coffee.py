# Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

order = 'small'
extra = True

if extra:
    coffee = order + " Coffe with Extra Short"
else:
    coffee = order + " Coffee"

print(coffee)