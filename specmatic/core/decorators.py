from flask import Flask
from specmatic.server.flask_server import FlaskServer
from specmatic.core.specmatic import Specmatic


def specmatic_stub(host: str, port: int, expectation_json_files=None, contract_file='', specmatic_json_file: str = ''):
    if expectation_json_files is None:
        expectation_json_files = []

    def decorator(cls):
        try:
            stub = Specmatic() \
                .stub(host, port) \
                .with_specmatic_json_at(specmatic_json_file) \
                .with_contract_file(contract_file) \
                .build()
            stub.start()
            cls.stub = stub
            stub.set_expectations(expectation_json_files)
        except Exception as e:
            if hasattr(cls, 'stub'):
                cls.stub.stop()
            print(f"Error: {e}")
            raise e
        return cls

    return decorator


def specmatic_contract_test(host: str, port: int, contract_file='', specmatic_json_file: str = ''):
    def decorator(cls):
        try:
            Specmatic() \
                .test(host, port) \
                .with_specmatic_json_at(specmatic_json_file) \
                .with_contract_file(contract_file) \
                .configure_py_tests(cls)
            return cls
        except Exception as e:
            if hasattr(cls, 'stub'):
                cls.stub.stop()
            print(f"Error: {e}")
            raise e

    return decorator


def start_flask_app(app: Flask, host: str, port: int):
    def decorator(cls):
        try:
            flask_server = FlaskServer(app, host, port)
            flask_server.start()
            cls.flask_server = flask_server
            return cls
        except Exception as e:
            if hasattr(cls, 'stub'):
                cls.stub.stop()
            print(f"Error: {e}")
            raise e

    return decorator
