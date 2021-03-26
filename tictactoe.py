# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 19:13:38 2021

@author: Dustin

This program allows to play the popular classic Tic Tac Toe in a two player mode.

"""

#   |   |   |
#   |   |   |
#   |   |   |

class Board_Creator:
    """
    This class creates a board for a game of Tic Tac Toe and contains the necessary functions for it.
    """
    def __init__(self):
        """

        Initilizes the empty board.

        """
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    def make_turn(self, move, player):
        """
        If it was a valid move the player symbol gets added to the position of the move

        Parameters
        ----------
        move : Integer
            This is where the player wants to place a sign (0-8) on the board.
        player : Player
            This is the current active player.

        Returns
        -------
        bool
             True if valid move else False

        """
        if self.valid_move(move):
            self.board[move] = player.symbol
            return True
        return False

    def valid_move(self, move):
        """
        Checks the move of validity. A move is valid if the position is not occupied yet.

        Parameters
        ----------
        move : Integer
            This is where the player wants to place a sign (0-8) on the board.

        Returns
        -------
        bool
            Returns True if the move was valid.

        """
        if self.board[move] == 0:
            return True
        else:
            return False
    
    def check_win(self,player):
        """
        Checks if a player has won the game.

        Parameters
        ----------
        player : Player
            Current active player.

        Returns
        -------
        bool
            Returns True if a player has three in a row.

        """
        s = player.symbol
        if self.board[0] == s and self.board[1] == s and self.board[2] == s:
            return True
        elif self.board[3] == s and self.board[4] == s and self.board[5] == s:
            return True
        elif self.board[6] == s and self.board[7] == s and self.board[8] == s:
            return True

        elif self.board[0] == s and self.board[3] == s and self.board[6] == s:
            return True
        elif self.board[1] == s and self.board[4] == s and self.board[7] == s:
            return True
        elif self.board[2] == s and self.board[5] == s and self.board[8] == s:
            return True

        elif self.board[0] == s and self.board[4] == s and self.board[8] == s:
            return True
        elif self.board[2] == s and self.board[4] == s and self.board[6] == s:
            return True

    def sign_to_printable(self, sign):
        """
        Transforms the players value to a printable sign. Player 1 = X and Player 2 = O

        Parameters
        ----------
        sign : Integer
            Integer value of the sign of a player.

        Returns
        -------
        str
            Returns a X for player 1 and O for player 2.

        """
        if sign == 0:
            return " "
        elif sign == 1:
            return "X"
        else:
            return "O"
        
    def print_board(self):
        """
        Prints the board.

        Returns
        -------
        None.

        """
        print(" " + self.sign_to_printable(self.board[0]) +" | " + self.sign_to_printable(self.board[1]) +  " | " + self.sign_to_printable(self.board[2]) + " \n" + 
              " " + self.sign_to_printable(self.board[3]) +" | " + self.sign_to_printable(self.board[4]) +  " | " + self.sign_to_printable(self.board[5]) + " \n" + 
              " " + self.sign_to_printable(self.board[6]) +" | " + self.sign_to_printable(self.board[7]) +  " | " + self.sign_to_printable(self.board[8]) + " \n")
           
    def is_full(self):
        """
        Checks if the board is full.

        Returns
        -------
        bool
            Returns False if there are still free spots (0) on the board.

        """
        for i in self.board:
            if i == 0:
               return False
        print("It is a tie!")
        self.print_board()
        return True
       
                   

class Player:

    def __init__(self, symbol):
        """
        This function initilizes a player object.

        Parameters
        ----------
        symbol : Integer
            Integer representation of the symbol of a player.

        Returns
        -------
        None.

        """
        self.symbol = symbol


        
       
if __name__ == '__main__':
    player_a = Player(1) # Create player 1 
    player_b = Player(-1) # Create player 2
    match = Board_Creator() # Create a board
    active_player = player_a # set player 1 as active
      
    def switch_players(player):
        """
        Switches the active player

        Parameters
        ----------
        player : Player
            Current active player.

        Returns
        -------
            Next player.
        """
        if player == player_a:
            return player_b
        else:
            return player_a
        
    while not match.is_full(): 
        match.print_board()
        try: 
            move = int(input("Where do you want to place your sign? (1-9) "))
        except ValueError:
            print("Please enter only numbers from 1 to 9!")
            continue
        move = move - 1
        if move < 0 or move > 8:
            print("Please enter a number between 1 and 9!")
            continue
        if not match.make_turn(move, active_player):
            print("This space is already occupied. Please choose another position!")
            continue
        if match.check_win(active_player):
            print("Congratulations! You won!")
            match.print_board()
            break
        active_player = switch_players(active_player)          
