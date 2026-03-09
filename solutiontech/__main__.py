from views.main_view import TkinterApp
from util import exec_query
from util import EntQuery

if __name__ == "__main__":
  exec_query(EntQuery.create)
  app = TkinterApp()
  app.mainloop()
