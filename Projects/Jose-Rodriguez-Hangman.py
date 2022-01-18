import random
word_list = ["Monopoly", "Clue", "Jenga", "Uno", "Scrabble", "Risk",
"Chess", "Checkers", "Battleship", "Sorry!" ]

def display_hangman(tries):
 stages = [ """
                 --------
                |   |
                |   O
                |  /|\\
                |   |
                |  / \\
                -
                """,
                """
                 --------
                |   |
                |   O
                |  /|\\
                |   |
                |  /
                -
                """,
                """
                 --------
                |   |
                |   O
                |  /|\\
                |   |
                |
                -
                """,
                """"
                 --------
                |   |
                |   O
                |  /|
                |   |
                |
                -
                """,
                """
                 --------
                |   |
                |   O
                |   |
                |   |
                |
                -
                """,
                """
                 --------
                |   |
                |   O
                |
                |
                |
                -
                """,
                """
                 --------
                |   |
                |
                |
                |
                |
                -
                """,
    ]