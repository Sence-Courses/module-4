from model.enterprise import Enterprise
from util.db_connector.connector import exec_query
from util.db_connector.queries import EntQuery

def insert_enterprise(e: Enterprise) -> bool: 
  data = (
    e.id, e.name, e.address, e.email, e.phone, e.register_date, e.active
  )
  result = exec_query(EntQuery.insert, data)
  return True if result else False

def delete_enterprise(enterprise_id: str) -> bool:
  result = exec_query(EntQuery.delete, (enterprise_id,))
  return True if result else False

def find_enterprise(enterprise_id: str) -> Enterprise:
  row = exec_query(EntQuery.select, (enterprise_id,))
  return row_to_object(row)

def get_enterprises() -> List[Enterprise]:
  rows = exec_query(EntQuery.select_all)
  return list(map(lambda row: row_to_object(row), rows))

def row_to_object(row) -> Enterprise:
  return Enterprise(
      id=row['enterprise_id'],
      name=row['name'],
      address=row['address'],
      email=row['email'],
      phone=row['phone'],
      register_date=row['register_date'],
      is_active=bool(row['active'])
    )
