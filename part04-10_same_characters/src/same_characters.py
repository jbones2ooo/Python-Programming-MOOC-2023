# Write your solution here
def same_chars(text, x1, x2):
    if x1 >= len(text) or x2 >= len(text):
        return False
    return text[x1] == text[x2]
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 10))