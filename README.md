### This project aims to test APIs through a Swagger trace automatically.
---
To achieve this, we have the flow:
- Parse swagger file for all validation rules, done by the `swaggerParser.py`
- Make a GPT call to instantiate the rules into generated data, done by the `gptLogicRunner.py`
- Prompting: the prompt used to generate the data can be changed in `prompt.txt`
- Format into CSV to feed into Postman tests, done by the `csvConverter.py`

---
### The flow of how to set up Postman for this task is not here! This is a short explanation of how it works:

Once the test data is generated, it can be fed into Postman to test a specific endpoint.
You feed the form fields with the generated data through Postman and generate a test for each one individually.

---
To generate data yourself:
- Fill in your api key in `gptLogicRunner.py`
- Start the application `./app.py`
- In the `client/requestTester`, change the `file_path` to the swagger endpoint trace
- Run `./client/requestTester`
