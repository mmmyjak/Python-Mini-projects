def multiply(a, b):
    return a*b

def divide(a,b):
    return round(a/b, 2)

print("4 ? 3")
a = input("Write the symbol -> ")

# dictionaries
dict_ = {"*": multiply, "/": divide}
if a in dict_:
    print(dict_[a](4, 3))
else:
    print("Error: Wrong Symbol")

#  match case
match a:
    case "*":
        print(multiply(4,3))
    case "/":
        print(divide(4,3))
    case _:
        print("Error: Wrong Symbol")