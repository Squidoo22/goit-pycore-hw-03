from datetime import datetime, timedelta

def is_weekend(date):
    return date.weekday() >= 5

def next_workday(date):
    while is_weekend(date):
        date += timedelta(days=1)
    return date

def get_upcoming_birthdays(users):
    filtered_users = []
    current_date = datetime.today().date()

    for user in users:
        birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        birthday_date_this_year = birthday_date.replace(year=current_date.year)

        if current_date > birthday_date_this_year:
            next_birthday = birthday_date.replace(year=current_date.year + 1)
        else:
            next_birthday = birthday_date_this_year

        if is_weekend(next_birthday):
            next_birthday = next_workday(next_birthday)

        days_left = (next_birthday - current_date).days

        if days_left <= 7:
            updated_user = {
                "name": user["name"],
                "congratulation_date": next_birthday.strftime("%Y.%m.%d")
            }
            filtered_users.append(updated_user)

    return filtered_users

users = [
    {"name": "John Doe", "birthday": "1985.07.23"},
    {"name": "Jane Smith", "birthday": "1990.07.21"},
    {"name": "Vasya Pupkin", "birthday": "1990.07.12"},
    {"name": "Emily Blank", "birthday": "1990.07.08"},
    {"name": "Lionel Messi", "birthday": "1990.05.07"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список приветствий на этой неделе:", upcoming_birthdays)
