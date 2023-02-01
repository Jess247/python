validChessboard = {"1b": "wrook", "b1": "wknight",
                   "c1": "wbishop", "d1": "wqueen", "e1": "wqueen"}
inValidChessboard = {"1b": "wrook", "b1": "wknight",
                     "c1": "wbishop", "d1": "wqueen", "fd": "wqueen"}


def validateChessboard(board):
    if board == validChessboard:
        print(True)
    else:
        print(False)


validateChessboard(inValidChessboard)
