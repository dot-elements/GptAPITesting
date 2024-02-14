import csv, io

# convert and return csv string to file
def convert_to_csv(content, csv_filename):
    # Extracting the content from the GPT response

    # Splitting the content into lines
    lines = content.split('\n')

    # Preparing to write to CSV
    with open(csv_filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Writing each line to the CSV
        for line in lines:
            # Splitting each line by comma to get individual columns
            columns = line.split('","')

            # Cleaning up quotes from the beginning and end of each line
            columns[0] = columns[0].lstrip('"')
            columns[-1] = columns[-1].rstrip('"')

            # Writing the row to the CSV file
            writer.writerow(columns)

# convert and return csv string to memory
def convert_to_csv_string(content):
    # Extracting the content from the GPT response

    # Splitting the content into lines
    lines = content.split('\n')

    # Using StringIO to create a file-like object
    output = io.StringIO()

    # Preparing to write to CSV in-memory
    writer = csv.writer(output, quoting=csv.QUOTE_MINIMAL, lineterminator='\n')

    # Writing each line to the CSV
    for line in lines:
        if line:  # Skip empty lines
            # Splitting each line by comma to get individual columns
            columns = line.split(',')

            # Stripping quotes from each field if needed
            columns = [col.strip('"') for col in columns]

            # Writing the row to the CSV in-memory
            writer.writerow(columns)

    # Get the content of the in-memory file and return it
    return output.getvalue()