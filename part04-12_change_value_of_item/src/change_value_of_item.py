# Write your solution here
my_list = [1,2,3,4,5]
while True:
    list_index = int(input("Index: "))
    if list_index == -1:
        break
    if list_index < 0 or list_index >= len(my_list):
        print("Index is outside of the range of the list")
        continue
    new_value = int(input("New value: "))
    my_list[list_index] = new_value
    print(my_list)