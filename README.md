This is a Python library to run the [Specmatic](https://specmatic.in).  
Specmatic is a contract driven development tool that allows us to turn OpenAPI contracts into executable specifications.


- The specmatic python library is geared towards integrating Specmatic capabilities in PyTest tests.  
  It provides three main functions:
  - The ability to start and stop a python flask app in a test class
  - The ability to run specmatic in test mode against a local contract/spec file, or against a spec defined in a Central Contract Repository (as defined in specmatic.json).
  - The ability to stub out an api dependency using the specmatic stub feature.


- To run Specmatic in test mode against a flask app, add the **start_flask_app** and **specmatic_contract_test** decorator functions on your test class:
    ``````
    @specmatic_contract_test(host, port)
    @start_flask_app(app, host, port)
    class TestApiContract:
        @classmethod
        def teardown_class(cls):
            cls.flask_server.stop()
    ``````
    
    - The **@start_flask_app** decorator adds an attribute 'flask_server' on the test class, which can be used in the
      teardown method to stop the flask app.
    - The **@start_flask_app** accepts an instance of your flask app and the host/port to run it on.
    - The **@specmatic_contract_test** accepts host/port of your flask app and the path to the specmatic.json file in your project.
    - Specmatic will look for a specmatic.json file in your project root directory.
      If you don't wish to use specmatic.json, you can also pass the path to the actual contract/specification file to the specmatic_contract_test decorator.
    - You can run this test class either from your IDE or from command line (from your project root directory) :   
       ``````pytest test -v -s``````  
      [Click here](https://specmatic.in/documentation/contract_tests.html) to learn more about Specmatic test mode.
   
**NOTE**:
    **If you are using an IDE like PyCharm to run tests, please edit the test configuration and set the working directory to your project root directory.**

- If you want to stub out a service dependency, add the **specmatic_stub** decorator on top of the **start_flask_app**.
    ``````
    @specmatic_contract_test(host, port)
    @start_flask_app(app, host, port)
    @specmatic_stub(stub_host, stub_port, [expectation_json_file])
    class TestApiContract:
        @classmethod
        def teardown_class(cls):
        cls.flask_server.stop()
        cls.stub.stop()
    ``````
    - The **specmatic_stub** decorator adds an attribute 'stub' on the test class, which can be used in the
      teardown method to stop the stub process.
    - The **@specmatic_stub** accepts host/port on which the dependency is expected to be running.
    - It also accepts a list of expectation json file paths which can be used to return stubbed responses.  
    - The Specmatic stub will look for a specmatic.json file in your project root directory.
      If you don't wish to use specmatic.json, you can also pass the path to the actual contract/specification file to the specmatic_stub decorator.
    - Run this test class either from your IDE or from command line (from your project root directory) :   
       ``````pytest test -v -s``````  
      [Click here](https://specmatic.in/documentation/service_virtualization_tutorial.html) to learn more about Specmatic stub mode and using expectation json files.
    
   