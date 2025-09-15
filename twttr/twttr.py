x = ["a", "e", "i", "o", "u"]

y = input("Input: ")

print("Output: ", end="")

for c in y:
    if c.lower() not in x:
        print(c, end="")
