#p1q1
def stringToNum(s):
    return [int(x) for x in s.split(',') if x != ""]
#p1q2
def n_w_h_input(n, w, h):
    return (n.upper(), round(w, 1), round(h, 1) )
#p1q3
def n_w_h_output(n, w, h):
    print(f"{n}'s weight is {w} and his/her height is {h}")
#p1q4
def calcBMI(w, h):
    return round(w / h / h * 10000, 1)
#p1q5
def bmiCat(bmi):
    if bmi < 18.5:
        return ("Underweight")
    elif bmi < 25:
        return ("Healthy")
    elif bmi < 30:
        return ("Overweight")
    elif bmi < 40:
        return ("Obese")
    else:
        return ("Severely Obese")
#p1q6
def bmiReport(name, weight, height, bmi, weight_category):
    return {name: {
        "weight": weight,
        "height": height,
        "BMI": bmi,
        "weight category": weight_category
    }}
#p2q7
def oddList(begin,end):
    return [x for x in range(begin, end+1) if x % 2 != 0]
#p2q8
def reverseString(s):
    return s[::-1]
#p2q9
def startAndEnd(list):
    if list.begin() == list.end():
        return (True)
    else:
        return (False)
#p3q10
def createBoard():
    return(
        [["_","_","_"],
        ["_","_","_"],
        ["_","_","_"]]
        )
#p3q11
def displayBOard(board):
    print(f"[\"{board[0][0]}\",\"{board[0][1]}\",\"{board[0][2]}\"]")
    print(f"[\"{board[1][0]}\",\"{board[1][1]}\",\"{board[1][2]}\"]")
    print(f"[\"{board[2][0]}\",\"{board[2][1]}\",\"{board[2][2]}\"]")
#p3q12
def getMove():
    position=input()
    if position in ["1","2","3","4","5","6","7","8","9"]:
        return int(position)
    else:
        return False
#p3q13
def intToBoard(position):
    row = (position - 1) // 3
    col = (position - 1) % 3
    return (row, col)
#p3q14
def insertToBoard(position_tuple, board, is_x):
    row, col = position_tuple
    if board[row][col] == "_":
        if is_x:
            board[row][col] = "X"
        else:
            board[row][col] = "O"
        return (True, board)
    else:
        return (False, board)
#p3q15
def checkDraw(board):
    for row in board:
        for cell in row:
            if cell == "_":
                return False
    return True
#p3q16
def checkWin(board):
    # Row
    for r in range(3):
        if board[r][0] != "_" and board[r][0] == board[r][1] == board[r][2]:
            return True
    # Col
    for c in range(3):
        if board[0][c] != "_" and board[0][c] == board[1][c] == board[2][c]:
            return True
    # Diagonals
    if board[0][0] != "_" and board[0][0] == board[1][1] == board[2][2]:
        return True
    if board[0][2] != "_" and board[0][2] == board[1][1] == board[2][0]:
        return True
    return False