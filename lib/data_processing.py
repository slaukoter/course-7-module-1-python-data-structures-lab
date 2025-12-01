# This module contains functions to process student data.

def format_student_data(student):
    """
    Format student data for display.
    Returns a string like:
    "ID: 10 | Name: Louis Medina | Major: Computer Science"
    """
    student_id, name, major = student
    return f"ID: {student_id} | Name: {name} | Major: {major}"


def display_students(student_list):
    """
    Display all student records by printing each formatted student line.
    """
    for student in student_list:
        print(format_student_data(student))
