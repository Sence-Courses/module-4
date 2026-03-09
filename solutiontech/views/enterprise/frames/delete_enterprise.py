import tkinter as tk
from tkinter import ttk
from manager import get_enterprises, delete_enterprise

LARGEFONT = ("Verdana", 14)

class DeleteEnterprise(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.configure(bg="LightSteelBlue3")
    label = ttk.Label(self, 
      text="Eliminar Empresa", 
      font=LARGEFONT, 
      background="LightSteelBlue3")
    label.pack(pady=5, padx=10)

    em_container = tk.LabelFrame(self,
      text="Empresas",
      labelanchor="n",
      bg="SlateGray3",
      bd=3,
      relief="groove"
    )
    em_container.pack(padx=15, pady=15, fill=tk.X, expand=True, anchor="n")

    cl_container = tk.LabelFrame(self,
      text="Clientes",
      labelanchor="n",
      bg="SlateGray3",
      bd=3,
      relief="groove"
    )
    cl_container.pack(padx=15, pady=15, fill="both", expand=True, anchor="n")

    ent_opts = enterprise_opts()
    combo_opts = list(ent_opts.keys())
    self.selected_id = None

    self.combo = ttk.Combobox(em_container, width=30, values=combo_opts, state="readonly")
    self.combo.current(0)
    self.combo.bind('<<ComboboxSelected>>', self.set_enterprise_id)
    self.delete_button = ttk.Button(em_container, text="Eliminar", 
      command=lambda: del_enterprise(self))

    self.combo.pack(side=tk.LEFT, padx=(140,0), pady=(5,5), anchor="nw")
    self.delete_button.pack(side=tk.LEFT, padx=(5), pady=(5,5), anchor="nw")

    def del_enterprise(self):
      print(self.selected_id)
      if self.selected_id:
        delete_enterprise(self.selected_id)
        ent_opts = enterprise_opts()
        self.combo['values'] = list(ent_opts.keys())
        self.combo.current(0)

  def set_enterprise_id(self, event):
    ent_opts = enterprise_opts()
    self.selected_id = ent_opts.get(event.widget.get())

def enterprise_opts():
  ent_list = get_enterprises()
  ent_dict = {'Seleccione una empresa..': None}

  if ent_list:
    for e in ent_list:
      ent_dict[e.name]=e.id
  else:
    pass
  return ent_dict