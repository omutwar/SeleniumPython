### Selenium Python Project

...
This is new python project to keep my competence in check.
...

#### How to rename a local branch to new branch
> To rename a branch both locally and remotely in Git, you can use the following commands:

##### Rename the local branch
> git branch -m old_branch new_branch

##### Delete the old remote branch
> git push origin :old_branch

##### Push the new branch to remote
> git push origin new_branch

##### Reset the upstream branch for the new local branch
> git push origin -u new_branch

`In this example, old_branch is the name of the branch you want to rename and new_branch is the new name you want to give to the branch`

Notes: updates will be stored here
----------------------------------
Tags: Selenium, Python

Explicit Wait
-------------
> Usage:
>   wait = WebDriverWait(driver, 10)
>   wait.until(EC.element_to_be_clickable(By.XPATH, <locator>))

#### NOTE: How To Install Venv
-- In Windows, we can install it by going to the python installation directory, then type <python.exe -m venv <path-to-install-the-package>

-- In Windows, the <activate> file is located inside the <Scripts> directory, while in Mac/Linux, it may be inside the <bin> directory


# How To Govern Test Search In Pytest
-------------------------------------
    - Create a file name <pytest.ini> or hidden version <.pytest.ini>
    - 
        > [pytest] # This should be the first line
        > python_files = test_*
        > python_classes = Tests*
        > python_functions = test_*
        -   add more as needed 

    - 
--------------------------------------
Creating a project-specific environment in Python is a good practice to isolate the dependencies of your project from other projects and the system-wide Python installation. This can be achieved using virtual environments. Here are the steps to create a virtual environment:

1. Navigate to your project's directory.

2. Create a virtual environment using the `venv` module that comes with Python 3.3 and later versions². If you're using Python 2, replace `venv` with `virtualenv`. The command is as follows:
```python
python -m venv myenv
```
Here, `myenv` is the name of your virtual environment. You can replace it with any name you prefer.

3. Activate the virtual environment. The command to activate the environment depends on your operating system:
   - On Windows:
   ```cmd
   myenv\Scripts\activate
   ```
   - On Unix or MacOS:
   ```bash
   source myenv/bin/activate
   ```

4. Now, your terminal prompt should change to show the name of the activated environment.

5. You can then install any required packages using pip, which will install packages in the virtual environment only⁶.

6. When you're done working in the virtual environment for the moment, you can deactivate it by running:
```bash
deactivate
```
This command needs to be run in the same shell where the environment was activated⁶.

Remember, each time you start a new terminal session, you need to reactivate your virtual environment. Also, different Python environments (like virtual environments) can have different sets of installed packages¹. So make sure you're installing packages in the same Python environment where you're trying to use them¹.

Source: Conversation with Bing, 9/12/2023
(1) Python Virtual Environments: A Primer – Real Python. https://realpython.com/python-virtual-environments-a-primer/.
(2) undefined. https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/.
(3) . https://bing.com/search?q=create+project+specific+environment+in+python.
(4) How to Set Up a Virtual Environment in Python – And Why It's Useful. https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/.
(5) Managing environments — conda 23.7.4.dev64 documentation. https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html.
(6) Configure a virtual environment | PyCharm Documentation - JetBrains. https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html.
(7) undefined. https://www.dataquest.io/blog/a-complete-guide-to-python-virtual-environments/.
(8) undefined. https://code.visualstudio.com/docs/python/environments.


#### How to setup virtualenv and venv
##### Creating virtualenv with Python 2
-  on Mac, or Linux OS
   > pip install virtualenv <venv name>
- On Windows:
   > pip install virtualenv <venv name>
- Activate the virtual environment with this command
> source venv/bin/activate
> venv/Scripts/activate
- 