from flask import Flask, request

app = Flask(__name__)
board = [' ' for x in range(9)]

current_player = 'X'
def check_victory(player, board):
    return (
        (board[0] == player and board[1] == player and board[2] == player) or
        (board[3] == player and board[4] == player and board[5] == player) or
        (board[6] == player and board[7] == player and board[8] == player) or
        (board[0] == player and board[3] == player and board[6] == player) or
        (board[1] == player and board[4] == player and board[7] == player) or
        (board[2] == player and board[5] == player and board[8] == player) or
        (board[0] == player and board[4] == player and board[8] == player) or
        (board[2] == player and board[4] == player and board[6] == player)
    )

def check_draw(board):
    return all([x != ' ' for x in board])

@app.route("/")
def index():
    return "Welcome to Tic Tac Toe API!"

@app.route("/board", methods=["GET"])
def get_board():
    return {"board": board, "current_player": current_player}

@app.route("/board", methods=["PUT"])
def play_turn():
    global current_player
    index = int(request.form.get("index"))
    if board[index] == ' ':
        board[index] = current_player
        if check_victory(current_player, board):
            return {"message": f"{current_player} wins!"}
        elif check_draw(board):
            return {"message": "Draw!"}
        else:
            current_player = 'X' if current_player == 'O' else 'O'
            return {"board": board, "current_player": current_player}
    else:
        return {"error": "Invalid move"}


if __name__ == "__main__":
    app.run()