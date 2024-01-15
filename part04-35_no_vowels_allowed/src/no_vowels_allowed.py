# Write your solution here
def no_vowels(string: str):
    vowels = "aeiouAEIOU"
    for i in vowels:
        string = string.replace(i, "")
    return string

if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))