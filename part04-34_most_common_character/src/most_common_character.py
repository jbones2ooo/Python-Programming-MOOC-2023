# Write your solution here
def most_common_character(sentence: str):
    highest = 0
    for i in sentence:
        if sentence.count(i) > highest:
            highest = sentence.count(i)
    for i in sentence:
        if sentence.count(i) == highest:
            highest = i
    return highest

if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))