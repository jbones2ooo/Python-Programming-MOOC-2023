# Copy here code of line function from previous exercise
def line(num, text):
    if text == "":
        text = "*"
    print(text[0] * num)
def square(size, character):
    i = 0
    # You should call function line here with proper parameters
    while i < size:
        line(size, character)
        i += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")