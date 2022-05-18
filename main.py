from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

def split_str(str: str): #try splitting with multiple delimiters
    result = []
    if ',' in str:
        result = str.replace(" ", "").split(",")
    elif ' ' in str:
        result = str.split(" ")
    else:
        result = list(str)
    result = [int(x) for x in result]
    return result

sudoku = [[],[],[],[],[],[],[],[],[]]


def display(table): #set display string
    solved = ""
    for i in range(len(table)):
        if i % 3 == 0 and i != 0:
            solved += "\n- - - - - - - - - - - -\n"
        for j in range(len(table[0])):
            if j % 3 == 0 and j != 0:
                solved += " | "
            if j == 8:
                solved += str(table[i][j]) + "\n"
            else:
                solved += str(table[i][j]) + " "   
    solved = solved.split("\n")
    return solved
def validator(table,num,pos): #check if number is valid
    for i in range(len(table[0])):
        if table[pos[0]][i] == num and pos[1] != i:
            return False
    for i in range(len(table)):
        if table[i][pos[1]] == num and pos[0] != i:
            return False
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if table[i][j] == num and (i,j) != pos:
                return False
    return True
def notempty(table): #check for empty spaces
    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j] == 0:
                return (i,j)
    return None
def solve(table): #solve sudoku
    find = notempty(table)
    if not find:
        return True
    else:
        row,col = find

    for i in range(1,10):
        if validator(table,i,(row,col)):
            table[row][col] = i
            if solve(table):
                print(table)
                return True
            table[row][col] = 0
    return False

@app.route('/', methods=['GET', 'POST']) #get sudoku from user
def get_table():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        sudoku[0] = split_str(str(request.form['frow']))
        sudoku[1] = split_str(str(request.form['srow']))
        sudoku[2] = split_str(str(request.form['trow']))
        sudoku[3] = split_str(str(request.form['forow']))
        sudoku[4] = split_str(str(request.form['firow']))
        sudoku[5] = split_str(str(request.form['sirow']))
        sudoku[6] = split_str(str(request.form['sevrow']))
        sudoku[7] = split_str(str(request.form['eigrow']))
        sudoku[8] = split_str(str(request.form['ninrow']))
        return redirect(url_for('return_solve'))

@app.route('/solve', methods=['GET']) #return solved sudoku
def return_solve():
    solve(sudoku)
    solved = display(sudoku)
    print(solved)
    return render_template('solve.html', solved_puzzle=solved)

app.run()
display(sudoku)
solve(sudoku)
print("#########")
display(sudoku)
