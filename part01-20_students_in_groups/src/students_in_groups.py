students = int(input("How many students on the course? "))
group_size = int(input("Desired group size? "))

# Calculate the number of full groups
full_groups = students // group_size

# Check if there is a last group with fewer members
last_group = students % group_size

# If there is a last group, increment the number of groups
if last_group > 0:
    full_groups += 1

print(f"Number of groups formed: {full_groups}")
