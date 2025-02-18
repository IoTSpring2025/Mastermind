# Mastermind

### General setup and tips with GitHub:
1. Clone the repo by clicking on "Code", copying, and then running 

`git clone <COPIED_DATA>` 

in your terminal

2. You will need to set up a virtual environment for python development. Install python and run the following: 

`python -m venv venv` 

and then run 

`source venv/bin/activate` 

if you are using a Unix OS or run 

`source venv/Scripts/activate` 

if you are on a Windows operating system (use git bash instead of command prompt)

3. After activating the virtual environment, run the following to install all of the necessary dependencies: 

`pip install -r requirements.txt`

Note: if you end up installing new dependencies, you can update this file with the current packages by running 

`pip freeze > requirements.txt`

4. If you are going to make additions/deletions to the codebase, start out in a separate branch outside of main. To do this, first run 

`git checkout -b <BRANCH_NAME>` 

to switch to a new branch.

5. Once you have made your changes, you will need to run 

`git add <UPDATED_FILES>`

then 

`git commit -m "<COMMIT_MESSAGE>"`

and then finally 

`git push origin <BRANCH_NAME>` 

to push the new branch up to the remote repository on GitHub.

6. Once you have pushed your branch, open up a Pull Request on the repository site. Then click "merge" when you are satisfied with your changes. Make sure you click "Squash and Merge." You can also add reviewers as well if you want to.

### Random but useful thing 
Assuming you have installed the requirements, you can run a linter by running

`python -m ruff format <DIRECTORY>`

which will format all of the python files in the directory specified. you can just do '.' for that
