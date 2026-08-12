def calculate_total(math, python, ai):
    return math + python + ai


def calculate_average(total):
    return total / 3


def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def calculate_result(average):
    if average >= 60:
        return "PASSED"
    else:
        return "FAILED"