all_students = [
    {'name': 'Luke', 'hometown': 'Tatooine', 'favorite_food': 'blue milk'},
    {'name': 'Leia', 'hometown': 'Alderaan', 'favorite_food': 'Coca-Cola'},
    {'name': 'Han', 'hometown': 'Corellia', 'favorite_food': 'grilled cheese'},
    {'name': 'Boba', 'hometown': 'Kamino', 'favorite_food': 'boba tea'}
]


def list_names(student_list: list):
    for student in enumerate(student_list):
        index, item = student
        print(f'{(index + 1)}. {item['name']}')


def get_new_student() -> dict[str, str]():
    student_name = input('Please input a name for the new student: ')
    student_home = input(f"Next, please input {student_name}'s hometown: ")
    student_food = input(f"Next, please input {student_name}'s favorite food: ")
    new_student_list = {'name': student_name, 'hometown': student_home, 'favorite_food': student_food}
    return new_student_list


while True:  # this loop is for getting the action
    user_selected_action = input("Please select which action you'd like to do: add, view, or quit \n>> ")
    if user_selected_action == 'quit':
        break
    elif user_selected_action == 'add':
        all_students.append(get_new_student())
    elif user_selected_action == 'view':  # selecting view and then picking a student
        list_names(all_students)
        while True:  # this loop for picking a student
            student_pick = input('Which student would you like to learn about? ').lower()
            if student_pick.isnumeric() and 0 < int(student_pick) <= len(all_students):
                student_index = int(student_pick) - 1
                break
            elif any(student_pick in name for name in [i['name'].lower() for i in all_students]):
                names = [item['name'].lower() for item in all_students]
                student_index = names.index([e for e in names if student_pick in e][0])
                break
            else:  # user typed number or name
                print('Please pick a valid student')

        print(f'You\'ve selected {all_students[student_index]['name']}')
        while True:  # this loop for selecting a fact category
            student_fact_pick = input(f"Would you rather learn about {all_students[student_index]['name']}'s "
                                      f"favorite food or hometown? >> ").lower()
            if 'home' in student_fact_pick:
                print(f"{all_students[student_index]['name']} is from {all_students[student_index]['hometown']}")
                break
            elif 'food' in student_fact_pick:
                print(f"{all_students[student_index]['name']}'s favorite food is {all_students[student_index]
                ['favorite_food']}")
                break
            else:  # user typed wrong fun fact category
                print('Please pick a valid category')

    else:  # user typed wrong action
        print('Please pick a valid option')

print('Thanks!')