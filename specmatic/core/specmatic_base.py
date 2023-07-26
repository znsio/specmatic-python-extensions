import os


class SpecmaticBase:
    def __init__(self, host: str = '127.0.0.1', port: int = 0, project_root: str = '',
                 specmatic_json_file_path: str = '', args=None, endpoints_api=""):
        self.specmatic_json_file_path = None
        self.contract_file_paths = None
        self.project_root = None
        self.project_root = project_root
        self.host = host
        self.port = port
        self.specmatic_json_file_path = specmatic_json_file_path
        self.args = [] if args is None else args
        self.endpoints_api = endpoints_api

    def validate_mandatory_fields(self):
        if self.project_root == '' and self.specmatic_json_file_path == '':
            raise Exception(
                'Please specify either of the following parameters: project_root, specmatic_json_file_path')

    def create_command_array(self, mode: str, junit_dir_path=""):
        jar_path = os.path.dirname(os.path.realpath(__file__)) + "/specmatic.jar"
        cmd = ["java"]

        if self.endpoints_api != "":
            print("Setting Endpoints API as: " + self.endpoints_api)
            cmd.append("-DendpointsAPI=" + self.endpoints_api)

        cmd.append("-jar")
        cmd.append(jar_path)
        cmd.append(mode)

        if self.specmatic_json_file_path != '':
            cmd.append("--config=" + self.specmatic_json_file_path)
        else:
            cmd.append("--config=" + self.project_root + "/specmatic.json")
        cmd += ['--host=' + self.host]
        if self.port != 0:
            cmd += ["--port=" + str(self.port)]
        if junit_dir_path != '':
            cmd += ["--junitReportDir=" + junit_dir_path]
        for arg in self.args:
            cmd += [arg]
        return cmd
