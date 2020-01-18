'''
Online for many tables or one table
Two players
Do we accept rolling back of moves?
white side plays first
Is there surrender?
how large is the chess board

'''
from enum import Enum
from abc import ABC, abstractmethod


class GameStatus(Enum):
    WHITE_WIN, BLACK_WIN, DRAW, CANCEL, Active = 1, 2, 3, 4, 5


class AccountStatus(Enum):
    ACTIVE, CLOSED, BLACKLISTED = 1,2,3


class Address:
    def __init__(self, street, city, state, zipcode):
        pass


class Person:
    def __init__(self, name, address: Address, email, phone):
        pass


class Account:
    def __init__(self, username, password):
        pass

    def reset_password(self):
        pass


class Box:
    def __init__(self, x, y, piece):
        pass

    def get_piece(self) -> Piece:
        pass

    def set_piece(self, piece):
        pass

    def get_x(self):
        pass

    def set_x(self, x):
        pass

    def get_y(self):
        pass

    def set_y(self):
        pass


class Piece(ABC):
    def __init__(self, white=False):
        self.__white = white
        self.__killed = False

    def is_white(self):
        return self.__white

    def is_killed(self):
        return self.__killed

    def set_white(self, white):
        self.__white = white

    def set_killed(self, killed):
        self.__killed = killed

    @abstractmethod
    def can_move(self, board, start_box, end_box):
        pass


class King(Piece):
    def __init__(self, white):
        super(King, self).__init__(white)
        self.__castling_done = False

    def get_castling_done(self):
        return self.__castling_done

    def set_castling_done(self, castling_done):
        self.__castling_done = castling_done

    def can_move(self, board, start_box: Box, end_box: Box):
        if end_box.get_piece().is_white() == self.is_white():
            return False

        x = abs(start_box.get_x() - end_box.get_x())
        y = abs(end_box.get_x() - end_box.get_y())
        if x + y == 1:
            return True

        return self.is_valid_castling(board, start_box, end_box)

    def is_valid_castling(self, board, start_box: Box, end_box: Box):
        if self.get_castling_done():
            return False

        #  Other logic


class Knight(Piece):
    def can_move(self, board, start_box, end_box):
        if end_box.get_piece().is_white() == self.is_white():
            return False
        x = abs(start_box.get_x() - end_box.get_x())
        y = abs(end_box.get_x() - end_box.get_y())
        return x * y == 2



class Board:
    def __init__(self):
        self.__boxes = []

    def reset(self):
        boxes = [[None] * 8 for _ in range(8)]
        # initialize white pieces
        boxes[0][0] = Box(0, 0, Rook(True))
        boxes[0][1] = Box(0, 1, Knight(True))
        boxes[0][2] = Box(0, 2, Bishop(True))
        # ...
        boxes[1][0] = Box(1, 0, Pawn(True))
        boxes[1][1] = Box(1, 1, Pawn(True))
        # ...

        # initialize black pieces
        boxes[7][0] = Box(7, 0, Rook(False))
        boxes[7][1] = Box(7, 1, Knight(False))
        boxes[7][2] = Box(7, 2, Bishop(False))
        # ...
        boxes[6][0] = Box(6, 0, Pawn(False))
        boxes[6][1] = Box(6, 1, Pawn(False))
        # ...

        # initialize remaining boxes without any piece
        for i in range(2, 6):
            for j in range(0, 8):
                boxes[i][j] = Box(i, j, None)


    def get_box(self, x, y):
        if not (0 <= x < 8 and 0 <= y < 8):
            raise Exception('')
        return self.__boxes[x][y]


class Player(Account):
    def __init__(self, person: Person, white_side=False):
        pass

    def is_white_side(self):
        pass


class Move:
    def __init__(self, player, start_box, end_box, piece_killed, castling_move=False):
        self.__player = player
        self.__start = start_box
        self.__end = end_box
        self.__piece_moved = self.__start.get_piece()
        self.__piece_killed = piece_killed
        self.__castling_move = castling_move

    def is_castling_move(self):
        return self.__castling_move

    def set_castling_move(self, castling_move):
        self.__castling_move = castling_move


class Game:
    def __init__(self):
        self.__players = []
        self.__board = Board()
        self.__current_turn = None
        self.__game_status = GameStatus.ACTIVE
        self.__moves_played = []

    def start_new_game(self, player1: Player, player2: Player):
        self.__players[0] = player1
        self.__players[1] = player2
        self.__board.reset()

        if player1.is_white_side():
            self.__current_turn = player1
        else:
            self.__current_turn = player2

        self.__moves_played = []

    def is_end(self):
        return self.__game_status != GameStatus.Active

    def player_move(self, player, start_x, start_y, end_x, end_y):
        start_box = self.__board.get_box(start_x, start_y)
        end_box = self.__board.get_box(end_x, end_y)
        move = Move(player, start_box, end_box, None)
        return self.make_move(move, player)

    def make_move(self, move, player):
        source_piece = move.get_start().get_piece()
        if source_piece is None:
            return False

        if player != self.__current_turn:
            return False

        if source_piece.iswhite() != player.is_white_side():
            return False

        if not source_piece.can_move(self.__board, move.get_start(), move.get_end()):
            return False

        dest_piece = move.get_start().get_piece()
        if dest_piece is not None:
            dest_piece.set_killed(True)
            move.set_pieceKilled(dest_piece)

        if isinstance(source_piece, King) and source_piece.is_castling_move():
            move.set_castling_move(True)

        self.__moves_played.append(move)

        move.get_end().set_piece(move.get_start().get_piece())
        move.get_start().set_piece(None)

        if isinstance(dest_piece, King):
            if player.is_white_side():
                self.set_status(GameStatus.WHITE_WIN)
            else:
                self.set_status(GameStatus.BLACK_WIN)

        if self.__current_turn == self.__players[0]:
            self.__current_turn = self.__players[1]
        else:
            self.__current_turn = self.__players[0]
        return True


