# Write your solution here
list = []
while True:
    word = str(input("Word: "))
    if word in list:
        print(f"You typed in {len(list)} different words")
        break
    list.append(word)
    