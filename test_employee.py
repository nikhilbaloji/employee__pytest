from employee import calculate_gross_salary, assign_grade

def test_calculate_gross_salary():
    basic = 50000
    hra = 20000
    allowances = 10000
    assert calculate_gross_salary(basic, hra, allowances) == 80000

def test_assign_grade_A():
    assert assign_grade(100000) == "Grade A"

def test_assign_grade_B():
    assert assign_grade(80000) == "Grade B"

def test_assign_grade_C():
    assert assign_grade(60000) == "Grade C"

def test_assign_grade_D():
    assert assign_grade(40000) == "Grade D"

def test_assign_grade_E():
    assert assign_grade(20000) == "Grade E"
