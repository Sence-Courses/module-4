import tkinter as tk
from tkinter import ttk
from util import VF, EM, validate, app_logger
from model import Enterprise
from manager import insert_enterprise

LARGEFONT = ("Verdana", 14)

class AddEnterprise(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.configure(bg="LightSteelBlue3")
    label = ttk.Label(self, 
      text="Agregar Empresa", 
      font=LARGEFONT, 
      background="LightSteelBlue3")
    label.pack(pady=5, padx=10)

    lf_container = tk.LabelFrame(self,
      text="Informacion de la empresa",
      labelanchor="n",
      bg="SlateGray3",
      bd=3,
      relief="groove"
    )
    lf_container.pack(padx=20, pady=20, fill="both", expand=True)
    #style = ttk.Style()
    #style.configure('My.TEntry', padding=(10, 5, 0, 0))

    name_label = ttk.Label(lf_container, text="Nombre",
      background="SlateGray3", padding=(25, 25, 0, 0))
    name_label.pack(pady=0, anchor="w")
    self.name_entry = ttk.Entry(lf_container, width=35)
    self.name_entry.pack(padx=(25, 0), pady=0, anchor="w")

    address_label = ttk.Label(lf_container, text="Direccion",
      background="SlateGray3", padding=(25, 10, 0, 0))
    address_label.pack(pady=0, anchor="w")
    self.address_entry = ttk.Entry(lf_container, width=35)
    self.address_entry.pack(padx=(25, 0), pady=0, anchor="w")

    # email entry
    email_label = ttk.Label(lf_container, text="Email",
      background="SlateGray3", padding=(25, 10, 0, 0))
    email_label.pack(pady=0, anchor="w")
    self.email_entry = ttk.Entry(lf_container, width=35)
    self.email_entry.config(validate='focusout', 
      validatecommand=(self.register(self.validate_field), '%P', VF.email.name), 
      invalidcommand=(self.register(self.on_invalid), EM.email.name))
    self.email_entry.pack(padx=(25, 0), pady=0, anchor="w")
    self.email_label_error = tk.Label(lf_container, foreground='red')

    # phone entry
    phone_label = ttk.Label(lf_container, text="Telefono",
      background="SlateGray3", padding=(25, 10, 0, 0))
    phone_label.pack(pady=0, anchor="w")
    self.phone_entry = ttk.Entry(lf_container, width=35)
    self.phone_entry.config(validate='focusout', 
      validatecommand=(self.register(self.validate_field), '%P', VF.phone.name), 
      invalidcommand=(self.register(self.on_invalid), EM.phone.name))
    self.phone_entry.pack(padx=(25, 0), pady=0, anchor="w")
    self.phone_label_error = tk.Label(lf_container, foreground='red')

    button = ttk.Button(self, text="Agregar", state="enabled", command=lambda: 
      set_enterprise(
        self.name_entry.get(),
        self.address_entry.get(),
        self.email_entry.get(),
        self.phone_entry.get())
    )
    button.pack(pady=(10, 30))

  def validate_field(self, value, type):
    match (type):
      case VF.email.name:
        if validate(value, type):
          self.show_message(type)
          self.email_label_error.pack_forget()
          return True
        self.email_label_error.pack(padx=(25, 0), pady=(20, 0), anchor="w")
        return False
      case VF.phone.name:
        if validate(value, type):
          self.show_message(type)
          self.phone_label_error.pack_forget()
          return True
        self.phone_label_error.pack(padx=(125, 0), pady=(20, 0), anchor="w")
        return False
      case _:
        pass

  def show_message(self, type, error='', color='black'):
    match (type):
      case EM.email.name:
        self.email_label_error['text'] = error
        self.email_entry['foreground'] = color
      case EM.phone.name:
        self.phone_label_error['text'] = error
        self.phone_entry['foreground'] = color
      case _:
        pass

  def on_invalid(self, type):
    match (type):
      case EM.email.name:
        self.show_message(type, EM.email.value, 'red') 
      case EM.phone.name:
        self.show_message(type, EM.phone.value, 'red')
      case _:
        pass 

def set_enterprise(name: str, address, email, phone):
  emp = Enterprise(
    name=name,
    address=address,
    email=email,
    phone=phone)
  
  if insert_enterprise(emp):
    app_logger.info(f'Empresa creada: {print(emp)}');
  else:
    pass