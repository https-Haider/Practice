def add_time(start, duration, day=None):
    # Days list for optional day handling
    days = [
        "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"
    ]

    # Split start time
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(":"))

    # Convert start time to 24-hour format
    if period == "PM" and start_hour != 12:
        start_hour += 12
    elif period == "AM" and start_hour == 12:
        start_hour = 0

    # Duration split
    dur_hour, dur_minute = map(int, duration.split(":"))

    # Calculate total minutes
    start_total = start_hour * 60 + start_minute
    duration_total = dur_hour * 60 + dur_minute

    new_total = start_total + duration_total

    # Calculate days passed
    days_later = new_total // (24 * 60)

    # New time in minutes of current day
    new_total = new_total % (24 * 60)

    new_hour = new_total // 60
    new_minute = new_total % 60

    # Convert back to 12-hour format
    if new_hour >= 12:
        new_period = "PM"
    else:
        new_period = "AM"

    if new_hour == 0:
        new_hour = 12
    elif new_hour > 12:
        new_hour -= 12

    result = f"{new_hour}:{new_minute:02d} {new_period}"

    # Add day if provided
    if day:
        day = day.capitalize()
        
        if day in days:
            day_index = days.index(day)
            new_day = days[(day_index + days_later) % 7]
            result += f", {new_day}"

    # Add next day / days later text
    if days_later == 1:
        result += " (next day)"
    elif days_later > 1:
        result += f" ({days_later} days later)"

    return result