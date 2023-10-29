from tkinter import Button, Label
import random
import settings
import ctypes
import sys
import time


class Cell:
    all = []
    cell_count_label_object = None
    cell_count = settings.CELL_COUNT

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False
        self.is_marked = False
        self.cell_button_object = None
        self.x = x
        self.y = y
        Cell.all.append(self)

    def create_btn_object(self, frame):
        btn = Button(
            frame,
            width=7,
            height=3,
            # text=f'{self.x},{self.y}'
        )
        btn.bind('<Button-1>', self.left_click_actions)
        btn.bind('<Button-3>', self.right_click_actions)
        self.cell_button_object = btn

    @staticmethod
    def create_cell_count_label(frame):
        lbl = Label(
            frame,
            text=f"Cells Left:{Cell.cell_count}",
            width=12,
            height=4,
            bg='dark gray',
            fg='white',
            font=("calibri", 18)
        )
        Cell.cell_count_label_object = lbl

    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length == 0:
                for c in self.surrounded_cells:
                    c.show_cell()
            self.show_cell()
            if Cell.cell_count == settings.NR_MINES:
                ctypes.windll.user32.MessageBoxW(
                    0,
                    'Congratulations! You won the game!',
                    'YOW WON',
                    0
                )
                sys.exit()

    def get_cell_by_axis(self, x, y):
        for c in Cell.all:
            if c.x == x and c.y == y:
                return c

    @property   # read only
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1)
        ]
        cells = [x for x in cells if x is not None]
        return cells

    @property   # read only
    def surrounded_cells_mines_length(self):
        counter = 0
        for x in self.surrounded_cells:
            if x.is_mine:
                counter += 1
        return counter

    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_button_object.configure(
                text=f'{self.surrounded_cells_mines_length}',
                background='SystemButtonFace'
            )
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text=f"Cells Left:{Cell.cell_count}"
                )
        self.is_opened = True

    def show_mine(self):
        # self.cell_button_object.configure(bg='red')
        Cell.cell_count_label_object.configure(
            text=f"###############"
        )
        ctypes.windll.user32.MessageBoxW(
            0,
            'You clicked on a mine',
            'GAME OVER',
            0
        )
        sys.exit()

    def right_click_actions(self, event):
        if not self.is_marked and not self.is_opened:
            self.cell_button_object.configure(bg='orange')
            self.is_marked = True
        else:
            self.cell_button_object.configure(bg='SystemButtonFace')
            self.is_marked = False
        if self.is_opened:
            self.is_marked = False

    @staticmethod
    def random_mines():
        picked_cells = random.sample(
            Cell.all,
            settings.NR_MINES
        )
        print(picked_cells)
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f'Cell({self.x},{self.y})'
