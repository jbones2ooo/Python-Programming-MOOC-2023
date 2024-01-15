# Write your solution here
items = []
number = int(input("How many items: "))
i = 1

while i <= number:
    x = int(input(f"Item {i}: "))
    items.append(x)
    i += 1

print(items)