import tkinter as tk
from tkinter import ttk
from views import AddEnterprise, FindEnterprise, DeleteEnterprise

LARGEFONT = ("Verdana", 14)

def setup_frames(self, container):
  self.frames = {}

  for F in (
      StartPage, 
      AddEnterprise, FindEnterprise, DeleteEnterprise):
    frame = F(container, self)
    self.frames[F] = frame
    frame.grid(row=0, column=0, sticky="nsew") # Stack all frames in the same grid position

  self.show_frame(StartPage) # Show the initial frame

class StartPage(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    label = ttk.Label(self, text="Start Page", font=LARGEFONT)
    label.pack(pady=10, padx=10)
    button = ttk.Button(self, 
      text="Go to Add",
      command=lambda: controller.show_frame(AddEnterprise))
    button.pack()
    button2 = ttk.Button(self, 
      text="Go to Find", 
      command=lambda: controller.show_frame(FindEnterprise))
    button2.pack()
