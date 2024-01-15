# Write your solution here
my_list = []
i = 0
j = 1
while True:
    print(f"The list is now {my_list}")
    choice = str(input("a(d)d, (r)emove or e(x)it: "))
    if choice == "d":
       item = len(my_list) + 1
       my_list.append(item)
    elif choice == "r":
       my_list.pop(len(my_list) - 1)
    elif choice == "x":
        print("Bye!")
        break