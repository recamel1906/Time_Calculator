# Return new time based on start time and duration in HH:MM format
def add_time(start, duration, day=None):
    # Split start time into different strings
    start_time = split_time(start)

    # Split duration into different strings
    duration_time = split_time(duration)

    # Convert 'numbers' in start_time into integers
    start_time = [int(start_time[0]), int(start_time[1]), start_time[2]]

    # Convert 'numbers' in start_time into integers
    duration_time = [int(duration_time[0]), int(duration_time[1])]

    # Compute new time
    new_hour = start_time[0] + duration_time[0]
    new_minute = start_time[1] + duration_time[1]

    # Set up dictionary to denote days of the week
    days_of_week = {'Sunday': 1, 'Monday': 2, 'Tuesday': 3, 'Wednesday': 4,
                    'Thursday': 5, 'Friday': 6, 'Saturday': 7}

    # Recognize day number in days_of_week from known input day
    current_day_number = recognizeDays(days_of_week, day)

    next_day = ""
    new_day_of_week = ""
    new_time_of_day = start_time[-1]
    if new_hour == start_time[0] and new_minute == start_time[1]:
        new_time_of_day = start_time[-1]
    elif duration[0] == 24:
        new_time_of_day = change_time_of_day(new_hour, start_time[-1])
    elif 12 <= new_hour < 30:
        new_hour = new_hour - 12
        new_time_of_day = change_time_of_day(new_hour, start_time[-1])
        next_day = "(next day)"
        if day is None:
            pass
        else:
            new_day_of_week = extractKeyByValue(days_of_week, (current_day_number + 1) % 7)
    elif 30 < new_hour < 150:
        new_hour = new_hour % 24
        new_time_of_day = change_time_of_day(new_hour, start_time[-1])
        days_later = round((start_time[0] + duration_time[0]) / 24 + (start_time[1] + duration_time[1]) / 1440)
        next_day = "(" + str(days_later) + " days later)"
        if day is None:
            pass
        else:
            new_day_of_week = extractKeyByValue(days_of_week, current_day_number + days_later)
            # if current_day_number + days_later > 7:
            #     new_day_of_week = extractKeyByValue(days_of_week, (current_day_number + days_later) % 7)
            # else:
            #     new_day_of_week = extractKeyByValue(days_of_week, current_day_number + days_later)
    elif new_hour > 200:
        new_hour = (new_hour % 24) - 12
        new_time_of_day = change_time_of_day(new_hour, start_time[-1])
        days_later = round((start_time[0] + duration_time[0]) / 24 + (start_time[1] + duration_time[1]) / 1440)
        next_day = "(" + str(days_later) + " days later)"
        if day is None:
            pass
        else:
            if current_day_number + days_later > 7:
                new_day_of_week = extractKeyByValue(days_of_week, (current_day_number + days_later) % 7)
            else:
                new_day_of_week = extractKeyByValue(days_of_week, current_day_number + days_later)
    else:
        # new_time_of_day = 'PM'
        next_day = ""
        if day is None:
            new_day_of_week = ""
        else:
            new_day_of_week = day

    if new_minute >= 60:
        new_hour += 1
        new_minute = new_minute - 60
        new_time_of_day = change_time_of_day(new_hour, start_time[-1])
    if new_hour > 12:
        new_hour = new_hour - 12
        new_time_of_day = change_time_of_day(new_hour, start_time[-1])
    if new_minute < 10:
        new_minute = '0' + str(new_minute)
    else:
        pass

    new_time = [str(new_hour), str(new_minute), new_time_of_day, next_day, str(new_day_of_week)]

    # Convert results into string
    if day is None:
        new_time = convert_time_to_string(new_time, day_included=False)
    else:
        new_time = convert_time_to_string(new_time, day_included=True)

    return new_time


# Split a time into different strings
def split_time(time_string):
    if 'AM' or 'PM' in time_string:
        return time_string.split(":")[0:-1] + time_string.split(":")[-1].split()
    else:
        return time_string.split(":")[0:-1]


# Change time to AM or PM
def change_time_of_day(hour, input_time_of_day):
    new_time_of_day = ''
    if hour > 12 and input_time_of_day == 'AM':
        new_time_of_day = 'PM'
    if hour > 12 and input_time_of_day == 'PM':
        new_time_of_day = 'AM'
    else:
        new_time_of_day = input_time_of_day
    return new_time_of_day


# Convert new time into HH:MM format
def convert_time_to_string(time, day_included=False):
    if day_included:
        return str(time[0] + ":" + time[1] + " " + time[2] + ", " + time[4] + " " + time[3]).strip()
    else:
        return str(time[0] + ":" + time[1] + " " + time[2] + " " + time[3]).strip()


# Convert days with upper or lower case letters
def recognizeDays(daysDict, input_day):
    day_number = 0
    if input_day is not None:

        # Check to see if input_day is uppercase in 1st letter and other letters
        # are lowercase
        day_split = input_day.split(input_day[0])
        rest_of_day = day_split[-1]  # input day without first letter
        input_day_mod = None
        if input_day[0].islower():
            input_day_mod = input_day[0].upper() + rest_of_day.lower()
        if input_day[0].isupper() and rest_of_day.isupper():
            input_day_mod = input_day[0] + rest_of_day.lower()
        else:
            pass

        # Find where input_day_mod is in dayDict
        if input_day_mod in daysDict.keys():
            day_number = daysDict[input_day_mod]
    else:
        day_number = 0  # there is no specified day

    return day_number


# Extract key of dict by value
def extractKeyByValue(dictionary, value):
    return list(dictionary.keys())[list(dictionary.values()).index(value)]
