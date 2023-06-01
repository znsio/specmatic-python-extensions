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

#### How to use
- Create a file called test_contract.py in your test folder.  
- Declare an empty class in it called 'TestContract'.
  Specmatic will use this class to inject tests dynamically into it when you run it via say PyTest.

## WSGI Apps

#### To run contract tests with a stub for a wsgi app (like Flask):  
``````
class TestContract:
    pass
    
Specmatic.test_wsgi_app(app,
                        TestContract,
                        app_contracts=[app_contract_file],
                        stub_contracts=[stub_contract_file],
                        app_host=app_host,
                        app_port=app_port,
                        stub_host=stub_host,
                        stub_port=stub_port,
                        expectation_files=[expectation_json_file])
`````` 

- The ``````Specmatic.test_wsgi_app()`````` method accepts:
  - an instance of a wsgi app like Flask. 
  - an empty test class.
  - app_host, app_port: the host and port on which your app/service is currently running.
  - a list of open api spec file paths which define and describe your app end points.
  - stub_host, stub_port: the host and port on which your dependency service is currently running (which needs to be stubbed).  
  - a list of open api spec file paths for the stubbed service.  
  - An optional list of json files to set expectations on the stub.
-  You can run this test from either your IDE or command line by pointing pytest to your test folder:
   ``````pytest test -v -s``````  
- NOTE: Please ensure that you set the '-v' and '-s' flags while running pytest as otherwise pytest may swallow up the console output.
- [Click here](https://specmatic.in/documentation/service_virtualization_tutorial.html) to learn more about stubbing/service virtualization.  

#### To run contract tests using a central contract repository:

``````
Specmatic.test_wsgi_app(app,
                        TestContract,
                        project_root=PROJECT_ROOT,
                        stub_host=stub_host,
                        stub_port=stub_port,
                        expectation_files=[expectation_json_file])
``````                        

- When using a [central contract repository](https://specmatic.in/documentation/central_contract_repository.html), provide the absolute path to the root folder
  of your application in the 'project_root' parameter.
- You would need to have a specmatic.json file in your project root directory. [Click here](https://specmatic.in/documentation/central_contract_repository.html#specmaticjson) to learn
  more about the specmatic.json file.


#### To run contract tests without a stub, set the 'with_stub' parameter as False:

``````
Specmatic.test_wsgi_app(app,
                        TestContract,
                        with_stub=False,
                        project_root=ROOT_DIR)
``````                        

## ASGI Apps

#### To run contract tests with a stub for an asgi app (like sanic):
``````
Specmatic.test_asgi_app('main:app',
                        TestContract,
                        app_contracts=[app_contract_file],
                        stub_contracts=[stub_contract_file],
                        app_host=app_host,
                        app_port=app_port,
                        stub_host=stub_host,
                        stub_port=stub_port,
                        expectation_files=[expectation_json_file])
``````
- The ``````Specmatic.start_asgi_app()`````` method accepts:
  - a string in the 'module:app' format for your asgi app like sanic.
  - the rest of the arguments are similar to that of the ``````Specmatic.test_wsgi_app()`````` method.


## Common Issues
- **'Error loading ASGI app'** error when running Specmatic.test_asgi_app()  
   This error occurs due to incorrect module being specified in the app module parameter 'module:app' string.
 
   #### Solutions:
   - Try to identify the correct module in which your app variable is instantiated/imported.  
     For example if your 'app' variable is declared in main.py, try passing 'main:app'.  
   - Try running the app using uvicorn directly:  
     `````` uvciron 'main:app' ``````  
     If you are able to get the app started using uvicorn, it will work with specmatic too.  

## Sample Projects
- [Check out the Specmatic Order BFF Python repo](https://github.com/znsio/specmatic-order-bff-python/) to see more examples of how to use specmatic with a Flask app.  
- [Check out the Specmatic Order BFF Python Sanic repo](https://github.com/znsio/specmatic-order-bff-python-sanic/) to see more examples of how to use specmatic with a Sanic app.  
- [Check out the Specmatic Order API Python repo](https://github.com/znsio/specmatic-order-api-python/) to see an examples of how to just run tests without using a stub.  




  
