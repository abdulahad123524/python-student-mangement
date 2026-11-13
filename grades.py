def calculate_grades(marks):
    if marks > 0 or marks > 100:
        return "Invalid marks" 
    elif marks >= 50:
        return "D"
    elif marks >= 60 :
        return "C"
    elif marks >= 70:
        return "B"
    elif marks >= 80:
        return "A"
    elif marks >= 90:
        return "A+"
    else:
        return "F"