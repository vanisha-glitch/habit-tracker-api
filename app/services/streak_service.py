from datetime import date, timedelta

def calculate_current_streak(dates):
    if not dates:
        return 0

    completed_set = set(dates)
    streak = 0
    day = date.today()

    while day in completed_set:
        streak += 1
        day -= timedelta(days=1)

    return streak


def calculate_longest_streak(dates):
    if not dates:
        return 0

    longest = 1
    temp = 1

    for i in range(1, len(dates)):
        if dates[i] == dates[i - 1] + timedelta(days=1):
            temp += 1
        else:
            longest = max(longest, temp)
            temp = 1

    return max(longest, temp)