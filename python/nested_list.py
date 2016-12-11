'''
Nested Lists
Given the names and grades for each student in a Physics class of students, store 
them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, 
order their names alphabetically and print each name on a new line.
Input: 
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
Output: 
Berry
Harry
'''


def main():
    # if __name__ == '__main__':
    names_and_grades = []
    names_and_grades = get_data(names_and_grades)
    name_list = get_lowest_grades(names_and_grades)
    printing(name_list)


def get_data(names_and_grades):
    students = int(input())
    for item in range(students):
        student_data = []
        name = input()
        score = float(input())
        student_data.append(score)
        student_data.append(name)
        names_and_grades.append(student_data)
    return names_and_grades


def get_lowest_grades(names_and_grades):
    lowest = min(names_and_grades)
    second_lowest_list = []
    for name_grade in names_and_grades:
        if name_grade[0] != lowest[0]:
            second_lowest_list.append(name_grade)

    second_lowest = min(second_lowest_list)
    name_list = []
    for name_grade in second_lowest_list:
        if name_grade[0] == second_lowest[0]:
            name_list.append(name_grade[1])
    return name_list


def printing(name_list):
    name_list = sorted(name_list)
    print("\n".join(name_list))

main()
