import tkinter as tk

#create windows and global variables
chess_window = tk.Tk()
chess_window.title("Chess")
chess_window.configure(background="white")
chess_window.geometry("640x640")
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
def view_pawn(pawn_type, pawn_pos, pawn_colour):
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
                movement = -1
            else:
                movement = 1
            if 0 <= pawn_pos[0]-1 < 8:
                if tile_list[pawn_pos[0]+movement][pawn_pos[1]+0]["text"] == "":
                    tile_list[pawn_pos[0]+movement][pawn_pos[1]].configure(bg="blue", command=lambda: move_pawn([pawn_pos[0], pawn_pos[1]], [pawn_pos[0]+movement, pawn_pos[1]], "♟", func_colour))
                    if 0 <= pawn_pos[0]-1 < 8 and (pawn_pos[0] == 6 or pawn_pos[0] == 1):
                        tile_list[pawn_pos[0]+movement*2][pawn_pos[1]].configure(bg="blue", command=lambda: move_pawn([pawn_pos[0], pawn_pos[1]], [pawn_pos[0]+movement*2, pawn_pos[1]], "♟", func_colour))
        if pawn_type == "knight":
            movement = [[-2, -1], [-2, 1], [2, 1], [2, -1], [-1, -2], [1, -2], [1, 2], [-1, 2]]
            for move in movement:
                if 0 <= pawn_pos[0]+move[0] < 8 and 0 <= pawn_pos[1]+move[1] < 8:
                    if tile_list[pawn_pos[0]+move[0]][pawn_pos[1]+move[1]]["fg"] != func_colour:
                        tile_list[pawn_pos[0]+move[0]][pawn_pos[1]+move[1]].configure(bg="blue", command=lambda pos_y = pawn_pos[0], pos_x = pawn_pos[1], move_y = move[0], move_x = move[1]: move_pawn([pos_y, pos_x], [pos_y+move_y, pos_x+move_x], "♞", func_colour))
        if pawn_type == "bishop":
            movement = [[1, 1], [-1, -1], [-1, 1], [1, -1]]
            for move in movement:
                for n in range(1, 8):
                    if 0 <= pawn_pos[0]+move[0]*n < 8 and 0 <= pawn_pos[1]+move[1]*n < 8:
                        if tile_list[pawn_pos[0]+move[0]*n][pawn_pos[1]+move[1]*n]["fg"] == opposing_colour:
                            tile_list[pawn_pos[0] + move[0] * n][pawn_pos[1] + move[1] * n].configure(bg="blue", command=lambda m=n, pos_y=pawn_pos[0], pos_x=pawn_pos[1], move_y=move[0], move_x=move[1]: move_pawn([pos_y, pos_x],[pos_y + move_y * m, pos_x + move_x * m],"♝", func_colour))
                            break
                        elif tile_list[pawn_pos[0]+move[0]*n][pawn_pos[1]+move[1]*n]["fg"] != func_colour:
                            tile_list[pawn_pos[0]+move[0]*n][pawn_pos[1]+move[1]*n].configure(bg="blue", command=lambda m=n, pos_y = pawn_pos[0], pos_x = pawn_pos[1], move_y = move[0], move_x = move[1]: move_pawn([pos_y, pos_x], [pos_y+move_y*m, pos_x+move_x*m], "♝", func_colour))
                        else:
                            break
        if pawn_type == "rook":
            movement = [[0, 1], [0, -1], [-1, 0], [1, 0]]
            for move in movement:
                for n in range(1, 8):
                    if 0 <= pawn_pos[0]+move[0]*n < 8 and 0 <= pawn_pos[1]+move[1]*n < 8:
                        if tile_list[pawn_pos[0] + move[0] * n][pawn_pos[1] + move[1] * n]["fg"] == opposing_colour:
                            tile_list[pawn_pos[0] + move[0] * n][pawn_pos[1] + move[1] * n].configure(bg="blue", command=lambda m=n, pos_y= pawn_pos[0], pos_x= pawn_pos[1], move_y= move[0], move_x= move[1]: move_pawn([pos_y, pos_x],[pos_y + move_y * m, pos_x + move_x * m],"♜", func_colour))
                            break
                        elif tile_list[pawn_pos[0] + move[0] * n][pawn_pos[1] + move[1] * n]["fg"] != func_colour:
                            tile_list[pawn_pos[0] + move[0] * n][pawn_pos[1] + move[1] * n].configure(bg="blue", command=lambda m=n, pos_y= pawn_pos[0], pos_x= pawn_pos[1], move_y= move[0], move_x= move[1]: move_pawn([pos_y, pos_x],[pos_y + move_y * m, pos_x + move_x * m],"♜", func_colour))
                        else:
                            break
        if pawn_type == "queen":
            movement = [[1, 1], [-1, -1], [-1, 1], [1, -1], [0, 1], [0, -1], [-1, 0], [1, 0]]
            for move in movement:
                for n in range(1, 8):
                    if 0 <= pawn_pos[0]+move[0]*n < 8 and 0 <= pawn_pos[1]+move[1]*n < 8:
                        if tile_list[pawn_pos[0] + move[0] * n][pawn_pos[1] + move[1] * n]["fg"] == opposing_colour:
                            tile_list[pawn_pos[0] + move[0] * n][pawn_pos[1] + move[1] * n].configure(bg="blue", command=lambda m=n,pos_y=pawn_pos[0], pos_x=pawn_pos[1], move_y=move[0], move_x=move[1]: move_pawn([pos_y, pos_x],[pos_y + move_y * m, pos_x + move_x * m],"♛", func_colour))
                            break
                        elif tile_list[pawn_pos[0] + move[0] * n][pawn_pos[1] + move[1] * n]["fg"] != func_colour:
                            tile_list[pawn_pos[0] + move[0] * n][pawn_pos[1] + move[1] * n].configure(bg="blue", command=lambda m=n, pos_y=pawn_pos[0], pos_x=pawn_pos[1], move_y=move[0], move_x=move[1]: move_pawn([pos_y, pos_x],[pos_y + move_y * m,pos_x + move_x * m],"♛", func_colour))
                        else:
                            break
        if pawn_type == "king":
            movement = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [0, 1], [-1, 1]]
            for move in movement:
                if 0 <= pawn_pos[0]+move[0] < 8 and 0 <= pawn_pos[1]+move[1] < 8:
                    if tile_list[pawn_pos[0]+move[0]][pawn_pos[1]+move[1]]["fg"] != func_colour:
                        tile_list[pawn_pos[0]+move[0]][pawn_pos[1]+move[1]].configure(bg="blue", command=lambda pos_y = pawn_pos[0], pos_x = pawn_pos[1], move_y = move[0], move_x = move[1]: move_pawn([pos_y, pos_x], [pos_y+move_y, pos_x+move_x], "♚", func_colour))
def move_pawn(old_pos, new_pos, pawn, colour):
    global current_turn, end_game
    #checks for white : black
    check_kings = [0, 0]
    tile_list[old_pos[0]][old_pos[1]].configure(text="", bg=colour_list[old_pos[1]][old_pos[0]])
    tile_list[new_pos[0]][new_pos[1]].configure(text=pawn, bg=colour_list[new_pos[1]][new_pos[0]], fg=colour)
    pawn_functions()
    if colour == "#c2c2c2":
        current_turn = "#000000"
    else:
        current_turn = "#c2c2c2"
    for tile_y in range(8):
        for tile_x in range(8):
            if tile_list[tile_y][tile_x]["text"] == "♚" and tile_list[tile_y][tile_x]["fg"] == "#c2c2c2":
                check_kings[0] += 1
            if tile_list[tile_y][tile_x]["text"] == "♚" and tile_list[tile_y][tile_x]["fg"] == "#000000":
                check_kings[1] += 1
    if check_kings == [1, 0]:
        end_game = True
        game_end("#c2c2c2")
    elif check_kings == [0, 1]:
        end_game = True
        game_end("#000000")
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

#start the game
chess_window.mainloop()