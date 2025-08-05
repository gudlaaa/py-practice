score = int(input("Enter student score"))

grade = ''

if score > 89 and score < 101:
    grade = 'A'
elif score > 79 and score < 90:
    grade = 'B'
elif score > 69 and score < 80:
    grade = 'C'
elif score > 59 and score < 70:
    grade = 'D'
else:
    grade = 'E'


print(grade)