# ACMS-Chatbot (AIML)
Chatbot for College Queries. An AIML based Maven project in JAVA.

## Requirements:
Eclipse </br>
Maven </br>
Tomcat v9.0 server </br>
Jersey artifacts in Maven </br>
Java 8 </br>
Program-ab </br>

## Getting Started
It is advised to import this project in eclipse. To run the project, do Maven Clean Install
and then Run on a Tomcat Server. 

### Things to Setup:
Change the path to AIML files. It has to be the path in your local machine. The AIML files are located in resources folder of the
project. In line 85 of the file Chatbot.java, give the path of the directory where the project is present.

Change the path to Google API key file: To use the google API for translating a sentence, add the key file to environment variable.
In eclipse, in run configration, go to environment tab and add a variable where the path is path to the key file which is present in
the resources folder of the project (a json file).

### Flow of the project:
Running the server at localhost using Tomcat server. APIs included in MyResource.java in src/chatbot folder. Home page is included 
in src/main/webapp folder which is index.html. An Ajax call is sent to API getResponse in MyResources class. It then calls getResponse 
function in the Singleton class Chatbot. Maintaining only one instance of the Chatbot class is important because context has to be 
saved for each user. Hence I have used a Singleton class. In the function getResponse, there is code to detect the language, convert
it into english, get the response from the Bot object and then translate back to the required language.
