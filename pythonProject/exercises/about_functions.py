def multiply(number_1, number_2):
    return number_1 * number_2


print("Multiplying integers: " + str(multiply(5, 5)))
print("Multiplying floats: " + str(multiply(1.55, 5.5)))

def multiply_hint(number_1: int, number_2: str):
    return number_1 * number_2


print("\n")
print("Multiplying integers with hint: " + str(multiply_hint(5, 5)))
print("Multiplying floats with hint: " + str(multiply_hint(1.55, 5.5)))