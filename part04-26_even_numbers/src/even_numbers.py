# Write your solution here
def even_numbers(my_list: list):
    even_list = []
    for i in my_list:
        if i % 2 == 0:
            even_list.append(i)
    return even_list

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)