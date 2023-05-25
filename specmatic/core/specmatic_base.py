class SpecmaticBase:
    def __init__(self):
        self.specmatic_json_file_path = None
        self.contract_file_path = None
        self.project_root = None

    def validate_mandatory_fields(self):
        if self.project_root == '' and self.contract_file_path == '' and self.specmatic_json_file_path == '':
            raise Exception(
                'Please specify either of the following parameters: project_root, contract_file_path, specmatic_json_file_path')
