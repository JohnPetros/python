# task 106 - Write a script that contains a function that will receive multiple grades of students and return a dictionary containing the following information:
# - The total of grades
# - The largest of grades
# - The smallest of grades
# - The average grade
# - The status (optional)
# Also add the docstrings

from math import trunc


def get_dictionary(*grades, should_show_status=False):
    """
    -> return a dictionary containing a report about the students' grades

    :param *grades: students' grades
    :should_show_status: indicates whether the students' status should be shown
    """

    dictionary = dict()

    dictionary["largest_number"] = grades[0]
    dictionary["smallest_number"] = grades[0]

    for number in grades:
        if number > dictionary["largest_number"]:
            dictionary["largest_number"] = number
        elif number < dictionary["smallest_number"]:
            dictionary["smallest_number"] = number

    dictionary["total"] = len(grades)
    dictionary["average"] = trunc(sum(grades) / dictionary["total"])

    if should_show_status:
        if dictionary["average"] < 5:
            dictionary["status"] = "BAD"
        elif dictionary["average"] < 7:
            dictionary["status"] = "REGULAR"
        else:
            dictionary["status"] = "GOOD"

    return dictionary


dictionary = get_dictionary(5.5, 2.5, 1.5, should_show_status=True)
print(dictionary)

help()
