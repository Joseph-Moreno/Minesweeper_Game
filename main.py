from tkinter import *
from tkinter import ttk
from cell import Cell
import settings
import utilities

#window settings
window_instance = Tk()
window_instance.configure(bg="black")
window_instance.geometry(f'{settings.width}x{settings.height}')
window_instance.title("Minesweeper")
window_instance.resizable(False, False)


top_frame = Frame(window_instance,
                  bg= "black" ,
                  width= settings.width ,
                  height=utilities.height_prct(25))
top_frame.place(x=0, y=0)

left_frame=Frame(window_instance,
                 bg="black",
                 width=utilities.width_prct(25),
                 height=utilities.height_prct(75))

left_frame.place(x=0, y=utilities.height_prct(25))

center_frame = Frame(window_instance,
                   bg="black",
                   width=utilities.width_prct(75),
                   height=utilities.height_prct(75))
center_frame.place(x=utilities.width_prct(25), y=utilities.height_prct(25))

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell()
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )



#run window
window_instance.mainloop()


