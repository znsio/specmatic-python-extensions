from specmatic_python.specmatic.specmatic import Specmatic


def create_stub(host, port, specmatic_json_file='', expectation_json_file=''):
    def decorator(cls):
        stub = Specmatic() \
            .stub(host, port) \
            .with_specmatic_json_at(specmatic_json_file) \
            .build()
        stub.start()
        stub.set_expectation(expectation_json_file)
        cls.stub = stub
        return cls

    return decorator


def run_specmatic(host, port, specmatic_json_file=''):
    def decorator(cls):
        Specmatic() \
            .test(host, port) \
            .with_specmatic_json_at(specmatic_json_file) \
            .configure_py_tests(cls)
        return cls

    return decorator