This is a Python library to run [Specmatic](https://specmatic.in).  
Specmatic is a contract driven development tool that allows us to turn OpenAPI contracts into executable specifications.


- The specmatic python library is geared towards integrating Specmatic capabilities in PyTest tests.  
  It provides three main functions:
  - The ability to start and stop a python web app like flask.
  - The ability to run specmatic in test mode against a local contract/spec file, or against a spec defined in a Central Contract Repository (as defined in specmatic.json).
  - The ability to stub out an api dependency using the specmatic stub feature.


- To run Specmatic in test mode against a flask app, add the **start_app** and **specmatic_contract_test** decorator functions on your test class:
    ``````
    @specmatic_contract_test(PROJECT_ROOT, app_host, app_port)
    @start_app(app, app_host, app_port)
    class TestApiContract:
        pass
    ``````

    - The **@start_app** decorator accepts an instance of your flask app and the host/port to run it on.
    - The **@specmatic_contract_test** decorator accepts your project root directory and the host/port of your flask app.
    - Specmatic will look for a specmatic.json file in your project root directory.
      If you don't wish to use specmatic.json, you can also pass the path to the actual contract/specification file to the specmatic_contract_test decorator.
    - You can run this test class either from your IDE or from command line (from your project root directory) :   
       ``````pytest test -v -s``````  
      [Click here](https://specmatic.in/documentation/contract_tests.html) to learn more about Specmatic test mode.


- If you want to stub out a service dependency, add the **specmatic_stub** decorator below the **start_app** decorator.
    ``````
    @specmatic_contract_test(PROJECT_ROOT, host, port)
    @start_app(app, host, port)
    @specmatic_stub(PROJECT_ROOT, stub_host, stub_port, [expectation_json_file])
    class TestApiContract:
       pass
    ``````
  
    - The **@specmatic_stub** decorator accepts your project root directory and the host/port on which the dependency is expected to be running.
    - It also optionally accepts a list of expectation json file paths which can be used to return stubbed responses.  
    - The Specmatic stub will look for a specmatic.json file in your project root directory.
      If you don't wish to use specmatic.json, you can also pass the path to the actual contract/specification file to the specmatic_stub decorator.
    - Run this test class either from your IDE or from command line (from your project root directory) :   
       ``````pytest test -v -s``````  
      [Click here](https://specmatic.in/documentation/service_virtualization_tutorial.html) to learn more about Specmatic stub mode and using expectation json files.

- If you do not want to use the specmatic decorators and directly use the specmatic api, here's how you can do it:
  ``````
  class TestContract:
    pass


  stub = Specmatic.create_stub(PROJECT_ROOT, stub_host, stub_port)
  stub.start()
  stub.set_expectations([expectation_json_file])

  app = WSGIServer(app, app_host, app_port)
  app.start()
  Specmatic.run_tests(PROJECT_ROOT, TestContract, app_host, app_port)

  app.stop()
  stub.stop()
  
  if __name__ == '__main__':
    pytest.main()
  ``````
  
  The above code can be broken down into three parts
  - **Stub setup:**  
     Use the ``````Specmatic.create_stub()`````` method to create a stub instance.  
     You can set expectations on the stub by calling the ``````set_expectations()`````` method and passing a list of expectation json files.
  - **App Setup:**  
    Create an instance of the ``````WSGIServer`````` class by passing it an instance of a WSGIApplication like a flask app and the host and port to run on.
  - **Run Tests**
    Call ``````Specmatic.run_tests()`````` by passing it your root directory, an empty Test class and the host/port on which your app is running.
          
        
        

    
   