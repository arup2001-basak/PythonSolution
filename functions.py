# function creating
def my_function():
    print("hello from world")


my_function()
print("....................")

# arguments


def my_function(fname):
    print(fname + " Refsnes")


my_function("Email")
my_function("Tobias")
my_function("linus")


# arguments functions
def my_function(*kids):
    print("The youngest child is " + kids[0])


my_function("Emil", "Tobias", "Linus")


# passing list of arguments
def my_function(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# return value


def my_function(x):
    return 5 * x


print(my_function(3))
print(my_function(5))
print(my_function(9))

# Recurssion function


def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
        return result


print("\n\nRecursion Example Results")
tri_recursion(6)
