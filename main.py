def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

# -------------------------
# NEW FUNCTIONS (Integration)
# -------------------------

def calculate_total(marks):
    return sum(marks)   # ✔ back to integer

def apply_tax(total, tax_rate):
    return total + (total * tax_rate)
# -------------------------
# WORKFLOW FUNCTIONS
# -------------------------


def calculate_average(total, subjects):
    return total / subjects

def assign_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "F"