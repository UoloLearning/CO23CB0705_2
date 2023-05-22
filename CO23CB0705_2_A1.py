fruit_prices = {
    "apple": 80,       # per kilogram
    "banana": 40,      # per dozen
}
apple_rate = fruit_prices["apple"]
print("The rate of apples is:", apple_rate, "INR per kilogram")
banana_rate = fruit_prices["banana"]
print("The rate of bananas is:", banana_rate, "INR per dozen")

fruit_prices["Pineapple"] = 100  #per kilogram

pineapple_rate = fruit_prices["Pineapple"]
print("The rate of pineapple is:", pineapple_rate, "INR per kilogram")
