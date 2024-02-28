count_of_data = 3


def calculate_session_time(load_time_value, exit_time_value) -> float:
    """ Returns session time in minutes. """
    return round(exit_time_value - load_time_value, 2)


def is_invalid_number(value) -> bool:
    """ Returns True if string is a number. """
    try:
        return float(value) < 0
    except ValueError:
        return True


inputs = []
session_times = []

for i in range(count_of_data):
    load_time = input(f"Enter load time in minutes [{i + 1}/{count_of_data}] : ")

    if is_invalid_number(load_time):
        print("Not a valid input, please input number only")
        exit(1)

    exit_time = input(f"Enter exit time in minutes [{i + 1}/{count_of_data}] : ")
    print("-" * 40)

    if is_invalid_number(exit_time):
        print("Not a valid input, please input number only")
        exit(1)

    inputs.append((float(load_time), float(exit_time)))

for index, (load_time, exit_time) in enumerate(inputs):
    session_time = calculate_session_time(load_time, exit_time)

    print(f"Session {index + 1} Duration (in minutes): {session_time}")
    session_times.append(session_time)

average = round(sum(session_times) / len(session_times), 2)
print(f"Average Session Duration (in minutes): {average}")


