import tkinter as tk

#create windows and global variables
chess_window = tk.Tk()
chess_window.title("Chess")
chess_window.configure(bg="#e8e8e8")
chess_window.geometry("800x640")
current_colour = 1
tile_list = [[], [], [], [], [], [], [], []]
colour_list = [["", "", "", "", "", "", "", ""],
               ["", "", "", "", "", "", "", ""],
               ["", "", "", "", "", "", "", ""],
               ["", "", "", "", "", "", "", ""],
               ["", "", "", "", "", "", "", ""],
               ["", "", "", "", "", "", "", ""],
               ["", "", "", "", "", "", "", ""],
               ["", "", "", "", "", "", "", ""]]
colour_tick = 0
tile_size = 6
end_game = False
calc_game_over = [0, ""]
current_turn = "#c2c2c2"
wking_check = False
bking_check = False
wking_move = False
bking_move = False
castles = [[False, False], [False, False]]
wking_castle_king = False
wking_castle_queen = False
bking_castle_king = False
bking_castle_queen = False
white_text =[""]
black_text =[""]
#end game
def game_end(colour):
    for tile_y in range(8):
        for tile_x in range(8):
            if tile_list[tile_y][tile_x]["text"] == "♚" and tile_list[tile_y][tile_x]["fg"] == colour:
                tile_list[tile_y][tile_x].configure(bg="yellow")
    chess_window.after(2500, chess_window.destroy)
#create dictionary of every colour on the board
for horizontal in range(0, 8):
    colour_tick += 1
    for vertical in range(0, 8):
        if colour_tick % 2 != 0:
            if vertical % 2 == 0:
                colour_list[horizontal][vertical] = "#eeeed2"
            else:
                colour_list[horizontal][vertical] = "#769656"
        else:
            if vertical % 2 == 0:
                colour_list[horizontal][vertical] = "#769656"
            else:
                colour_list[horizontal][vertical] ="#eeeed2"
#tiles - creates tiles and adds them to the tile list
def create_tile(tile, size, row, column, x, y):
    tile = tk.Button(chess_window, background=colour_list[y][x], font=("Segoe UI Symbol", 40), relief="flat", bd=0)
    tile.place(x=column*80, y=row*80, width=80, height=80)
    tile_list[y].append(tile)
#creating tiles with the create_tile function
for rows in range(8):
    for cols in range(8):
        tile_name = "tile" + str(cols)
        create_tile(tile_name, 6, rows, cols, cols, rows)
        current_colour += 1
move_label = tk.Label(chess_window, text="Moves:", bg="#e8e8e8")
move_label.place(x=695, y=10)
move_label_white = tk.Label(chess_window, text="W:", font=("Segoe UI Symbol", 15), bg="#e8e8e8")
move_label_white.place(x=660, y=50)
move_label_black = tk.Label(chess_window, text="B:", font=("Segoe UI Symbol", 15), bg="#e8e8e8")
move_label_black.place(x=740, y=50)
#assign pawn functions after movement / at start
def pawn_functions():
    for tile_y in range(8):
        for tile_x in range(8):
            current_tile = tile_list[tile_y][tile_x]
            if current_tile["text"] == "♟":
                current_tile.configure(command=lambda y=tile_y, x=tile_x, colour=current_tile["fg"]: view_pawn("pawn", [y, x], colour))
            if current_tile["text"] == "♞":
                current_tile.configure(command=lambda y=tile_y, x=tile_x, colour=current_tile["fg"]: view_pawn("knight", [y, x], colour))
            if current_tile["text"] == "♝":
                current_tile.configure(command=lambda y=tile_y, x=tile_x, colour=current_tile["fg"] :view_pawn("bishop", [y, x], colour))
            if current_tile["text"] == "♜":
                current_tile.configure(command=lambda y=tile_y, x=tile_x, colour=current_tile["fg"] :view_pawn("rook", [y, x], colour))
            if current_tile["text"] == "♛":
                current_tile.configure(command=lambda y=tile_y, x=tile_x, colour=current_tile["fg"] :view_pawn("queen", [y, x], colour))
            if current_tile["text"] == "♚":
                current_tile.configure(command=lambda y=tile_y, x=tile_x, colour=current_tile["fg"] :view_pawn("king", [y, x], colour))
            if current_tile["text"] == "":
                current_tile.configure(command="", fg="red")
            tile_list[tile_y][tile_x].configure(bg=colour_list[tile_y][tile_x])
#pawn movement logic
def show_turn(check_kings):
    global wking_check, bking_check
    for tile_y in range(8):
        for tile_x in range(8):
            if tile_list[tile_y][tile_x]["text"] == "♚" and tile_list[tile_y][tile_x]["fg"] == current_turn:
                tile_list[tile_y][tile_x].configure(bg="purple")
            if tile_list[tile_y][tile_x]["text"] == "♚" and tile_list[tile_y][tile_x]["fg"] == "#c2c2c2":
                check_kings[0] += 1
                if bking_check:
                    tile_list[tile_y][tile_x].configure(bg="red")
            if tile_list[tile_y][tile_x]["text"] == "♚" and tile_list[tile_y][tile_x]["fg"] == "#000000":
                check_kings[1] += 1
                if wking_check:
                    tile_list[tile_y][tile_x].configure(bg="red")
#check if king is in check
def check_for_check(pawn_pos, func_colour):
    global wking_check, bking_check
    #check if any pawn is in the checking zone
    movement_rows = [[1, 1], [-1, -1], [-1, 1], [1, -1], [0, 1], [0, -1], [-1, 0], [1, 0]]
    if func_colour == "#c2c2c2":
        opposing_colour = "#000000"
    else:
        opposing_colour = "#c2c2c2"
    def assign_check():
        global bking_check, wking_check
        if opposing_colour == "#000000":
            bking_check = True
        if opposing_colour == "#c2c2c2":
            wking_check = True
    for move in movement_rows:
        for n in range(1, 8):
            if 0 <= pawn_pos[0] + move[0] * n < 8 and 0 <= pawn_pos[1] + move[1] * n < 8:
                if tile_list[pawn_pos[0] + move[0] * n][pawn_pos[1] + move[1] * n]["fg"] == func_colour:
                    break
                if tile_list[pawn_pos[0] + move[0] * n][pawn_pos[1] + move[1] * n]["fg"] == opposing_colour and tile_list[pawn_pos[0] + move[0] * n][pawn_pos[1] + move[1] * n]["text"] in ["♝", "♛"] and move in [[1, 1], [-1, -1], [-1, 1], [1, -1]]:
                    assign_check()
                    break
                if tile_list[pawn_pos[0] + move[0] * n][pawn_pos[1] + move[1] * n]["fg"] == opposing_colour and tile_list[pawn_pos[0] + move[0] * n][pawn_pos[1] + move[1] * n]["text"] in ["♜", "♛"] and move in [[0, 1], [0, -1], [-1, 0], [1, 0]]:
                    assign_check()
                    break
    movement_knight = [[-2, -1], [-2, 1], [2, 1], [2, -1], [-1, -2], [1, -2], [1, 2], [-1, 2]]
    for move in movement_knight:
        if 0 <= pawn_pos[0] + move[0] < 8 and 0 <= pawn_pos[1] + move[1] < 8:
            if tile_list[pawn_pos[0]+move[0]+0][pawn_pos[1]+move[1]+0]["fg"] == opposing_colour and tile_list[pawn_pos[0]+move[0]][pawn_pos[1]+move[1]]["text"] in ["♞"]:
                assign_check()
    movement_pawn = [[-1, 1], [-1, -1], [1, 1], [1, -1]]
    for move in movement_pawn:
        if 0 <= pawn_pos[0] + move[0] < 8 and 0 <= pawn_pos[1] + move[1] < 8:
            if tile_list[pawn_pos[0]+move[0]+0][pawn_pos[1]+move[1]+0]["fg"] == opposing_colour and tile_list[pawn_pos[0]+move[0]][pawn_pos[1]+move[1]]["text"] in ["♟"]:
                assign_check()
    #check for checkmate
    movement_king = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    available_spaces = 0
    for move in movement_king:
        if 0 <= pawn_pos[0] + move[0] < 8 and 0 <= pawn_pos[1] + move[1] < 8:
            if tile_list[pawn_pos[0]+move[0]][pawn_pos[1]+move[1]]["text"] == "":
                if func_colour == "#c2c2c2" and wking_check:
                    available_spaces += 1
                if func_colour == "#000000" and bking_check:
                    available_spaces += 1
    if available_spaces == 0 and (wking_check or bking_check):
        #game_end(func_colour)
        pass
def view_pawn(pawn_type, pawn_pos, pawn_colour):
    global castles
    for tile_y in range(8):
        for tile_x in range(8):
            tile_list[tile_y][tile_x].configure(bg=colour_list[tile_y][tile_x])
    func_colour = pawn_colour
    if func_colour == current_turn and not end_game:
        if func_colour == "#c2c2c2":
            opposing_colour = "#000000"
        else:
            opposing_colour = "#c2c2c2"
        if pawn_type == "pawn":
            if pawn_colour == "#c2c2c2":
                movement = [[-1, 0], [-1, 1], [-1, -1]]
            else:
                movement = [[1, 0], [1, 1], [1, -1]]
            for move in movement:
                if 0 <= pawn_pos[0]+move[0] < 8 and 0 <= pawn_pos[1]+move[1] < 8:
                    if tile_list[pawn_pos[0]+move[0]][pawn_pos[1]+0]["text"] == "" and move in [[1, 0], [-1, 0]]:
                        tile_list[pawn_pos[0]+move[0]][pawn_pos[1]].configure(bg="blue", command=lambda: move_pawn([pawn_pos[0], pawn_pos[1]], [pawn_pos[0]+move[0], pawn_pos[1]], "♟", func_colour))
                        if 0 <= pawn_pos[0]+move[0] < 8 and (pawn_pos[0] == 6 or pawn_pos[0] == 1) and tile_list[pawn_pos[0]+move[0]*2][pawn_pos[1]+0]["text"] == "":
                            tile_list[pawn_pos[0]+move[0]*2][pawn_pos[1]].configure(bg="blue", command=lambda: move_pawn([pawn_pos[0], pawn_pos[1]], [pawn_pos[0]+move[0]*2, pawn_pos[1]], "♟", func_colour))
                    if tile_list[pawn_pos[0]+move[0]][pawn_pos[1]+move[1]]["fg"] == opposing_colour and move in [[-1, 1], [-1, -1], [1, 1], [1, -1]]:
                        tile_list[pawn_pos[0] + move[0]][pawn_pos[1] + move[1]].configure(bg="blue", command=lambda pos_y=pawn_pos[0], pos_x=pawn_pos[1], move_y=move[0], move_x=move[1]: move_pawn( [pos_y, pos_x], [pos_y + move_y, pos_x + move_x], "♟", func_colour))
        if pawn_type == "knight" or pawn_type == "king":
            movement = []
            icon = ""
            if pawn_type == "knight":
                movement = [[-2, -1], [-2, 1], [2, 1], [2, -1], [-1, -2], [1, -2], [1, 2], [-1, 2]]
                icon = "♞"
            if pawn_type == "king":
                movement = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
                icon = "♚"
            for move in movement:
                if 0 <= pawn_pos[0]+move[0] < 8 and 0 <= pawn_pos[1]+move[1] < 8:
                    if tile_list[pawn_pos[0]+move[0]+0][pawn_pos[1]+move[1]+0]["fg"] != func_colour:
                        tile_list[pawn_pos[0]+move[0]][pawn_pos[1]+move[1]].configure(bg="blue", command=lambda pos_y = pawn_pos[0], pos_x = pawn_pos[1], move_y = move[0], move_x = move[1]: move_pawn([pos_y, pos_x], [pos_y+move_y, pos_x+move_x], icon, func_colour))
                        row = 0
                        if not wking_move and pawn_colour == "#c2c2c2":
                            row = [7, 1]
                            if tile_list[row[0]][5]["text"] == "" and tile_list[row[0]][6]["text"] == "":
                                tile_list[row[0]][6].configure(bg="blue",
                                                               command=lambda: move_pawn([row[0], 4], [row[0], 6], icon,
                                                                                         func_colour))
                                castles[row[1]][1] = True
                            if tile_list[row[0]][3]["text"] == "" and tile_list[row[0]][2]["text"] == "" and \
                                    tile_list[row[0]][1]["text"] == "":
                                tile_list[row[0]][2].configure(bg="blue",
                                                               command=lambda: move_pawn([row[0], 4], [row[0], 2], icon,
                                                                                         func_colour))
                                castles[row[1]][0] = True
                        if not bking_move and pawn_colour == "#000000":
                            row = [0, 0]
                            if tile_list[row[0]][5]["text"] == "" and tile_list[row[0]][6]["text"] == "":
                                tile_list[row[0]][6].configure(bg="blue",
                                                               command=lambda: move_pawn([row[0], 4], [row[0], 6], icon,
                                                                                         func_colour))
                                castles[row[1]][1] = True
                            if tile_list[row[0]][3]["text"] == "" and tile_list[row[0]][2]["text"] == "" and \
                                    tile_list[row[0]][1]["text"] == "":
                                tile_list[row[0]][2].configure(bg="blue",
                                                               command=lambda: move_pawn([row[0], 4], [row[0], 2], icon,
                                                                                         func_colour))
                                castles[row[1]][0] = True

        if pawn_type == "bishop" or pawn_type == "rook" or pawn_type == "queen":
            movement = []
            icon = ""
            if pawn_type == "bishop":
                movement = [[1, 1], [-1, -1], [-1, 1], [1, -1]]
                icon = "♝"
            if pawn_type == "rook":
                movement = [[0, 1], [0, -1], [-1, 0], [1, 0]]
                icon = "♜"
            if pawn_type == "queen":
                movement = [[1, 1], [-1, -1], [-1, 1], [1, -1], [0, 1], [0, -1], [-1, 0], [1, 0]]
                icon = "♛"
            for move in movement:
                for n in range(1, 8):
                    if 0 <= pawn_pos[0]+move[0]*n < 8 and 0 <= pawn_pos[1]+move[1]*n < 8:
                        if tile_list[pawn_pos[0]+move[0]*n][pawn_pos[1]+move[1]*n]["fg"] == opposing_colour:
                            tile_list[pawn_pos[0] + move[0] * n][pawn_pos[1] + move[1] * n].configure(bg="blue", command=lambda m=n, pos_y=pawn_pos[0], pos_x=pawn_pos[1], move_y=move[0], move_x=move[1]: move_pawn([pos_y, pos_x],[pos_y + move_y * m, pos_x + move_x * m], icon, func_colour))
                            break
                        elif tile_list[pawn_pos[0]+move[0]*n][pawn_pos[1]+move[1]*n]["fg"] != func_colour:
                            tile_list[pawn_pos[0]+move[0]*n][pawn_pos[1]+move[1]*n].configure(bg="blue", command=lambda m=n, pos_y = pawn_pos[0], pos_x = pawn_pos[1], move_y = move[0], move_x = move[1]: move_pawn([pos_y, pos_x], [pos_y+move_y*m, pos_x+move_x*m], icon, func_colour))
                        else:
                            break
def move_pawn(old_pos, new_pos, pawn, colour):
    global current_turn, end_game, wking_check, bking_check, wking_move, bking_move, castles
    wking_check = False
    bking_check = False
    white_king_pos = []
    black_king_pos = []
    # pawn movement
    def pawn_notation():
        global bking_move, wking_move
        pawn_letter = ""
        row_to_letter = ["a", "b", "c", "d", "e", "f", "g", "h"]
        if pawn == "♟":
            pawn_letter = ""
        if pawn == "♞":
            pawn_letter = "N"
        if pawn == "♝":
            pawn_letter = "B"
        if pawn == "♜":
            pawn_letter = "R"
        if pawn == "♛":
            pawn_letter = "Q"
        if pawn == "♚":
            if castles[1][1] or castles[0][1]:
                if colour == "#c2c2c2":
                    white_text.append(f"0-0")
                if colour == "#000000":
                    black_text.append(f"0-0")
            if castles[1][0] or castles[0][0]:
                if colour == "#c2c2c2":
                    white_text.append(f"0-0-0")
                if colour == "#000000":
                    black_text.append(f"0-0-0")
            else:
                pawn_letter = "K"
                if colour == "#c2c2c2":
                    wking_move = True
                if colour == "#000000":
                    bking_move = True
        if not castles[0][0] and not castles[1][0] and not castles[1][1] and not castles[0][1]:
            if tile_list[new_pos[0]+0][new_pos[1]+0]["text"] == "":
                if colour == "#c2c2c2":
                    white_text.append(f"{pawn_letter}{row_to_letter[new_pos[1]]}{new_pos[0]}")
                if colour == "#000000":
                    black_text.append(f"{pawn_letter}{row_to_letter[new_pos[1]]}{new_pos[0]}")
            else:
                if colour == "#c2c2c2":
                    white_text.append(f"{pawn_letter}{row_to_letter[old_pos[1]]}x{row_to_letter[new_pos[1]]}{new_pos[0]+1}")
                if colour == "#000000":
                    black_text.append(f"{pawn_letter}{row_to_letter[old_pos[1]]}x{row_to_letter[new_pos[1]]}{new_pos[0]+1}")
        wdis = "W:"
        bdis = "B:"
        for n in white_text:
            wdis += f"{n}\n"
            move_label_white.configure(text=wdis)
        for n in black_text:
            bdis += f"{n}\n"
            move_label_black.configure(text=bdis)
    pawn_notation()
    #update board
    check_kings = [0, 0]
    tile_list[old_pos[0]][old_pos[1]].configure(text="", bg=colour_list[old_pos[1]][old_pos[0]])
    tile_list[new_pos[0]][new_pos[1]].configure(text=pawn, bg=colour_list[new_pos[1]][new_pos[0]], fg=colour)
    #check for castle
    if castles[1][1] and wking_move:
        tile_list[7][7].configure(text="", bg=colour_list[7][7], command="")
        tile_list[7][5].configure(text="♜", bg=colour_list[7][5], fg="#c2c2c2")
        castles[1][1] = False
    if castles[1][0] and wking_move:
        tile_list[7][0].configure(text="", bg=colour_list[7][7], command="")
        tile_list[7][3].configure(text="♜", bg=colour_list[7][5], fg="#c2c2c2")
        castles[1][0] = False
    if castles[0][1] and bking_move:
        tile_list[0][7].configure(text="", bg=colour_list[7][7], command="")
        tile_list[0][5].configure(text="♜", bg=colour_list[7][5], fg="#000000")
        castles[0][1] = False
    if castles[0][0] and bking_move:
        tile_list[0][0].configure(text="", bg=colour_list[7][7], command="")
        tile_list[0][3].configure(text="♜", bg=colour_list[7][5], fg="#000000")
        castles[0][0] = False
    #is king in check
    for tile_y in range(8):
        for tile_x in range(8):
            if tile_list[tile_y][tile_x]["text"] == "♚" and tile_list[tile_y][tile_x]["fg"] == "#c2c2c2":
                white_king_pos = [tile_y, tile_x]
            if tile_list[tile_y][tile_x]["text"] == "♚" and tile_list[tile_y][tile_x]["fg"] == "#000000":
                black_king_pos = [tile_y, tile_x]
    pawn_functions()
    check_for_check(white_king_pos, "#c2c2c2")
    check_for_check(black_king_pos, "#000000")
    #displays turn + check
    if colour == "#c2c2c2":
        if bking_check:
            tile_list[new_pos[0]][new_pos[1]].configure(text="", bg=colour_list[old_pos[1]][old_pos[0]])
            tile_list[old_pos[0]][old_pos[1]].configure(text=pawn, bg=colour_list[new_pos[1]][new_pos[0]], fg=colour)
            pawn_functions()
            white_text.pop()
        else:
            current_turn = "#000000"
    else:
        if wking_check:
            tile_list[new_pos[0]][new_pos[1]].configure(text="", bg=colour_list[old_pos[1]][old_pos[0]])
            tile_list[old_pos[0]][old_pos[1]].configure(text=pawn, bg=colour_list[new_pos[1]][new_pos[0]], fg=colour)
            pawn_functions()
            black_text.pop()
        else:
            current_turn = "#c2c2c2"
    show_turn(check_kings)
#place pawns on the board
def assign_pawns(pawn_pos, knight_pos, bishop_pos, rook_pos, queen_pos, king_pos, colour):
    global tile_list, tile_size
    if colour == "W":
        text_colour = "#c2c2c2"
    else:
        text_colour = "#000000"
    #pawn placement
    for pawn_place in range(8):
        tile_list[pawn_pos[1]][pawn_place].configure(text="♟", fg=text_colour)
    #knight placement
    tile_list[knight_pos[1]][knight_pos[0]].configure(text="♞", fg=text_colour)
    tile_list[knight_pos[1]][knight_pos[0]+5].configure(text="♞", fg=text_colour)
    #bishop placement
    tile_list[bishop_pos[1]][bishop_pos[0]].configure(text="♝", fg=text_colour)
    tile_list[bishop_pos[1]][bishop_pos[0]+3].configure(text="♝", fg=text_colour)
    #rook placement
    tile_list[rook_pos[1]][rook_pos[0]].configure(text="♜", fg=text_colour)
    tile_list[rook_pos[1]][rook_pos[0]+7].configure(text="♜", fg=text_colour)
    #queen and king placement
    tile_list[queen_pos[1]][queen_pos[0]].configure(text="♛", fg=text_colour)
    tile_list[king_pos[1]][king_pos[0]].configure(text="♚", fg=text_colour)
    pawn_functions()
#assigning pawn placements for black and white pieces using the assign_pawn function
assign_pawns([0, 1], [1, 0], [2, 0], [0, 0], [3, 0], [4, 0], "B")
assign_pawns([0, 6], [1, 7], [2, 7], [0, 7], [3, 7], [4, 7], "W")
show_turn([0, 0])
#start the game
chess_window.mainloop()
