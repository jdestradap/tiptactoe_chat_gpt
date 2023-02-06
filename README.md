
# Tic Tac Toe

This is a Tic Tac Toe game that can be played in your browser. The game is made up of two parts: a Flask app and a React app.

## Running the program

### Flask app

1.  Navigate to the Flask app directory
2.  Install the required packages by running `pip install -r requirements.txt`
3.  Start the Flask app by running `flask run`
4.  The Flask app should now be running on `http://localhost:5000`

### React app

1.  Navigate to the React app directory
2.  Install the required packages by running `npm install`
3.  Start the React app by running `npm start`
4.  The React app should now be running on `http://localhost:3000`

## How the program works

The React app is responsible for displaying the game board, handling user inputs and communicating with the Flask app through API calls.

When the React app starts, it makes a call to the Flask app to get the initial state of the game board and the current player. After that, every time a player makes a move, the React app sends a PUT request to the Flask app with the index of the cell that was clicked. The Flask app then updates the game board and sends back the updated state to the React app.

The game ends when one of the players gets three in a row or when all the cells are filled without a winner. The React app then displays the winner if there is one, otherwise it shows that the game ended in a draw.

## Enjoy the game!

Hope you enjoy playing this Tic Tac Toe game!