def subtract_values(start_value, *x):  # x = args
    end_value = start_value
    for arg in x:
        end_value -= arg
    return end_value


print(subtract_values(100, 55, 22, 33, 44))

