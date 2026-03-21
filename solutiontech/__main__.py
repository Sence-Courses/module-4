from views.main_view import TkinterApp
from util import exec_query
from util import EntQuery

from model.client_type import RegularCustomer
from model.client import Client
from model.enterprise import Enterprise
from datetime import datetime, timedelta

if __name__ == "__main__":
  #exec_query(EntQuery.create)

  ent1 = Enterprise(
    id='MyId123',
    name='MyName',
    address='MyAddress',
    email='MyEmail',
    phone='MyPhone',
    register_date=datetime.today() - timedelta(days=1),
    is_active=True
  )
  print(ent1)

  ent2 = Enterprise(
    name='MyName',
    address='MyAddress',
    email='MyEmail',
    phone='MyPhone'
  )
  #print(ent2)
  
  r_cust = RegularCustomer(
    enterprise=ent1,
    points=15
  )
  print(r_cust)
  
  #app = TkinterApp()
  #app.mainloop()
  
