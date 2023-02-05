#!/bin/bash

# Update Homebrew
brew update

# Install Python and pip
brew install python

# Upgrade pip
pip3 install --upgrade pip

# Install virtualenv
pip3 install virtualenv

# Create a virtual environment
virtualenv venv

# Activate virtual environment
source venv/bin/activate

# Install Flask
pip install Flask

# Create a sample Flask app
mkdir myapp
cd myapp
echo "from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()" > app.py

# Run the app
export FLASK_APP=app
flask run
