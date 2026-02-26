import sqlite3
from pathlib import Path
from util.logger.logger import debug_logger, error_logger

DDBB_PATH = f'{Path(__file__).parent}/../../data/solutiontech.db'

def exec_query(querytype, datalist = ()):
  try:
    with sqlite3.connect(DDBB_PATH, detect_types=sqlite3.PARSE_DECLTYPES) as conn:
      conn.row_factory = sqlite3.Row
      cursor = conn.cursor()
      debug_logger.debug(f'Executing query: {querytype.value} with data: {datalist}')
      result = cursor.execute(querytype.value, datalist)
      
      match (querytype.name):
        case 'insert':
          return [cursor.rowcount, cursor.lastrowid]
        case 'delete':
          return [cursor.rowcount]
        case 'select':
          return cursor.fetchone()
        case 'select_all':
          return cursor.fetchall()
  except sqlite3.Error as e:
    error_logger.error(f'An SQLite error occurred: {e}')
  finally:
    if conn:
      conn.commit()
      conn.close()
