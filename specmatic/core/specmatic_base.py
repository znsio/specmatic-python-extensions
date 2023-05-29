import os


class SpecmaticBase:
    def __init__(self, host: str = '127.0.0.1', port: int = 0, project_root: str = '', contract_file_paths=None,
                 specmatic_json_file_path: str = ''):
        self.specmatic_json_file_path = None
        self.contract_file_paths = None
        self.project_root = None
        self.project_root = project_root
        self.host = host
        self.port = port
        self.specmatic_json_file_path = specmatic_json_file_path
        self.contract_file_paths = contract_file_paths if contract_file_paths else []

    def validate_mandatory_fields(self):
        if self.project_root == '' and len(self.contract_file_paths) == 0 and self.specmatic_json_file_path == '':
            raise Exception(
                'Please specify either of the following parameters: project_root, contract_file_paths, specmatic_json_file_path')

    def create_command_array(self, mode: str, junitDirPath=''):
        jar_path = os.path.dirname(os.path.realpath(__file__)) + "/specmatic.jar"
        cmd = [
            "java",
            "-jar",
            jar_path,
            mode
        ]
        if self.specmatic_json_file_path != '':
            cmd.append("--config=" + self.specmatic_json_file_path)
        else:
            if len(self.contract_file_paths) > 0:
                for contract_file_path in self.contract_file_paths:
                    cmd.append(contract_file_path)
            else:
                cmd.append("--config=" + self.project_root + "/specmatic.json")
        cmd += ['--host=' + self.host]
        if self.port != 0:
            cmd += ["--port=" + str(self.port)]
        if junitDirPath != '':
            cmd += ["--junitReportDir=" + junitDirPath]
        return cmd
