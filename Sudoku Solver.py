import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

def plot_series(x, y, xlen=10, ylen=6, xlabel="", ylabel="", grid=True, format="-", start=0, end=None):
    plt.figure(figsize=(xlen,ylen))
    plt.plot(x[start:end], y[start:end], format)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(grid)

cords = []
cords_dict = {}

for row in range(0,9):
    for col in range(0,9):
        cord = [row,col]
        square_cord = [row//3,col//3]
        square = ((row//3) * 3) + (col//3)
        cords.append(cord)
        cords_dict.update({len(cords_dict) : {'cord' : cord,
                                              'row' : row,
                                              'col' : col,
                                              'square_cord' : square_cord,
                                              'square' : square}})

print(cords)
print(cords_dict)

def get_distinct_cords_lists():

    distinct_cords_lists = []

    for n in range(0,9):
        row_cords = []
        col_cords = []
        square_cords = []
        for cord in cords:
            row, col = cord[0], cord[1]
            square = ((row//3) * 3) + (col//3)
            if row == n:
                row_cords.append(cord)
            if col == n:
                col_cords.append(cord)
            if square == n:
                square_cords.append(cord)
        distinct_cords_lists.append(row_cords)
        distinct_cords_lists.append(col_cords)
        distinct_cords_lists.append(square_cords)

    return distinct_cords_lists

def get_lists(grid, row, col):

    row_list = [num for num in grid[row] if num != 0]
    col_list = [x[col] for x in grid if x[col] != 0]
    trio = [row // 3, col // 3]
    square_list = []

    for row in range(0,9):
        for col in range(0,9):
            other_cell_trio = [row // 3, col // 3]
            if other_cell_trio == trio:
                if grid[row][col] != 0:
                    square_list.append(grid[row][col])

    return row_list, col_list, square_list

def find_values(cell_row, cell_col, skip_values=[]):

    row_list, col_list, square_list = get_lists(grid, cell_row, cell_col)

    possible_values = []

    for value in range(1,10):
        if value not in row_list and value not in col_list and value not in square_list and value not in skip_values:
            possible_values.append(value)

    return possible_values

def show_grid(message=''):

    print(message)
    print()
    for r in grid:
        print(r)
#         print(f"{r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} | {r[5]} | {r[6]} | {r[7]} | {r[8]}")
#         print('-'*33)
    print()

def show_guesses():
    for guess in guesses:
        print(f'{guess} : {guesses[guess]}')
    print('')

def get_possibilities(mode):

    poss_empty_cords = []

    for cord in cords:
        row, col = cord[0], cord[1]
        if grid[row][col] == 0:
            possible_values = find_values(row, col)

            poss_empty_cords.append({
                'cord'            : cord,
                'row'             : row,
                'col'             : col,
                'possible_values' : possible_values,
                'possibilities'   : len(possible_values)
            })

    if len(poss_empty_cords) > 0:
        poss_empty_cords_df = pd.DataFrame(poss_empty_cords)
    else:
        poss_empty_cords_df = pd.DataFrame([{
                'cord'            : None,
                'row'             : None,
                'col'             : None,
                'possible_values' : None,
                'possibilities'   : None
            }])

    if mode == 'quick':
        sort_by = ['possibilities','row','col']
    elif mode == 'relentless':
        sort_by = ['row','col']

    poss_empty_cords_df.sort_values(by=sort_by, axis=0, ascending=True, inplace=True)
    poss_empty_cords_df.reset_index(drop=True, inplace=True)

    zero_poss_empty_cords = poss_empty_cords_df[poss_empty_cords_df['possibilities'] == 0].values.tolist()

    return poss_empty_cords, zero_poss_empty_cords

def assess_dupe_error():

    dupe_error = False

    lists = []

    for cord in cords:
        row, col = cord[0], cord[1]
        row_list, col_list, square_list = get_lists(grid, row, col)
        for list in [row_list, col_list, square_list]:
            if len(list) != len(set(list)):
                dupe_error = True

    return dupe_error

def assess_homeless_error():

    homeless_error = False

    # use get_distinct_cords_lists() to get current values and remaining possibilities for each row, col, and square list
    # if any number 1-9 is missing from those values and possibilities then flag homeless_error

    distinct_cords_lists = get_distinct_cords_lists()

    for cords_list in distinct_cords_lists:
        list_current_and_poss_values = []
        for cord in cords_list:
            row, col = cord[0], cord[1]
            value = grid[row][col]
            if value != 0:
                list_current_and_poss_values.append(value)
            else:
                possible_values = find_values(row, col)
                for poss_value in possible_values:
                    if poss_value not in list_current_and_poss_values:
                        list_current_and_poss_values.append(poss_value)

        list_current_and_poss_values = sorted(list_current_and_poss_values)
        ideal_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        if list_current_and_poss_values != ideal_list:
            homeless_error = True
            break

    return homeless_error

def get_most_recent_guess():

    guess_list = []

    for guess in guesses:
        guess_list.append(guess)

    if len(guesses) > 1:
        most_recent_guess_index = max(guess_list)
    else:
        most_recent_guess_index = 0

    most_recent_guess = guesses[most_recent_guess_index]

    cord = most_recent_guess['cord']
    last_guess = most_recent_guess['guess']
    possible_values = most_recent_guess['possible_values']
    failed_guesses = most_recent_guess['failed_guesses']

    return most_recent_guess_index, most_recent_guess, cord, last_guess, possible_values, failed_guesses

grids = {

    'easy' : [[0,0,0,2,6,0,7,0,1],
              [6,8,0,0,7,0,0,9,0],
              [1,9,0,0,0,4,5,0,0],
              [8,2,0,1,0,0,0,4,0],
              [0,0,4,6,0,2,9,0,0],
              [0,5,0,0,0,3,0,2,8],
              [0,0,9,3,0,0,0,7,4],
              [0,4,0,0,5,0,0,3,6],
              [7,0,3,0,1,8,0,0,0]],

    'hard' : [[4,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,9,0,0,0],
              [0,0,0,0,0,0,7,8,5],
              [0,0,7,0,4,8,0,5,0],
              [0,0,1,3,0,0,0,0,0],
              [0,0,6,0,7,0,0,0,0],
              [8,6,0,0,0,0,9,0,3],
              [7,0,0,0,0,5,0,6,2],
              [0,0,3,7,0,0,0,0,0]],

    'blank' : [[0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0]]

}

grid = grids['easy']

show_grid(f'start')

###################################################################################

window = tk.Tk()

for cord in cords:
    row, col = cord[0], cord[1]
    x, y = (col + 1) * 35, (row + 1) * 35
    value = grid[row][col]
    if value != 0:
        print_value = value
    else:
        print_value = ""

    frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1, bg="black")
    frame.grid(row=y, column=x)
    label = tk.Label(master=frame, text=print_value, width=4, height=2)
    label.pack()

def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)

def next_guess(event):
    print("The next guess is...")

print('Open and close the Sudoku grid dialog on the taskbar')
print()

# Bind keypress event to handle_keypress()
# window.bind("<Key>", handle_keypress)
window.bind("<Key>", next_guess)
window.mainloop()

# while True:
#     tk.update_idletasks()
#     tk.update()

###################################################################################

loops_and_guesses = []

already_filled = 0

for row in grid:
    for x in row:
        if x > 0:
            already_filled = already_filled + 1

mode = 'quick'
# mode = 'relentless'

poss_empty_cords, zero_poss_empty_cords = get_possibilities(mode)

guesses = {}
loops = 0
loops_limit = 1000000

while len(poss_empty_cords) > 0 and loops < loops_limit:
#     print('')
#     print('New loop! ##########################################################################')
#     print('')

    dupe_error = assess_dupe_error()
    homeless_error = assess_homeless_error()
    # 1. Undo incorrect previous guess

    if len(zero_poss_empty_cords) > 0 or dupe_error or homeless_error:

        most_recent_guess_index, most_recent_guess, cord, last_guess, possible_values, failed_guesses = get_most_recent_guess()

        failed_guesses.append(last_guess)

        row, col = cord[0], cord[1]
        grid[row][col] = 0

        undos = 0

        while len(possible_values) == len(failed_guesses) and undos < 100:

            del guesses[most_recent_guess_index]

            get_most_recent_guess()

            failed_guesses.append(last_guess)

            row, col = cord[0], cord[1]
            grid[row][col] = 0

            undos = undos + 1

        for poss in possible_values:
            if poss not in failed_guesses:
                guess = poss
                break

        row, col = cord[0], cord[1]
        grid[row][col] = guess
        most_recent_guess['guess'] = guess

    # 2. Make a guess at the first cell with the least possibilities

    else:

        guess_cord = poss_empty_cords[0]
        possible_values = guess_cord['possible_values']
        guess = possible_values[0]
        cord = guess_cord['cord']
        row, col = cord[0], cord[1]
        grid[row][col] = guess
        index = len(guesses)
        guesses.update({
            index: {
                'cord'            : cord,
                'possible_values' : possible_values,
                'guess'           : guess,
                'failed_guesses'  : []
            }
        })

    poss_empty_cords, zero_poss_empty_cords = get_possibilities(mode)

    loops = loops + 1
    no_guesses = len(guesses)

    if loops % 10000 == 0:
        print(f'Loop {loops} has {no_guesses} guesses')

    loops_and_guesses.append({
        'Loop'               : loops,
        'Filled Cells'       : no_guesses,
        'Total Filled Cells' : no_guesses + already_filled,
    })

print(f'Completed {no_guesses} guesses in {loops} loops :)')
print('')
show_grid('end')

# because of a bad guess made earlier, two neighbouring cells may share the same single possibility
# these will both then be eliminated until the mistake is apparent from a cell having no possibilities
# to prevent this, get_possibilities should be run after every elimination in the for loop, and break out if some have 0 poss
# this would allow the while loop to run again straight away, discover the 0 poss cells and undo last guess and following elims

loops_and_guesses_df = pd.DataFrame(loops_and_guesses)

x_name = 'Loop'
x = loops_and_guesses_df[x_name]

for y_name in ['Filled Cells','Total Filled Cells']:
    y = loops_and_guesses_df[y_name]
    plot_series(x, y, 18, 6, x_name, y_name, grid=True)

for guess in guesses:
    print(f'{guess} : {guesses[guess]}')
