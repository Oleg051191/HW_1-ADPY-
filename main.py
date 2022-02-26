from application.salary import get_employees
from application.db.people import calculate_salary
import datetime as dt


if __name__ == '__main__':
    get_employees()
    calculate_salary()
    print(dt.datetime.now(tz=None))