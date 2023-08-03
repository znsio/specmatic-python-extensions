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
  This is could either be a normal class like:
  ``````
  class TestContract:
    pass
  ``````
  Or you could also have a class which inherits from unittest.TestCase:
  ``````
  class TestContract(unittest.TestCase):
    pass
  ``````
  Specmatic will use this class to inject tests dynamically into it when you run it via PyTest or UnitTest.

## WSGI Apps

#### To run contract tests with a stub for a wsgi app (like Flask):  

``````
class TestContract:
    pass
    
    
Specmatic() \
    .with_project_root(PROJECT_ROOT) \
    .with_stub(stub_host, stub_port, [expectation_json_file]) \
    .with_wsgi_app(app, app_host, app_port) \
    .test(TestContract) \
    .run()
`````` 

- In this, we are passing:
  - an instance of your asgi app like flask 
  - app_host and app_port. If they are not specified, the app will be started on a random available port on 127.0.0.1.
  - You would need a [specmatic.json](https://specmatic.in/documentation/specmatic_json.html) file to be present in the root directory of your project.
  - an empty test class.
  - stub_host, stub_port, optional list of json files to set expectations on the stub.  
    The stub_host, stub_port will be used to run the specmatic stub server.   
    If they are not supplied, the stub will be started on a random available port on 127.0.0.1.    
    [Click here](https://specmatic.in/documentation/service_virtualization_tutorial.html) to learn more about stubbing/service virtualization.
-  You can run this test from either your IDE or command line by pointing pytest to your test folder:
   ``````pytest test -v -s``````  
- NOTE: Please ensure that you set the '-v' and '-s' flags while running pytest as otherwise pytest may swallow up the console output.
  

#### To run contract tests without a stub:

``````
class TestContract:
    pass
    
Specmatic() \
    .with_project_root(PROJECT_ROOT) \
    .with_wsgi_app(app, app_host, app_port) \
    .test(TestContract) \
    .run()
``````                        

## ASGI Apps

#### To run contract tests with a stub for an asgi app (like sanic):
- If you are using an asgi app like sanic, fastapi, use the ``````with_asgi_app`````` function and pass it a string in the 'module:app' format.
``````
class TestContract:
    pass
    
    
Specmatic() \
    .with_project_root(PROJECT_ROOT) \
    .with_stub(stub_host, stub_port, [expectation_json_file]) \
    .with_asgi_app('main:app', app_host, app_port) \
    .test(TestContract) \
    .run()
``````

### Passing extra arguments to stub/test
- To pass arguments like '--strict', '--testBaseUrl', pass them as a list to the 'args' parameter:
``````
class TestContract:
    pass


Specmatic() \
    .with_project_root(PROJECT_ROOT) \
    .with_stub(stub_host, stub_port, [expectation_json_file], ['--strict']) \
    .with_wsgi_app(app, port=app_port) \
    .test(TestContract, args=['--testBaseURL=http://localhost:5000']) \
    .run()
``````

## Coverage
Specmatic can generate a coverage summary report which will list out all the apis exposed by your app/service with a status next to it indicating if it has been covered in your contract tests.

### Enabling api coverage for Flask apps

``````
class TestContract:
    pass


Specmatic() \
    .with_project_root(PROJECT_ROOT) \
    .with_stub(stub_host, stub_port, [expectation_json_file]) \
    .with_wsgi_app(app, app_host, app_port) \
    .test_with_flask_app_api_coverage(TestContract) \
    .run()
``````

### Enabling api coverage for Sanic apps

``````
class TestContract:
    pass


Specmatic() \
    .with_project_root(PROJECT_ROOT) \
    .with_stub(stub_host, stub_port, [expectation_json_file]) \
    .with_asgi_app('test.apps.sanic:app', app_host, app_port) \
    .test_with_sanic_app_api_coverage(TestContract, app) \
    .run()
``````

### Enabling api coverage for FastApi apps

``````
class TestContract:
    pass


Specmatic() \
    .with_project_root(PROJECT_ROOT) \
    .with_stub(stub_host, stub_port, [expectation_json_file]) \
    .with_asgi_app('test.apps.fast_api:app', app_host, app_port) \
    .test_with_fastapi_app_api_coverage(TestContract, app) \
    .run()
``````

### Enabling api coverage for any other type of app
For any app other than Flask, Sanic, and FastApi, you would need to implement an ``````AppRouteAdapter`````` class.  
The idea is to implement ``````to_coverage_routes`````` method, which returns a list of ``````CoverageRoute`````` objects corresponding to all the routes defined in your app.  
The ``````CoverageRoute`````` class has two properties:  
``````url`````` : This represents your route url in this format: `````` /orders/{order_id}``````  
``````method`````` : A list of HTTP methods supported on the route, for instance : ``````['GET', 'POST']``````  

You can then enable coverage by passing your adapter like this:  

``````
Specmatic() \
    .with_project_root(PROJECT_ROOT) \
    .with_stub(stub_host, stub_port, [expectation_json_file]) \
    .with_asgi_app('main:app', app_host, app_port) \
    .test_with_api_coverage(TestContract, MyAppRouteAdapter(app)) \
    .run()
``````

### Enabling api coverage by setting the EndPointsApi property
You can also start your coverage server externally and use the EndPointsApi method to enable coverage.  
We have provided ready to use Coverage Server classes for:  
Flask: ``````FlaskAppCoverageServer``````  
Sanic: ``````SanicAppCoverageServer``````  
FastApi ``````FastApiAppCoverageServer``````  

You can also easily implement your own coverage server if you have written a custom implementation of the ``````AppRouteAdapter`````` class.
The only point to remember in mind is that the EndPointsApi url should return a list of routes in the format used buy Spring Actuator's ```````/actuator/mappings``````` endpoint
as described [here](https://docs.spring.io/spring-boot/docs/current/actuator-api/htmlsingle/#mappings).  

Here's an example where we start both our FastApi app and coverage server outside the specmatic api call.  
``````
app_server = ASGIAppServer('test.apps.fast_api:app', app_host, app_port)
coverage_server = FastApiAppCoverageServer(app)

app_server.start()
coverage_server.start()


class TestContract:
    pass


Specmatic() \
    .with_project_root(PROJECT_ROOT) \
    .with_stub(stub_host, stub_port, [expectation_json_file]) \
    .with_endpoints_api(coverage_server.endpoints_api) \
    .test(TestContract, app_host, app_port) \
    .run()

app_server.stop()
coverage_server.stop()
``````

## Common Issues
- **'Error loading ASGI app'** 
   This error occurs when an incorrect app module string is passed to the ``````with_asgi_app`````` function.  
 
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




  
