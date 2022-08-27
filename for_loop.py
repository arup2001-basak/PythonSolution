# for loop
fruits = ["apel", "banana", "cherry"]
for x in fruits:
    print(x)
# looping through string
for x in "banana":
    print(x)

# break statements
for x in fruits:
    print(x)
    if x == "banana":
        break

# continue statements
for x in fruits:
    if x == "banana":
        continue
    print(x)

# range function
for x in range(6):
    print(x)
for x in range(2, 6):
    print(x)

# else in for loop
for x in range(6):
    print(x)
else:
    print("Finally dinished!")

print("...................")
for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("Finally finished!")

print("...................")

# nested loops
add = ["red", "big", "testy"]
fruits = ["appel", "banana", "cherry"]
for x in add:
    for y in fruits:
        print(x, y)
print("...................")


# pass statements
for x in [0, 1, 2]:
    pass
