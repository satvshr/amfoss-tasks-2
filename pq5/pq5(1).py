
def isValidChessBoard(board):
        # check for one black and one white king
        if "bking" not in board.values() or "wking" not in board.values():
            return False

        # check for a maximum of 16 pieces per player
        black_pieces = 0
        white_pieces = 0
        for i in board.values():
            if i[0] == "b":
                black_pieces += 1
            elif i[0] == "w":
                white_pieces += 1
        if black_pieces >= 17 or white_pieces >= 17:
            return False

        # check for at most 8 pawns per player

        if sum(i == "bking" for i in board.values()) > 1 or sum(i == "wking" for i in board.values()) > 1:
            return False
        if sum(i == "bqueen" for i in board.values()) > 1 or sum(i == "wqueen" for i in board.values()) > 1:
            return False
        if sum(i == "bpawn" for i in board.values()) >8 or sum(i == "wpawn" for i in board.values()) > 8:
            return False
        if sum(i == "bbishop" for i in board.values()) > 2 or sum(i == "wbishop" for i in board.values()) > 2:
            return False
        if sum(i == "bknight" for i in board.values()) > 2 or sum(i == "wknight" for i in board.values()) >  2:
            return False        
        if sum(i == "brook" for i in board.values()) > 2 or sum(i == "wrook" for i in board.values()) > 2:
            return False

        # check for a valid location
        square = list(board)  # create list of dictionary keys. eg: ['1h', '6c', '2g', '5h', '3e']
        y = ["1", "2", "3", "4", "5", "6", "7", "8"]
        vertical = [s[0] for s in square]  # removes letters from list. eg: ['1', '6', '2', '5', '3']
        if not all(i in y for i in vertical):  # checks if all values from vertical are in the y-list
            return False

        x = ["a", "b", "c", "d", "e", "f", "g", "h"]
        horiz = [s[1] for s in square]  # removes numbers from list. eg: ['h', 'c', 'g', 'h', 'e']
        if not all(i in x for i in horiz):  # checks if all values from horiz are in the x-list
            return False

        # check if the name starts with a "w" or "b"
        for i in board.values():
            if i[0] != "b" and i[0] != "w":
                return False

        # check if the pieces_names name is valid
        pieces_names = ["pawn", "knight", "bishop", "rook", "queen", "king"]
        for i in board.values():
            if i[1:] not in pieces_names:
                return False
        return True


# testing boards
print(isValidChessBoard({"1h": "bking", "6c": "wqueen", "2g": "bbishop", "5h": "bqueen", "3e": "wking"}))  # True
print(isValidChessBoard({"1a": "bpawn", "2a": "wking"}))  # False: no bking
print(isValidChessBoard({"1a": "wking", "2a": "wking", "3c": "bbishop"}))  # False: cannot have 2 white kings, no bking
print(isValidChessBoard({"1a": "bking", "9z": "wking"}))  # False: 9z is an invalid position