def cheaters():
    # Initialize dictionaries to store start times and submission times
    start_times = {}
    submission_times = {}

    # Read start times from start_times.csv
    with open("start_times.csv") as start_file:
        for line in start_file:
            name, start_time = line.strip().split(";")
            start_times[name] = start_time

    # Read submission times from submissions.csv
    with open("submissions.csv") as submission_file:
        for line in submission_file:
            name, task, _, submission_time = line.strip().split(";")
            if name in submission_times:
                # Update submission time if it's later than the previous submission
                if submission_time > submission_times[name]:
                    submission_times[name] = submission_time
            else:
                submission_times[name] = submission_time

    # Identify cheaters (students with submission times over 3 hours later than start times)
    cheater_names = []
    for name, start_time in start_times.items():
        start_hour, start_minute = map(int, start_time.split(":"))
        submission_hour, submission_minute = map(int, submission_times.get(name, "00:00").split(":"))

        # Calculate time difference in minutes
        time_difference = (submission_hour - start_hour) * 60 + (submission_minute - start_minute)
        if time_difference > 180:  # 3 hours = 180 minutes
            cheater_names.append(name)

    return cheater_names

# Example usage
if __name__ == "__main__":
    cheaters_list = cheaters()
    print("Cheaters:", cheaters_list)
