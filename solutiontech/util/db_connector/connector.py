import sqlite3
from pathlib import Path
from util.logger.logger import debug_logger, error_logger

DDBB_PATH = f'{Path(__file__).parent}/../../data/solutiontech.db'

def exec_query(query, datalist = ()):
  try:
    with sqlite3.connect(DDBB_PATH) as conn:
      conn.row_factory = sqlite3.Row
      cursor = conn.cursor()
      debug_logger.debug(f'Executing query: {query} with data: {datalist}')
      return cursor.execute(query, datalist)
  except sqlite3.Error as e:
    error_logger.error(f'An SQLite error occurred: {e}')
  finally:
    if conn:
      conn.close()
