# MLops_iCodeGuru

Within this digital space, I have meticulously curated a treasure trove of golden tips, insightful words, and illuminating lectures.

## Host  

[Sir Zafar Shahid](https://www.linkedin.com/in/zafarshahid/)


| speakers 🗣 | Moderators 🌟| 
|----------|----------|
| [Ma'am Rehmana Younius](https://www.linkedin.com/in/rehmana-younis/) | [Ma'am Asia Hassan]() | 
| [Sir AqibRehman PirZada](https://www.linkedin.com/in/aqibrehman-pirzada-ml/) | [Sir Muhammad Talha](https://www.linkedin.com/in/muhammadtalha01/)| 


## Week 1

Summery as learn about baic of machine learning operations, importance from business and indusrial point of view. Stages of machine learning operations:
  - Data collection
    - Warehouse, Apis, CSV files etc.
  - Model Development
    - Alogrithms
    - Hyperparameters
  - Model validation
    - With respect to ML pipeline feature includes: f1-m1=====m2-f2
    - Modularization of code
    - tracking all experiments including change in code, configuration and parameters
    - CI approach to automate pipeplines includes initiatem reviews and approve process.
  - Model Development
  - Model Monitoring
    - Resource monitoring
    - alerts
  - Model Updating
  - Governace and Compliance
    - Model Transdepancy
    - Data privacy etc.   
  
.

## Week 2

VCS (`Version control system`) in GitHub, bacis commands, and importance of github for every coder/programmer. 

- Set username and email globally 

      git config –global user.email “Your email”

      git config –global user.user “Your user”

- Initializes a new Git repository in the current directory.

      git init

- Creates a new Git repository in the specified directory

      git init <directory>

- Clones a repository from a remote server to your local machine.

      git clone "URL repo"

- Adds all modified and new files to the staging area

      git add .

- Shows the current state of your repository, including tracked and untracked files, modified files, and branch information.
  
      git status

- Creates a new commit with the changes in the staging area and specifies the commit message inline

      git commit -m "message"  

 - Pushes local commits to the specified remote repository
 
       git push origin main

About git [more](https://www.geeksforgeeks.org/git-cheat-sheet/)

### Directory Flow 

```

(Main folder) proj_name
  - (sub-folder) configuration

      config.py -> there are 2 functions written init: f1, f2

      init.py # this is cruial. for Linking to other files

  - (sub-folder) Processing

      data_hand.py
      init.py # this is cruial. for Linking to other files

  - (sub-folder) Model Training

      init.py		# this is cruial. for Linking to other files

  - (sub-folder) Test

      init.py		# this is cruial. for Linking to other files

  - (file) model.py

      model.py link to configuration file by like: (from configuration.config imoprt f1)

```

### Project Flow

  Through the different stages like
  - Reading-file,
  - Preprocessing,
  - Visualiztion,
  - Feature-Engineering,
  - Split-data,model-train,
  - Model-evaluation

### YAML
  Berife intro about YAML and usecase, importance and syntax.

## Week 3

### Uni-testing see the file `Sir AqibRehman-file.ipynb`

- Docker Engin
- Docker compoents
- Kubeneretes
- Cluster (Master & worker node)
- Pods


## Week 4

Presentations and Discuss on errors.

Deployment on web application using

- Streamlit

Berife explaination on 
- Libraries
    - Streamlit
    - Gradio
- Framworks
    - Flask
    - Django
    - FlastApi
      
## Week 5


----
If this repo helpful to take initial step so give it star ⭐.
