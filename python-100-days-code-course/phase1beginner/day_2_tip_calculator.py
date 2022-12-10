# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇
print("Welcome to the tip calculator")

subtotal = float(input("What was the total bill? "))
percent_tip = int(input("What percentage tip would you like to leave? "))
num_people = int(input("How many people split the bill? "))

total = ((100 + percent_tip) / 100) * subtotal

split_amt = total / num_people
print(f"Each person should pay: {split_amt:.2f}")
