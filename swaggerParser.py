import json

# Parser function to extract request paths and the request body parameters with their validation rules
def parse_swagger(swagger_data):
    paths = {}
    for path, methods in swagger_data.get("paths", {}).items():
        paths[path] = {}
        for method, details in methods.items():
            paths[path][method] = {
                "parameters": [],
                "responses": {}
            }
            # Get requestBody details if present
            request_body = details.get("requestBody")
            if request_body:
                content = request_body.get("content", {}).get("application/json", {})
                schema = content.get("schema", {})
                required_params = schema.get("required", [])
                properties = schema.get("properties", {})
                for param_name, param_details in properties.items():
                    param_info = {
                        "name": param_name,
                        "description": param_details.get("description"),
                        "type": param_details.get("type"),
                        "required": param_name in required_params
                    }
                    # Add validation rules based on the type of parameter
                    if param_info['type'] == 'string':
                        if "maxLength" in param_details:
                            param_info["maxLength"] = param_details["maxLength"]
                        if "minLength" in param_details:
                            param_info["minLength"] = param_details["minLength"]
                        if "format" in param_details:
                            param_info["format"] = param_details["format"]
                    paths[path][method]["parameters"].append(param_info)
            # Get responses
            responses = details.get("responses", {})
            for status_code, response_details in responses.items():
                paths[path][method]["responses"][status_code] = response_details.get("description")
    return paths
