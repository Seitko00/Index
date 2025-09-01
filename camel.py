x = input("camelCase: ")


result = ""
for i in range(len(x)):
    if x[i].isupper() and i != 0:
        result += "_" + x[i].lower()
    else:
        result += x[i].lower()

print(f"snake_case: {result}")