import tkinter as tk
from tkinter import ttk
from manager import find_enterprise
from model import Enterprise

LARGEFONT = ("Verdana", 14)

class FindEnterprise(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.configure(bg="LightSteelBlue3")
    label = ttk.Label(self, 
      text="Buscar Empresa", 
      font=LARGEFONT, 
      background="LightSteelBlue3")
    label.pack(pady=5, padx=10)

    lf_container = tk.LabelFrame(self,
      text="Buscador",
      labelanchor="n",
      bg="SlateGray3",
      bd=3,
      relief="groove"
    )
    lf_container.pack(padx=15, pady=(15,0), fill=tk.X, expand=True, anchor="n")

    self.search_entry = ttk.Entry(lf_container, width=30)
    self.search_button = ttk.Button(lf_container, text="Buscar", 
      command=lambda: get_enterprise(self))

    self.search_entry.pack(side=tk.LEFT, padx=(140,0), pady=(5,5), anchor="nw")
    self.search_button.pack(side=tk.LEFT, padx=(5), pady=(5,5), anchor="nw")

    vsb = ttk.Scrollbar(self, orient="vertical")
    hsb = ttk.Scrollbar(self, orient="horizontal")
    columns = ("id", "Nombre", "Direccion", "Email", "Telefono", "Fecha Registro", "Activo")
    
    self.ent_tree = ttk.Treeview(self, columns=columns, show='headings')
    vsb.configure(command=self.ent_tree.yview)
    hsb.configure(command=self.ent_tree.xview)
    self.ent_tree.configure(yscrollcommand=vsb.set)
    self.ent_tree.configure(xscrollcommand=hsb.set)
    vsb.pack(side='right', fill='y', padx=(0,15), pady=(0,10))
    hsb.pack(side='bottom', fill='x', padx=(15,0), pady=(0,10))

    for col in columns: self.ent_tree.heading(col, text=col)
    
    self.ent_tree.pack(padx=(15,0), pady=0, expand=True, fill=tk.BOTH)

    def get_enterprise(self):
      self.ent_tree.delete(*self.ent_tree.get_children())

      search_key = self.search_entry.get()
      ent_list = find_enterprise(search_key if search_key else '')

      if ent_list:
        for ent in ent_list:
          self.ent_tree.insert("", tk.END, values=(
            ent.id,
            ent.name,
            ent.address,
            ent.email,
            ent.phone,
            ent.register_date,
            ent.active
          ))
      else:
        message = ('No se encontraron datos.','','','','','','')
        item = self.ent_tree.insert("", tk.END, values=(message))
