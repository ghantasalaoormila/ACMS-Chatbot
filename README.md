# ACMS-Chatbot
A project under Amazon Campus Mentorship Series.

## Project Requirements
1. Python3: You can easily install Python 3 (along with the pip3 tool) from [python.org](https://www.python.org/)</br>
2. Django==2.0.6: use pip3 to install Django. 
```
$ pip3 install django
```
3. Chatterbot==1.0.0a1 use pip3 to install chatterbot
```
$ pip3 install chatterbot
```

That's it! That is all you need to get started.

## Features
A Chatbot to answer College Queries. Students can ask questions related to the Curriculum or Programme and get answers from the Bot.

## How to use:
Clone the project into your local system. Navigate to the project directory and run:
```
$ python3 manage.py runserver
```
A server will be started at http://127.0.0.1:8000/ <br>
You can access it by opening in any browser. 

The file chatbot.py contains code for training the model. It is kept separeately because now we need not train the model everytime the server starts. It is pre-trained and can be loaded while using. The model is then saved to the file database.sqlite3. It is then read in views.py and corresponding responses to the questions are computed. 
