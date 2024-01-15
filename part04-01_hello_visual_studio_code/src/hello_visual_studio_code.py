# Write your solution here
while True:
    text = str(input("Editor: "))
    if text.lower() == "visual studio code":
        print("an excellent choice!")
        break
    elif text.lower() == "word" or text.lower() == "notepad":
        print("awful")
    else:
        print("not good")