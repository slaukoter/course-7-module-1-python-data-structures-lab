# This module contains operations related to sets.

def unique_majors(student_list):
    """
    Return a set of unique student majors using set comprehension.
    Extracts the major (index 2) from each student tuple.
    """
    return {student[2] for student in student_list}

