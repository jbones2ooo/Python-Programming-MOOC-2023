# Copy here code of line function from previous exercise and use it in your solution
def line(num, text):
    if text == "":
        text = "*"
    print(text[0] * num)

def shape(len, x1, height, x2):
    i = 1
    j = 1
    while i <= len:
        line(i, x1)
        i += 1
    while j <= height:
        line(len, x2)
        j += 1
        
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")