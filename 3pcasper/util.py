def parse_json_file(file_path):
    with open(file_path) as file:
        json_dict = json.loads(file.read())
        return json_dict
