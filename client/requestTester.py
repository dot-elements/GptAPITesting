import requests

url = 'http://localhost:5000/upload'

# Replace this with the path to the JSON file you need to test
file_path = 'swagger_docs.json'

# This is the path to the CSV file where you want to save the response
output_csv_file_path = 'output.csv'

with open(file_path, 'rb') as f:
    files = {'file': (file_path, f, 'application/json')}
    response = requests.post(url, files=files)

    # Check if the response is successful
    if response.status_code == 200:
        # Write the response content to a CSV file
        with open(output_csv_file_path, 'w', encoding='utf-8') as csv_file:
            csv_file.write(response.text)
        print(f"CSV data saved to {output_csv_file_path}")
    else:
        print(f"Error: Received status code {response.status_code}")