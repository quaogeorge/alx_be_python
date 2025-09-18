# weather_advice.py

# Step 1: Ask the user about the weather
weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

# Step 2: Use if/elif/else to give clothing recommendations
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")