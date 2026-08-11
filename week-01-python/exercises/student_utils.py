def calculate_total(sub1, sub2, sub3):
    total = sub1 + sub2 + sub3
    return total

def calculate_average(total):
    # total = calculate_total(sub1, sub2, sub3)
    average = total/3
    return average

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

def calculate_result(grade):
    if grade == "F":
        return "FAILED"
    else:
        return "PASSED"

def calculate_Total(math, python, ai):
    return math + python + ai


def calculate_Average(total):
    return total / 3


def calculate_Grade(average):
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


def calculate_Result(grade):
    if grade == "F":
        return "FAILED"
    else:
        return "PASSED"