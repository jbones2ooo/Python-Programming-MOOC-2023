# Write your solution here
def everything_reversed(my_list):
    newList = []
    i = len(my_list) - 1
    while i >= 0:
        rev = my_list[i]
        newList.append(rev[::-1])
        i -= 1
    return newList
        

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)