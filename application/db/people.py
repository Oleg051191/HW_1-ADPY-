
Bookkeeping = {'google': {'google_ep1' : 500, 'google_ep2' : 700, 'google_ep3' : 1000, 'google_ep4' : 2000,'google_ep5' : 3000,
          'google_ep6' : 5000, 'google_ep7' : 8000, 'google_ep8' : 12000, 'google_ep9' : 23000, 'google_ep10' : 43000,
          'google_ep11' : 72000, 'google_ep12' : 120000, 'google_ep13' : 110000, 'google_ep14' : 133000, 'google_ep15' : 150000},
               'yandex': {'employee_1' : 500, 'employee_2' : 700, 'employee_3' : 1000, 'employee_4' : 2000,'employee_5' : 3000,
          'employee_6' : 5000, 'employee_7' : 7000, 'employee_8' : 10000, 'employee_9' : 20000, 'employee_10' : 40000,
          'employee_11' : 70000, 'employee_12' : 100000, 'employee_13' : 110000, 'employee_14' : 130000, 'employee_15' : 150000}
               }

def calculate_salary():
    for company_name, company_salary in Bookkeeping.items():
        total_salary = 0
        for salary in company_salary.values():
            total_salary += salary
        avg_salary = round(total_salary / len(company_salary), 2)
        print(f"Cредняя зарплата в '{company_name}' - {avg_salary}")


if __name__ == '__main__':
    calculate_salary()