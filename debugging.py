# There is something wrong with the arguments the function is getting; a precondition is violated.

# When a function expects a specific input to perform computations.

# Precondition: The function expects a numeric value. If the function is called with an argument other than numeric (e.g. boolean, string, etc.), we get unexpected behavior.
# Postcondition: The function should return "True" if there's enough stock, "False" if otherwise.
# current_stock = 10

# def is_available(quantity):
#     if (quantity <= current_stock):
#         return true

# print(is_available(False))
# # There is something wrong with the function; a postcondition is violated.
# # When not all cases were handled by the function resulting to unexpected behavior.

# # Postcondition: The function should return either "True" or "False"

# current_stock = 10

# def is_available(quantity):
#     if (quantity <= current_stock):
#         return True

# print(is_available(1))

# # There is something wrong with the return value or the way it is being used.
# # When the function executes and returns an unexpected value.
# # Postcondition: The function should return either "True" or "False"
current_stock = 0

def is_available(quantity):
    if (quantity <= current_stock):
        return True

    return False

print(is_available(5))
