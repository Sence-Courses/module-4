import tkinter as tk
from views.view_setup import setup_frames
from views import enterprise_menu

class TkinterApp(tk.Tk):
  def __init__(self, *args, **kwargs):
    tk.Tk.__init__(self, *args, **kwargs)
    self.title("SolutionTech App")
    self.geometry("640x480")

    # Container creation
    container = tk.Frame(self)
    container.pack(side="top", fill="both", expand=True)
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)

    # Charge frames
    setup_frames(self, container)

    # Create menu Bar
    menubar = tk.Menu(self, background="SlateGray3")
    menubar = enterprise_menu(self, menubar)
    #menubar = menu_secundario(self, menubar)
    self.config(menu=menubar)

  def show_frame(self, cont):
    """ Raises the selected frame to the front """
    frame = self.frames[cont]
    frame.tkraise()
