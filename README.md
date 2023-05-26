# Specmatic Python
This is a Python library to run [Specmatic](https://specmatic.in).  
Specmatic is a contract driven development tool that allows us to turn OpenAPI contracts into executable specifications.
<br/>Click below to learn more about Specmatic and Contract Driven Development<br/><br/>
[![Specmatic - Contract Driven Development](https://img.youtube.com/vi/3HPgpvd8MGg/0.jpg)](https://www.youtube.com/watch?v=3HPgpvd8MGg "Specmatic - Contract Driven Development")

  The specmatic python library provides three main functions:
  - The ability to start and stop a python web app like flask/sanic.
  - The ability to run specmatic in test mode against an open api contract/spec.
  - The ability to stub out an api dependency using the specmatic stub feature.

#### Running Contract Tests
A contract test validates an open api specification against a running api service.  
The open api specification can be present either locally or in a [Central Contract Repository](https://specmatic.in/documentation/central_contract_repository.html)  
[Click here](https://specmatic.in/documentation/contract_tests.html) to learn more about contract tests.  

To run contract tests:  
``````
class TestContract:
    pass
    
Specmatic.test(TestContract, app_host, app_port, contract_file_path=service_contract_file)
``````
- Create a file called test_contract.py in your test folder.  
- Declare an empty class in it called 'TestContract'.  
  Specmatic will use this class to inject tests dynamically into it when you run it via say PyTest.
- The ``````Specmatic.test()`````` method accepts:
  - an empty test class 
  - the host and port on which your app/service is currently running
  - path to an open api spec file which defines and describes the service end points
-  You can run this test from either your IDE or command line by pointing pytest to your test folder :
   ``````pytest test -v -s``````  
- NOTE: Please ensure that you set the '-v' and '-s' flags while running pytest as otherwise pytest may swallow up the console output.


#### Setting up Stubs
In many cases, your app/service might require calling another api to perform its operations.  
Specmatic provides you with an option of creating a stub for such service dependencies and setup expectations on it (like you would do in any of the mocking frameworks).  

To create a stub:
``````
stub = Specmatic.start_stub(stub_host, stub_port, contract_file_path=stub_contract_file)
stub.set_expectations([expectation_json_file])
# run tests ...
stub.stop()
``````    

- The ``````Specmatic.start_stub()`````` method accepts:
  - the host and port on which your app/service is currently running (which needs to be stubbed).  
  - path to an open api spec file for the stubbed service.  
  - An optional list of json files to set expectations on the stub.  
- [Click here](https://specmatic.in/documentation/service_virtualization_tutorial.html) to learn more about stubbing/service virtualization.  

#### Starting/Stopping a python web app
If you wish to start/stop your python app as part of your tests, here's how you can do it:  
- WSGI Apps:  
  ``````app_server = Specmatic.start_wsgi_app(app, app_host, app_port)``````  

- The ``````Specmatic.start_wsgi_app()`````` method accepts:
  - an instance of a wsgi app like flask.  
  - the host/port to run on  

- ASGI Apps:  
  ``````app_server = Specmatic.start_asgi_app('app:app', app_host, app_port)``````  

- The ``````Specmatic.start_asgi_app()`````` method accepts:
  - a string in the 'module:app' format for your asgi app like sanic.
  - the host/port to run on.  
<br/>

### Putting it all together
This is how it looks when use all these in a single test:

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


- [Check out the Specmatic Order BFF Python repo](https://github.com/znsio/specmatic-order-bff-python/) to see more examples of how to use specmatic with a Flask app.  
- [Check out the Specmatic Order BFF Python Sanic repo](https://github.com/znsio/specmatic-order-bff-python-sanic/) to see more examples of how to use specmatic with a Sanic app.  




  
