x = input("Say something: ")
y = x.strip().lower()
if y[ :5] == ("hello"):
    print("$0")
elif y[ :1] == ("h"):
    print("$20")
else:
    print("$100")
