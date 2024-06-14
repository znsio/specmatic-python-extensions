class ContractTest:
    def __init__(self, name: str, passed: bool, error_message: str = ""):
        self.name = name
        self.passed = passed
        self.error_message = error_message
