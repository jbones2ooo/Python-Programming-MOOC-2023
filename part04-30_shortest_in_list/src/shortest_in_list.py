# Write your solution here
def shortest(my_list: list):
    short = my_list[0]
    for i in my_list:
        if len(i) <= len(short):
            short = i
    return short

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = shortest(my_list)
    print(result)