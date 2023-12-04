#TODO
#cases:
# - year more than actual (2024)
# - 0 exceptions
# - months exceptions (more than 12)
# - days exceptions (30-31 >)
# - february cases
# - etc

from collections import defaultdict
from datetime import datetime, timedelta

def get_next_weekday(d, weekday):
    days_until_target = (weekday - d.weekday() + 7) % 7
    return d + timedelta(days=days_until_target)

def get_birthdays_per_week(users):
    today = datetime.today().date()
    next_week_start = get_next_weekday(today, 0) + timedelta(weeks=1)
    days_of_week = defaultdict(list)

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days
        day_of_week = (today + timedelta(days=delta_days)).strftime("%A")

        if delta_days < 7:
            days_of_week[day_of_week].append(name)
        elif delta_days == 7:
            next_birthday_weekday = birthday_this_year.weekday()
            if next_birthday_weekday == 6:  # If birthday falls on Saturday
                days_of_week['Monday'].append(name)
            elif next_birthday_weekday == 7:  # If birthday falls on Sunday
                days_of_week['Monday'].append(name)

    for day, names in days_of_week.items():
        if day == 'Sunday' and names:
            print(f"Monday: {', '.join(names)}")
        elif day == 'Saturday'and names:
            print(f"Monday: {', '.join(names)}")
        elif names:
            print(f"{day}: {', '.join(names)}")

# Tests examples
users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 12, 8)},
    {"name": "Jan Koum", "birthday": datetime(2024, 12, 9)},
]

get_birthdays_per_week(users)