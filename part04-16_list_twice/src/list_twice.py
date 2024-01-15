# Write your solution here
list = []

while True:
    item = int(input("New item: "))
    list.append(item)
    if item != 0:
        print(f"The list now: {list}")
        print(f"The list in order: {sorted(list)}")
    else:
        break

print("Bye!")
    