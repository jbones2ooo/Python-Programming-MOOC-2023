# Write your solution here
def all_the_longest(my_list: list):
    long_list = []
    longest = 0
    for i in my_list:
        if len(i) > longest:
            longest = len(i)
    for i in my_list:
        if len(i) == longest:
            longest == i
            long_list.append(i) 
    return long_list

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']