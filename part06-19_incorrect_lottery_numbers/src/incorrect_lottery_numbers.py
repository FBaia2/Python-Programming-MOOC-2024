def filter_incorrect():
    with open("lottery_numbers.csv", "r") as infile, open("correct_numbers.csv", "w") as outfile:
        for line in infile:
            # Split the line into week and numbers
            parts = line.strip().split(";")
            print(parts)
            if len(parts) != 2:
                continue  # Skip lines without exactly one semicolon
            week, numbers = parts
            # Check the week part
            if not week.startswith("week ") or not week[5:].isdigit():
                continue  # Skip lines where week number is incorrect
            # Check the numbers part
            numbers = numbers.split(",")
            if len(numbers) != 7:
                continue  # Skip lines with too few or too many numbers
            try:
                numbers = [int(num) for num in numbers]
            except ValueError:
                continue  # Skip lines with non-integer numbers
            if any(num < 1 or num > 39 for num in numbers):
                continue  # Skip lines with numbers out of range
            if len(numbers) != len(set(numbers)):
                continue  # Skip lines with duplicate numbers
            # If we made it here, the line is correct
            outfile.write(line)

if __name__ == "__main__":
    filter_incorrect()
