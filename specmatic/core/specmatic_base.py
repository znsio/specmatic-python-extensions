import os
import pathlib


class SpecmaticBase:
    def __init__(self, host: str = '127.0.0.1', port: int = 0, project_root: str = '',
                 specmatic_config_file_path: str = '', args=None, endpoints_api=""):
        self.specmatic_config_file_path = None
        self.contract_file_paths = None
        self.project_root = None
        self.project_root = project_root
        self.host = host
        self.port = port
        self.specmatic_config_file_path = specmatic_config_file_path
        self.args = [] if args is None else args
        self.endpoints_api = endpoints_api

    def validate_mandatory_fields(self):
        if not self.project_root and not self.specmatic_config_file_path:
            raise Exception('Please specify either of the following parameters: project_root, specmatic_config_file_path')

        if not self.specmatic_config_file_path and self.project_root:
            config_file_paths = [
                f"{self.project_root}/specmatic.json",
                f"{self.project_root}/specmatic.yaml",
                f"{self.project_root}/specmatic.yml"
            ]
            for config_file in config_file_paths:
                if pathlib.Path(config_file).exists():
                    self.specmatic_config_file_path = config_file
                    break

        if not self.specmatic_config_file_path:
            raise Exception("Specmatic config file not found, please check project_root and specmatic_config_file_path parameters")

    def create_command_array(self, mode: str, junit_dir_path=""):
        self.validate_mandatory_fields()
        jar_path = os.path.dirname(os.path.realpath(__file__)) + "/specmatic.jar"
        cmd = ["java"]

        if self.endpoints_api != "":
            print("Setting Endpoints API as: " + self.endpoints_api)
            cmd.append(f"-DendpointsAPI={self.endpoints_api}")

        cmd.append("-jar")
        cmd.append(jar_path)
        cmd.append(mode)
        cmd.append(f"--config={self.specmatic_config_file_path}")
        
        cmd += ['--host=' + self.host]
        if self.port != 0:
            cmd += ["--port=" + str(self.port)]
        if junit_dir_path:
            cmd += ["--junitReportDir=" + junit_dir_path]
        for arg in self.args:
            cmd += [arg]
        return cmd
