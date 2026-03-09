import tkinter as tk
from views import AddEnterprise, FindEnterprise, DeleteEnterprise

def enterprise_menu(self, menubar):
  filemenu = tk.Menu(menubar, tearoff=0, bd=1, relief='flat')
  filemenu.add_command(
    label="Agregar Empresa", 
    command=lambda: self.show_frame(AddEnterprise))
  filemenu.add_command(
    label="Buscar Empresa", 
    command=lambda: self.show_frame(FindEnterprise))
  filemenu.add_command(
    label="Eliminar Empresa", 
    command=lambda: self.show_frame(DeleteEnterprise))
  filemenu.add_separator()
  filemenu.add_command(label="Exit", command=self.quit)
  menubar.add_cascade(label="Empresa", menu=filemenu)

  return menubar
