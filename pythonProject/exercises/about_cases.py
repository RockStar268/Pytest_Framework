def print_guesses_left(guesses_made: int):
    match guesses_made:
        case 0:
            return "Please take your first guess."
        case 1:
            return "1 guess made, 2 guesses left!"
        case 2:
            return "2 guesses made, 1 guess left!"
        case 3 | 5:
            return "You have no more guesses left!"
        case _ if guesses_made > 8:
            return "Greater than feature is triggered!"
        case _:
            return "You have taken more than 3 guesses. Do not cheat!"

# case match
print(print_guesses_left(0))
print(print_guesses_left(1))
print(print_guesses_left(2))
print("====")

# 3 or 5
print(print_guesses_left(3))
print(print_guesses_left(5))
print("====")

# wildcard
print(print_guesses_left(4))
print(print_guesses_left(8))
print("====")

# triggering if statement
print(print_guesses_left(9))

