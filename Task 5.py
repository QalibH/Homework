# Financial Industry:

def calc_budget():
    expenses = float(input("Enter total monthly expenses: $"))
    income = float(input("Enter total monthly income: $"))
    
    remaining_budget = income - expenses
    
    return remaining_budget

budget = calc_budget()
print(f"Remaining budget for the month: ${budget}")


# Healthcare Industry:

def calculate_bmi(weight, height):
    bmi = weight / (height**2)
    return bmi

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi >= 18.5 and bmi < 25:
        return "Normal weight"
    elif bmi >= 25 and bmi < 30:
        return "Overweight"
    else:
        return "Obese"

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
bmi = calculate_bmi(weight, height)
bmi_category = get_bmi_category(bmi)

print("Your BMI is: {:.2f}".format(bmi))
print("BMI Category: {}".format(bmi_category))


# Education Industry:

def get_scores():
    scores = []
    subjects = ['Math', 'Chemistry', 'Physics', 'Physical training', 'English']

    for subject in subjects:
        score = float(input(f'Enter score for {subject}: '))
        scores.append(score)

    return scores

def calculate_gpa(scores):
    total_score = sum(scores)
    gpa = total_score / len(scores)
    return gpa

def determine_grade(gpa):
    if gpa > 90:
        return 'A'
    elif gpa > 80:
        return 'B'
    elif gpa > 70:
        return 'C'
    elif gpa > 60:
        return 'D'
    else:
        return 'F'

def main():
    scores = get_scores()
    gpa = calculate_gpa(scores)
    grade = determine_grade(gpa)

    print(f'GPA: {gpa}')
    print(f'Letter Grade: {grade}')

if __name__ == '__main__':
    main()
