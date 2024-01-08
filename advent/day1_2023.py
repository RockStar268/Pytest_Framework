# read data file

with open('Day_1_Trebuchet_data.py', 'r') as file:
    test_data = file.read()

total_value = 0
# filtering 1st available digit and last available digit + combining them together
for line in test_data.split('\n'):
    list_with_digit = [value for value in line if value.isdigit()]
    if list_with_digit:
        new_value = int(list_with_digit[0] + list_with_digit[-1])
        total_value += new_value
print(total_value)




number_mapping = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

total_value1 = 0
for line in test_data.split('\n'):
    # replacing word with number in given number_mapping
    for word, number in number_mapping.items():
        line = line.replace(word, str(number))
    # get number in given dataset
    list_with_digit = [value for value in line if value.isdigit()]
    if list_with_digit:
        new_value1 = int(list_with_digit[0] + list_with_digit[-1])
        total_value1 += new_value1
print(total_value1)
