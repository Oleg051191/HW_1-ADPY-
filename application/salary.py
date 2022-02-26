
company = {'google': ['employees_1', 'employees_2', 'employees_3', 'employees_4'],
           'yandex': ['employees_1', 'employees_2', 'employees_3', 'employees_4', 'employees_5', 'employees_6']}

def get_employees():
    for c_name, c_epl in company.items():
        print(f"В компании '{c_name}' - {len(c_epl)} работника")


if __name__ == '__main__':
    get_employees()