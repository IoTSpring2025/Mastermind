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

### ML Model setup
The dataset and base code were adapted from here: [Kaggle Link](https://www.kaggle.com/datasets/gpiosenka/cards-image-datasetclassification)
Right now, I trained the initial model using a T4 GPU on Google Collaboratory. To run inference with the model, you need to be running on a device with the same processor (GPU vs CPU) that the model was trained on. The model weights are saved in the 

I.e., if I train the model on a GPU and save the weights (right now I save them to [weights.pth](Mastermind/model/weights.pth)), in order to run inference with this model, I need to use a device with a GPU (I am not able to run inference on my PC that does not have GPU/CUDA support).

### Docker
We will use Docker to containerize our web server application so that we can run it in AWS. We need to decide on if we should run it in ECS or EC2. But this server will have an API endpoint where we can make an HTTP POST request via the Raspberry Pi and receive the predicted class in return.

To build the docker container locally, run

`docker build . -t <CONTAINER_NAME>`

then, to run the container run

`docker run -p 80:80 <CONTAINER_NAME>`

Or, just run the scripts called [build_docker.sh](Mastermind/build_docker.sh) and [run_docker.sh](Mastermind/run_docker.sh) respectively, which just do the same thing. You can run it like this:

`./build_docker.sh`

A really helpful way to debug the container can be to run 

`docker run -it <CONTAINER_NAME> sh` 

to open a shell in the container.

It can also be helpful to install Docker Desktop if you want to view your containers that ways
