from openai import OpenAI
import os
import swaggerParser
import csvConverter

prompt_file_path = "prompt.txt"

class GPTLogicRunner:
    def __init__(self, base_prompt_file_path="prompt.txt"):
        self.api_key = os.getenv("OPENAI_API_KEY")
        #Add your gpt api key below
        self.api_key = "<your key here>"
        self.client = OpenAI(api_key=self.api_key)
        self.base_prompt_file_path = base_prompt_file_path
        self.model = "gpt-4"
        self.max_tokens = 200

    def query_gpt(self, json_data):
        # Read the prompt content from the file
        with open(self.base_prompt_file_path, 'r') as file:
            base_prompt_content = file.read().strip()

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "system", "content": base_prompt_content},
                      {"role": "user", "content": json_data}]
        )
        return response.choices[0].message.content

    def run_logic_to_file(self, json_data):
        parsed_request_data = swaggerParser.parse_swagger(json_data)
        print(parsed_request_data)
        request_prompt = "Here is the json data: " + str(parsed_request_data)
        response = self.query_gpt(request_prompt)
        print("GPT says:", response)
        csvConverter.convert_to_csv(response, 'client/output.csv')

    def run_logic(self, json_data):
        parsed_request_data = swaggerParser.parse_swagger(json_data)
        print(parsed_request_data)
        request_prompt = "Here is the json data: " + str(parsed_request_data)
        response = self.query_gpt(request_prompt)
        print("GPT says:", response)
        csv_data = csvConverter.convert_to_csv_string(response)
        print(csv_data)
        return csv_data



