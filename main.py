from tkinter import *
from cell import Cell
import settings
import utils

root = Tk()
root.configure(background="dark gray")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('Minesweeper')
root.resizable(False, False)

top_frame = Frame(root, background='dark gray', width=f'{settings.WIDTH}', height=utils.height_prct(20))
top_frame.place(x=0, y=0)


game_title = Label(
    top_frame,
    bg='dark gray',
    fg='White',
    text='Minesweeper Game',
    font=('', 48)
)
game_title.place(
    x=utils.width_prct(25), y=utils.height_prct(0)
)


left_frame = Frame(root, background= 'dark gray', width=utils.width_prct(25), height=utils.height_prct(80))
left_frame.place(x=0, y=utils.height_prct(20))

center_frame = Frame(root, background='gray', width=utils.width_prct(80), height=utils.height_prct(80))
center_frame.place(x=utils.width_prct(25), y=utils.height_prct(20))


for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_button_object.grid(
            column=x,
            row=y)

Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x=0, y=0)
Cell.random_mines()


root.mainloop()
