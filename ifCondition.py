# If statement
a = 33
b = 200
if b > a:
    print("b is greater then a")

# elif statement
a = 37
b = 37
if b > a:
    print("b is greater then a")
elif a == b:
    print("a and b is equal")

# else statement
a = 200
b = 30
if b > a:
    print("b is greater then a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater theb b")

# short hand if
a = 330
b = 300
if a > b:
    print("a is greater")

# short hand if....else
a = 2
b = 220
print("A") if a > b else print("B")

# multiple statements
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# And keyword
a = 200
b = 30
c = 500
if a > b and c > a:
    print("Both are true")

# Or keyword
a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one is true")

# nested if else
x = 41
if x > 10:
    print("Above ten, ")
    if x > 20:
        print("aslo above 20.")
    else:
        print("but not above 20.")
