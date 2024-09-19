import data_extraction
import feature_engineer
import database

form_id = "1URq2Pb8-fj3vQJKfiDF1KPD3uYH6tw6TbhHwk9v7TMM"

extracted_data = data_extraction.data_extraction(form_id)

# Format the fetched data
formatted_data = feature_engineer.feature_engineer(extracted_data, form_id)

# Print the formatted data
print("Formatted data:")
for row in formatted_data:
    print(row)


# Main program to run the fucntions
if __name__ == "__main__":
    # Connect to the PostgreSQL database
    connection = database.connect_to_db()

    if connection:
        # Create the 'inspections' table
        database.create_table(connection)

        # Insert example data into the table
        for date, student_name, form_id in formatted_data:
            database.insert_data(connection, date, student_name, form_id)

        # Query and print the data from the table
        database.query_data(connection)

        # Close the connection
        connection.close()
