def get_exam_results_template(score: int):
    if score == int(score):
        return "Your input is a integer, but got converted into a string: " + str(score)
    else:
        return "Your input is not a integer."


print(get_exam_results_template(88))
print(get_exam_results_template(88.8))

def get_exam_results(score):
    if score > 99:
        return "Well done!"
    elif score > 65:
        return "You are passed"
    else:
        return "Too bad, you failed"


print("\n")
print(get_exam_results(100))
print(get_exam_results(99))
print(get_exam_results(65))