import urllib.request
import json

def retrieve_all():
    with urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses") as url:
        data = json.loads(url.read().decode())
    print("[")
    for course in data:
        if isinstance(course, dict) and 'fullName' in course and 'name' in course and 'year' in course and 'exercises' in course:
            sum_exercises = sum(course['exercises'])
            print("    ",(course['fullName'], course['name'], course['year'], sum_exercises))
        else:
            print("Course is not a dictionary or does not have the expected keys.")
    print("]")

if __name__=="__main__":
    retrieve_all()
