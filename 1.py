from datetime import datetime


def get_days_from_today(date: str) -> int | str:
    try:
        if not isinstance(date, str):
            raise ValueError("Input date must be a string in 'YYYY-MM-DD' format.")

        choosen_date = datetime.strptime(date, '%Y-%m-%d')
        current_datetime = datetime.now()

        day_difference = choosen_date - current_datetime

        return day_difference.days

    except ValueError as e:
        return str(e)


print(f"difference in {get_days_from_today('2024-10-09')} days")
print(f"Non valid example - {get_days_from_today(20241009)}")
print(f"Invalid date example - {get_days_from_today('invalid-date')}")
