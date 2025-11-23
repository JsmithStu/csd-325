import json

STUDENT_FILE = "student.json"


def print_student_list(students):
    """Loop through the student list and print each student."""
    for student in students:
        last_name = student["L_Name"]
        first_name = student["F_Name"]
        student_id = student["Student_ID"]
        email = student["Email"]

        print(f"{last_name}, {first_name} : ID = {student_id} , Email = {email}")


def main():
    # 1. Load the JSON file into a Python list
    with open(STUDENT_FILE, "r") as infile:
        student_list = json.load(infile)

    # 2. Print original list
    print("Original Student list:")
    print_student_list(student_list)
    print()

    # 3. Add YOUR record to the list
    new_student = {
        "F_Name": "Johnathan",
        "L_Name": "Smith",
        "Student_ID": 99999,  # fictional ID
        "Email": "johnathan.smith@example.com"
    }

    student_list.append(new_student)

    # 4. Print updated list
    print("Updated Student list (with my record added):")
    print_student_list(student_list)
    print()

    # 5. Dump updated list back into student.json
    with open(STUDENT_FILE, "w") as outfile:
        json.dump(student_list, outfile, indent=4)

    print("student.json file was updated.")


if __name__ == "__main__":
    main()