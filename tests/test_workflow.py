from main import calculate_total, calculate_average, assign_grade

def test_student_workflow():
    marks = [80, 90, 70]   # total = 240

    total = calculate_total(marks)
    avg = calculate_average(total, len(marks))
    grade = assign_grade(avg)

    assert total == 240
    assert avg == 80
    assert grade == "B"