import data_extraction

id_key = "1URq2Pb8-fj3vQJKfiDF1KPD3uYH6tw6TbhHwk9v7TMM"

formatted_data = data_extraction.data_extraction(id_key)

# Print the formatted data
print("Formatted data:")
for row in formatted_data:
    print(row)
