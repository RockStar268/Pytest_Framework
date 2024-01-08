def count_targeted_character(input_data, expected_character):
    count = 0
    for i in input_data:
        if i == expected_character:
            count += 1
    return count


with open('Day_1_Not_Quite_Lisp', 'r') as file:
    data = file.read()


character = "("
result_count1 = count_targeted_character(data, character)
print(f"Occurence of {character}: {result_count1}")

character = ")"
result_count2 = count_targeted_character(data, character)
print(f"Occurence of {character}: {result_count2}")

delta = abs(result_count1 - result_count2)
print(delta)
