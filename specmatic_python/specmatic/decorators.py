from flask import Flask

from specmatic_python.server.flask_server import FlaskServer
from specmatic_python.specmatic.specmatic import Specmatic


def specmatic_stub(host: str, port: int, expectation_json_files=None, specmatic_json_file: str = '', contract_file=''):
    if expectation_json_files is None:
        expectation_json_files = []

    def decorator(cls):
        stub = Specmatic() \
            .stub(host, port) \
            .with_specmatic_json_at(specmatic_json_file) \
            .with_contract_file(contract_file) \
            .build()
        stub.start()
        stub.set_expectations(expectation_json_files)
        cls.stub = stub
        return cls

    return decorator


def specmatic_contract_test(host: str, port: int, specmatic_json_file: str = '', contract_file=''):
    def decorator(cls):
        Specmatic() \
            .test(host, port) \
            .with_specmatic_json_at(specmatic_json_file) \
            .with_contract_file(contract_file) \
            .configure_py_tests(cls)
        return cls

    return decorator


def start_flask_app(app: Flask, host: str, port: int):
    def decorator(cls):
        flask_server = FlaskServer(app, host, port)
        flask_server.start()
        cls.flask_server = flask_server
        return cls

    return decorator
