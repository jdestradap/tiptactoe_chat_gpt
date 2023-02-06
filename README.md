
# Tic Tac Toe

A simple Tic Tac Toe game built with Flask and ReactJS. This game allows players to play Tic Tac Toe against each other on the same device or over a network.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them:

-   Python 3.x
-   NodeJS and npm
-   pip

### Installing

A step by step series of examples that tell you how to get a development env running.

Clone the repository to your local machine:


`git clone https://github.com/<your-username>/tic-tac-toe.git` 

Create a virtual environment and activate it:

bashCopy code

    python -m venv venv
    source venv/bin/activate

Install the required dependencies:

`pip install -r requirements.txt` 

Go to the ReactJS app directory:

`cd tic-tac-toe/client` 

Install the required dependencies:

`npm install` 

## Running the program

In order to run the program, two servers need to be started: one for the Flask app and one for the ReactJS app.

Start the Flask app:

makefileCopy code

`FLASK_APP=app.py FLASK_ENV=development flask run` 

Start the ReactJS app:

sqlCopy code

`npm start` 

Open a web browser and go to [http://localhost:3000](http://localhost:3000/) to play the game.

## Built With

-   [Flask](https://flask.palletsprojects.com/en/1.1.x/) - A micro web framework written in Python
-   [ReactJS](https://reactjs.org/) - A JavaScript library for building user interfaces

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://chat.openai.com/chat/LICENSE.md) file for details.