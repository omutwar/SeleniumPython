# Selenium Python Project

...
This is new python project to keep my competence in check.
...

## How to rename a local branch to new branch
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
>   wait = WebDriverWait(driver, 10)
>   wait.until(EC.element_to_be_clickable(By.XPATH, <locator>))

### NOTE: How To Install Venv
-- In Windows, we can install it by going to the python installation directory, then type <python.exe -m venv <path-to-install-the-package>

-- In Windows, the <activate> file is located inside the <Scripts> directory, while in Mac/Linux, it may be inside the <bin> directory
