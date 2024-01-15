# Write your solution here
def palindromes(word):
    for i in range(0, int(len(word)/2)):
        if word[i] != word[len(word) - i - 1]:
            return False
    return True

while True:
    user = str(input("Please type in a palindrome:"))
    if palindromes(user):
        print(f"{user} is a palindrome!")
        break
    print("that wasn't a palindrome")
    
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
