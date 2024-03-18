# Selenium Python Project

...
This is new python project to keep my competence in check.
...

#### How to rename a local branch to new branch

> To rename a branch both locally and remotely in Git, you can use the following commands:

#### Rename the local branch

> git branch -m old_branch new_branch

#### Delete the old remote branch

> git push origin :old_branch

#### Push the new branch to remote

> git push origin new_branch

#### Reset the upstream branch for the new local branch

> git push origin -u new_branch

`In this example, old_branch is the name of the branch you want to rename and new_branch is the new name you want to give to the branch`

Notes: updates will be stored here
----------------------------------
Tags: Selenium, Python

Explicit Wait
-------------
> Usage:
> wait = WebDriverWait(driver, 10)
> wait.until(EC.element_to_be_clickable(By.XPATH, <locator>))

#### NOTE: How To Install Venv

-- In Windows, we can install it by going to the python installation directory, then type <python.exe -m venv <
path-to-install-the-package>

-- In Windows, the <activate> file is located inside the <Scripts> directory, while in Mac/Linux, it may be inside
the <bin> directory


#### How To Govern Test Search In Pytest
-------------------------------------

    - Create a file name <pytest.ini> or hidden version <.pytest.ini>
    - 
        > [pytest] # This should be the first line
        > python_files = test_*
        > python_classes = Tests*
        > python_functions = test_*
        -   add more as needed 

    - 

##### How to initialize webdriver instance
-----------------------------------
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver-manager import GeckoDriverManager

driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))
driver.maximize_window()

driver.get('url.to.test.website')

#####   

pytest.ini
A concise and comprehensive pytest.ini file for Selenium tests might include settings for configuring test runs,
plugins, and output formats. Here's an example:

[pytest]

# Test discovery

python_files = test_*.py
python_classes = Test*
python_functions = test_*

# Output settings

addopts = -ra -v --html=reports/report.html --self-contained-html
norecursedirs = .git .tox venv

# Plugins

filterwarnings =
ignore::DeprecationWarning
ignore::UserWarning

# HTML report customization

render_collapsed = True
render_module = true
render_class = true
render_instance = true
In this pytest.ini file:

python_files, python_classes, and python_functions define patterns to discover test files, classes, and functions,
respectively.
addopts specifies additional command-line options for pytest, including generating an HTML report (
--html=reports/report.html) with verbose output (-v) and showing all test results (-ra). The --self-contained-html
option ensures that the report is self-contained.
norecursedirs excludes specific directories from test discovery.
filterwarnings suppresses certain types of warnings during test execution.
HTML report customization options (render_collapsed, render_module, render_class, render_instance) control the level of
detail in the HTML report.
Adjust these settings according to your project's needs.

###### Three ways of executing the tests in pytest

    - py.test -v -s file_path # runs all the tests in that file path
    - py.test -v -s test_mod.py py. # run tests in module or in test file
    - py.test -v -s test_module.py::test_method # only runs the test_method in test_module.py

    -v : verbose (verbose in an argument which is used to report more information about an operation in your program)
    -s : to print statements

