
def isValidChessBoard(board):
        if "bking" not in board.values() or "wking" not in board.values():
            return False

        black_pieces = 0
        white_pieces = 0
        for i in board.values():
            if i[0] == "b":
                black_pieces += 1
            elif i[0] == "w":
                white_pieces += 1
        if black_pieces >= 17 or white_pieces >= 17:
            return False

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
        square = list(board)  
        
        y = ["1", "2", "3", "4", "5", "6", "7", "8"]
        vertical = [s[0] for s in square]  
        if not all(i in y for i in vertical):
            return False

        x = ["a", "b", "c", "d", "e", "f", "g", "h"]
        horiz = [s[1] for s in square]  
        if not all(i in x for i in horiz):  
            return False

        
        for i in board.values():
            if i[0] != "b" and i[0] != "w":
                return False

        pieces_names = ["pawn", "knight", "bishop", "rook", "queen", "king"]
        for i in board.values():
            if i[1:] not in pieces_names:
                return False
        return True


print(isValidChessBoard({"1h": "bking", "6c": "wqueen", "2g": "bbishop", "5h": "bqueen", "3e": "wking"}))  # True
print(isValidChessBoard({"8h": "bbishop", "5k": "bking", "4f":"frook"}))  
print(isValidChessBoard({"4b": "wking", "3d": "wking", "3c": "bbishop"}))  #program doesnt check if 2 kings are side by side, soemthing which is not possible in actual chess
print(isValidChessBoard({"1a": "bking", "9z": "wking"}))  