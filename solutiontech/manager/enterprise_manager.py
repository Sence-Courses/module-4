from model.enterprise import Enterprise
from util import exec_query
from util import EntQuery

def insert_enterprise(e: Enterprise) -> bool: 
  data = (
    e.id, e.name, e.address, e.email, e.phone, e.register_date, e.active
  )
  result = exec_query(EntQuery.insert, data)
  return True if result else False

def delete_enterprise(enterprise_id: str) -> bool:
  result = exec_query(EntQuery.delete, (enterprise_id,))
  return True if result else False

def find_enterprise(search_key: str) -> [Enterprise]:
  row_list = exec_query(EntQuery.select, (search_key,search_key,))
  
  if row_list:
    return list(map(lambda row: row_to_object(row), row_list))
  return row_list

def get_enterprises() -> List[Enterprise]:
  rows = exec_query(EntQuery.select_all)
  return list(map(lambda row: row_to_object(row), rows))

def row_to_object(row) -> Enterprise:
  return Enterprise(
      id=row[0], #enterprise_id
      name=row[1], #name
      address=row[2], #address
      email=row[3], #email
      phone=row[4], #phone
      register_date=row[5], #register_date
      is_active=bool(row[6]) #active
    )
