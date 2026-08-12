from student_grade_sheet import StudentGradeSheet
import student_util


def analyze_students(filename):

    highest_score = float("-inf")
    highest_name = ""
    highest_grade = ""

    lowest_score = float("inf")
    lowest_name = ""
    lowest_grade = ""

    class_total = 0.0
    student_count = 0

    passed = []
    failed = []
    bright_students = []

    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        print("=========================================")
        print("STUDENT GRADE ANALYZER".center(41, "="))
        print("=========================================")
        print()

        for line in lines[1:]:

            try:
                line = line.strip()

                if not line:
                    continue

                data = line.split(",")

                name = data[0]
                math = float(data[1])
                python = float(data[2])
                ai = float(data[3])
                age = int(data[4])

                # Create Student object
                student = StudentGradeSheet(
                    name,
                    math,
                    python,
                    ai,
                    age
                )

                # Use functions from student_util.py
                total_score = student_util.calculate_total(
                    student.math,
                    student.python,
                    student.ai
                )

                average_score = student_util.calculate_average(
                    total_score
                )

                grade = student_util.calculate_grade(
                    average_score
                )

                result = student_util.calculate_result(
                    average_score
                )

                # Find highest scorer
                if total_score > highest_score:
                    highest_score = total_score
                    highest_name = student.name
                    highest_grade = grade

                # Find lowest scorer
                if total_score < lowest_score:
                    lowest_score = total_score
                    lowest_name = student.name
                    lowest_grade = grade

                # Class total
                class_total += total_score
                student_count += 1

                # Passed / Failed
                if result == "PASSED":
                    passed.append(student.name)
                else:
                    failed.append(student.name)

                # Bright students
                if average_score >= 90:
                    bright_students.append(student.name)

                # Display student information
                print(f"Name: {student.name}")
                print(f"Age: {student.age}")
                print(f"Math: {student.math:.2f}")
                print(f"Python: {student.python:.2f}")
                print(f"AI: {student.ai:.2f}")
                print(f"Total: {total_score:.2f}")
                print(f"Average: {average_score:.2f}")
                print(f"Grade: {grade}")
                print(f"Result: {result}")
                print("-----------------------------------------")

            except (ValueError, IndexError):
                print("Error: Invalid student data.")
                print("-----------------------------------------")

        # Class summary
        if student_count > 0:

            class_average = class_total / student_count

            print()
            print("CLASS SUMMARY")
            print("=========================================")

            print(
                f"Highest Scorer: {highest_name} "
                f"-> {highest_score:.2f} ({highest_grade})"
            )

            print(
                f"Lowest Scorer: {lowest_name} "
                f"-> {lowest_score:.2f} ({lowest_grade})"
            )

            print(f"Class Total: {class_total:.2f}")
            print(f"Class Average: {class_average:.2f}")

            print(
                f"Passed: "
                f"{', '.join(passed) if passed else 'None'}"
            )

            print(
                f"Failed: "
                f"{', '.join(failed) if failed else 'None'}"
            )

            print(
                f"Bright Students: "
                f"{', '.join(bright_students) if bright_students else 'None'}"
            )

    except FileNotFoundError:
        print(f"Error: {filename} was not found.")


if __name__ == "__main__":
    analyze_students("student_list.txt")