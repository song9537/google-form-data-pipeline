import re


# Define a function to format the data
def extract_numbers(rows):
    result = []

    for row in rows[1:]:  # Skip the header row (first row)
        timestamp = row[0].split(" ")[0]  # Extract just the date (removing the time)
        names_column = row[1]

        # Use regex to find all names (ignoring numbers in parentheses)
        names = re.findall(r"[\uAC00-\uD7A3]+", names_column)

        # Prepend the timestamp to the list of names
        formatted_row = [timestamp] + names
        result.append(formatted_row)

    return result


def separate_data(rows, form_id):
    # Process data into a list of tuples
    result = []
    for row in rows:
        date = row[0]  # The date is the first element
        students = row[1:]  # The rest are student names
        for student in students:
            result.append((date, student, form_id))

    return result


def feature_engineer(rows, form_id):
    first_iteration = extract_numbers(rows)
    second_iteration = separate_data(first_iteration, form_id)

    result = second_iteration

    return result
