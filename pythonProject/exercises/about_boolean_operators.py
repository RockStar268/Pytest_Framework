def get_exam_results_template(score: int):
    if score == int(score):
        return "Your input is a integer, but got converted into a string: " + str(score)
    else:
        return "Your input is not a integer."


print(get_exam_results_template(88))
print(get_exam_results_template(88.8))

def get_exam_results(score):
    if score > 110 or score <= 65:
        return "Too bad, you failed"
    elif score <= 99:
        return "You are passed"
    else:
        return "Well done!"


print("\n")
print(get_exam_results(100))
print(get_exam_results(99))
print(get_exam_results(65))
print(get_exam_results(66))
print(get_exam_results(111))
print(get_exam_results(110))