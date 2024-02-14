from flask import Flask, request, jsonify, Response
import json
import csv
import io
import gptLogicRunner

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file and file.filename.endswith('.json'):
        content = json.load(file)
        # Process the JSON content here
        csv_data = gptLogicRunner.run_logic(content)
        # Convert csv_data string to a list of lists
        lines = csv_data.split('\n')
        rows = [line.split(',') for line in lines if line]  # Split each line into columns

        # Create a CSV response
        si = io.StringIO()
        cw = csv.writer(si, quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        cw.writerows(rows)

        output = si.getvalue()
        return Response(output, mimetype='text/csv', headers={"Content-disposition": "attachment; filename=test_data.csv"})
    else:
        return jsonify({"error": "Invalid file format"}), 400

if __name__ == '__main__':
    # define the GPT logic runner here
    gptLogicRunner = gptLogicRunner.GPTLogicRunner()
    app.run(debug=True)
