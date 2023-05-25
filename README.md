This is a Python library to run [Specmatic](https://specmatic.in).  
Specmatic is a contract driven development tool that allows us to turn OpenAPI contracts into executable specifications.


- The specmatic python library is geared towards integrating Specmatic capabilities in PyTest tests.  
  It provides three main functions:
  - The ability to start and stop a python web app like flask/sanic.
  - The ability to run specmatic in test mode against a local contract/spec file, or against a spec defined in a Central Contract Repository (as defined in specmatic.json).
  - The ability to stub out an api dependency using the specmatic stub feature.


-  To run Specmatic against a wsgi app like flask:

``````
class TestContract:
    pass


stub = None
app_server = None

try:
    stub = Specmatic.start_stub(stub_host, stub_port, contract_file_path=stub_contract_file)
    stub.set_expectations([expectation_json_file])

    app_server = Specmatic.start_wsgi_app(app, app_host, app_port)

    Specmatic.test(TestContract, app_host, app_port, contract_file_path=service_contract_file)
except Exception as e:
    print(f"Error: {e}")
    raise e
finally:
    if app_server is not None:
        app_server.stop()
    if stub is not None:
        stub.stop()

if __name__ == '__main__':
    pytest.main()
``````  

- Specify absolute paths to the 'contract_file_path' parameter to point to the respective open api specification file.
- Run this test class either from your IDE or from command line:   
   ``````pytest test -v -s``````  
- NOTE: Please ensure that you set the '-v' and '-s' flags while running pytest as otherwise pytest may swallow up the console output.
- [Check out this repo](https://github.com/znsio/specmatic-order-bff-python/) to see more examples of how to use specmatic with a Flask app.  
- [Click here](https://specmatic.in/documentation/contract_tests.html) to learn more about Specmatic tests.  

-  To run Specmatic against an awsgi app like sanic, just replace the 'app_server' creation code above with:  
``````
app_server = Specmatic.start_asgi_app(app, app_host, app_port)
``````



  
