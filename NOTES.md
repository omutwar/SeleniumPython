#### How to configure pytest.ini for test discovery

##### When configuring test discovery in pytest, you can customize it in various ways

1) If you want to exclude specific directories or modules during test collection, you can use the --ignore=path option on the command line. You can even specify multiple --ignore options.
For example, if you have a directory structure like this:
tests/
├── example/
│   ├── test_example_01.py
│   ├── test_example_02.py
│   └── test_example_03.py
├── foobar/
│   ├── test_foobar_01.py
│   ├── test_foobar_02.py
│   └── test_foobar_03.py
└── hello/
    └── world/
        ├── test_world_01.py
        ├── test_world_02.py
        └── test_world_03.py
2) You can run pytest with:
pytest --ignore=tests/foobar/test_foobar_03.py --ignore=tests/hello/ 
- This will collect only the specified test modules, excluding those that match the patterns specified.

3) Changing Naming Conventions:
You can configure different naming conventions by setting the following options in your configuration file (e.g., pytest.ini):
[pytest]
python_files = check_*.py
python_classes = Check
python_functions = *_check

This example tells pytest to look for files starting with “check” instead of “test” and to recognize classes and functions with specific prefixes.


#####  When configuring naming conventions for test discovery in pytest, you can indeed specify multiple patterns for test file names
- In your pytest.ini (or any other configuration file), you can set the following options to customize the naming conventions for test files:
[pytest]
python_files = check_*.py *_test.py


In this example, we’ve specified two patterns:
check_*.py: This will match files starting with “check_” (e.g., check_utils.py, check_api.py).
*_test.py: This will match files ending with “_test” (e.g., my_module_test.py, test_functions_test.py).


Multiple Patterns:

By separating the patterns with spaces, you can include both check_*.py and *_test.py files in your test collection.
pytest will look for files that match either of these patterns during test discovery.

Example Usage:

Suppose you have the following test files:
my_module_check.py
my_module_test.py
utils_check.py
utils_test.py

With the configuration above, pytest will collect tests from both my_module_check.py and my_module_test.py.
