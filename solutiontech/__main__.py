from util.db_connector.connector import exec_query
from util.db_connector.queries import Query

print(exec_query(Query['example'].value))