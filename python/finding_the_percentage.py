'''
Input:
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
Output: 56.00
'''


def main():
    students_dic = {}
    students_dic, name = get_input_and_put_data_in_dict(students_dic)
    stu_ave = students_dic[name]
    print_average(stu_ave)


def get_input_and_put_data_in_dict(students_dic):
    num = int(input())
    for i in range(num):
        student_data = input().split()
        ''' put data in dictionary (name and point average) '''
        students_dic = data_to_dict(students_dic, student_data)
    name = input()
    return students_dic, name


def data_to_dict(students_dic, student_data):
    points = list(map(float, student_data[1:]))
    average = sum(points) / float(len(points))
    students_dic[student_data[0]] = average
    return students_dic


def print_average(stu_ave):
    print("{0:.2f}".format(stu_ave))


main()
