# StudyBuddy Forum 

This is a simple forum web application built in Flask framework in Python.
The idea is for students of asrjc to interact with each other on an online platform dedicated to making learning efficient. They can do this by either posting a question related to their lessons in asrjc or answering a question posted by other students in asrjc. This way, not only can students clarify their doubts quickly, they can also revise and help others at the same time by answering questions posted by other students.

## Features

* Add accounts
* Listing the topics
* Asking questions and responding with answers
* Like option for topics and answers


In the future, this can be extended by incorporating more features like:

* Security to ensure only Anderson Serangoon Junior College students can participate
* Notification to user who raised the question, when there are new answers
* Change password 
* Manage categories and limit them
* Providing a search option to search through topics and replies

## Why I made it

I made this forum as part of JC-1 Computing project to apply client side (HTML5) and server side (Python) concepts.
Also, to make a response web application

## How to build the source code

### From scratch

1. Download the source code:

```bash
git clone https://gitea.com/chopin42/simple-forum
cd simple-forum
```

2. Install Python (pre-requisite) first, and then the depedencies

```bash
pip3 install -r requirements.txt --user
```
Reference for Python installation: https://realpython.com/installing-python/ 

3. Run the main file:

```bash
python app.py
```

