Str = input("Enter a string: ")
words = Str.split()
lower = []
upper = []
for char in Str:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)
sortedstring = ''.join(lower + upper)
print("\n Arranging characters by giving precedence to lower case:")
print(sortedstring)
