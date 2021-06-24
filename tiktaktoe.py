#!/usr/bin/env python
# coding: utf-8

# In[1]:


X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9


# In[2]:


def display_instructions():
    print(
    """
    Welcome to a game of Tic-Tac-Toe. You will be playing against an AI.
    You will be able to make your move on the board by entering any number from 0 - 8.
    The number will correspond to the board position as shown below:

                      0 | 1 | 2
                      ---------
                      3 | 4 | 5
                      ---------
                      6 | 7 | 8

    May the best player win!\n
    """
    )


# In[3]:


def ask_question(question):
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


# In[4]:


def ask_number(question, low, high):
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


# In[5]:


def pieces():
    go_first = ask_question("Do you want to go first? (y/n): ")
    if go_first == "y":
        print("\nGreat! Let the game begin.")
        human = X
        computer = O
    else:
        print("\nAlright. I will go first. Wish you all the best!")
        computer = X
        human = O
    return computer, human


# In[6]:


def new_board():
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


# In[7]:


def display_board(board):
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\n\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\n\t", board[6], "|", board[7], "|", board[8], "\n")


# In[8]:


def legal_moves(board):
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


# In[9]:


def winner(board):
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
    if EMPTY not in board:
        return TIE
    return None


# In[10]:


def human_move(board, human):
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Where will you move? (0-8): ", 0, NUM_SQUARES)
        if move not in legal:
            print("\nUn oh, looks like that square is already occupied. Choose another one.\n")
    print("Fine...")
    return move


# In[11]:


def computer_move(board, computer, human):
    board = board[:]

    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)

    print("I shall take square number", end=" ")

    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move 
        board[move] = EMPTY

    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        board[move] = EMPTY

    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move


# In[12]:


def next_turn(turn):
    if turn == X:
        return O
    else:
        return X


# In[13]:


def congrat_winner(the_winner, computer, human):
    if the_winner != TIE:
        print(the_winner, "won!\n")
    else:
        print("It's a tie!\n")

    if the_winner == computer:
        print("Well, I won this round.  \n"
              "Better luck next time.")

    elif the_winner == human:
        print("You know what they say. \n"
              "Winner Winner Chicken Dinner!")

    elif the_winner == TIE:
        print("It's a TIE. \n"
              "Better luck next time.")


# In[14]:


def main():
    display_instructions()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)

    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)


# In[15]:


main()
input("\n\nPress the enter key to quit.")


# In[ ]:




