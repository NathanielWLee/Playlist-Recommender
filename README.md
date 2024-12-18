# tune-link
## AI Capstone Final Project

## Installing:
### 1. Python packages for Django:
    If using python3:
    ```
    $ pip3 install django djangorestframework
    $ pip3 install social-auth-core
    $ pip3 install social-auth-app-django
    $ pip3 install flask
    $ pip3 install flask_cors
    ```
    If using python:
    ```
    $ pip install django djangorestframework
    $ pip install social-auth-core
    $ pip install social-auth-app-django
    $ pip3 install flask
    $ pip3 install flask_cors
    ```
### 2. npm packages for front end:
    (if you don't have npm, install node.js then run $ sudo npm install npm -g
    OR
    visit https://docs.npmjs.com/getting-started)

    Step 1:

        $ npm install -g yarn

        If you encounter a permissions denied error, try:
        $ sudo npm install -g yarn

    Step 2:

        $ yarn add node-cron@2.0.3
        $ pip3 install html5lib

    Step 3:

        For the following packages, please install them in the frontend folder!

        $ npm init -y
        $ npm i webpack webpack-cli --save-dev
        $ npm i @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev
        $ npm i react react-dom --save-dev
        $ npm install @material-ui/core
        $ npm install @babel/plugin-proposal-class-properties
        $ npm install react-router-dom
        $ npm install @material-ui/icons

## To run:
### 1. Make sure you're in the tune-link-project folder
    ```
    $ cd tune-link/tune-link-project
    ```
### 2. Run
    ```
    $ .\manage.py runserver
    ```
    Click the link provided in terminal, (should be at http://127.0.0.1:8000/)
### 3. Run flask server
    ```
    $ .\manage.py runserver
    ```
    You can check on status of the chatbot question stream by going to http://127.0.0.1:5000/test
### 4. If developing, run this command which automatically recompiles whenever you make changes to the front end. Must be in frontend folder to run
    ```
    $ cd frontend
    $ npm run dev

## Troubleshooting
Currently, we have found that when encountering errors, quitting the server and clearing the browser history before relaunching is effective. Please use this method if encountering unsolvable errors for the time being.

## General reminder:
Though you need to be in the tune-link-project to run the web app, make sure to change the directory to tune-link if you make any changes to the readme and do a push from that outter directory
