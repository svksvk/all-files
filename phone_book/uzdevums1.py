import json

file = open('so_big_list_of_students.json', 'r')
data = json.load(file)
file.close()

for s in data['Students']:
    print(f"{s['FirstName']} {s['LastName']} ({s['Grade']})")

# UZDEVUMS 2 - VIDĒJAIS ARITMĒTISKAIS
# Risinājums 1
grade_sum = 0
for s in data['Students']:
    grade_sum += int(s['Grade'])

average_grade = grade_sum / len(data['Students'])
print(f"Student count is {len(data['Students'])}")
print(f"Average grade is {average_grade}")
# Risinājums 2
grade_list = []
for s in data['Students']:
    grade_list.append(int(s['Grade']))
print(f"Student count is {len(grade_list)}")
print(f"Average grade is {sum(grade_list) / len(grade_list)}")

# UZDEVUMS 3 - KATRA DZIMUMA VIDĒJAIS ARITMĒTISKAIS
grade_list = []
for s in data['Students']:
    grade_list.append(int(s['Male']))
    grade_list.append(int(s['Female']))
print(f"Student count is {len(grade_list)}")
print(f"Average grade is {sum(grade_list) / len(grade_list)}")