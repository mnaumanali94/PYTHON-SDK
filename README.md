Testerlib
=================
This API SDK was automatically generated by APIMATIC v2.0

This SDK uses the Requests library and will work for Python 2.7 — 3.5.

How to configure:
=================
The generated code might need to be configured with your API credentials. 
To do that, open the file "Configuration.py" and edit its contents.

How to resolve dependencies: 
===========================
The generated code uses Python packages named requests, jsonpickle and dateutil.
You can resolve these dependencies using pip ( https://pip.pypa.io/en/stable/ ).

  1. From terminal/cmd navigate to the root directory of the SDK.
  2. Invoke 'pip install -r requirements.txt'

Note: You will need internet access for this step.

How  to test:
=============
You can test the generated SDK and the server with automatically generated test
cases. unittest is used as the testing framework and nose is used as the test
runner. You can run the tests as follows:

  1. From terminal/cmd navigate to the root directory of the SDK.
  2. Invoke 'nosetests'

How to use:
===========
After having resolved the dependencies, you can easily use the SDK following these steps.

  1. Create a "testerlib_test.py" file in the root directory.
  2. Use any controller as follows:
```python
from __future__ import print_function
from testerlib.tester_client import *

api_client = TesterClient()
controller = api_client.response_types_controller
response = controller.get_long(<required parameters if any>)

print(response)
```