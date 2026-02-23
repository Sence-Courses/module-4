import logging
import logging.handlers
from pathlib import Path

def setup_logger(name, log_filename, level):
  """
  Function to set up a logger an add a handler to it.
  Args:
    name (str): Name for the handler.
    log_filename (str): Full path to the log file.
    level (int): Level of the logger.
  Returns:
    Logger: Configured logger.
  """
  logger = logging.getLogger(name)
  logger.setLevel(level)
    
  handler = logging.handlers.TimedRotatingFileHandler(
    log_filename,
    when="midnight",
    interval=1,
    backupCount=7
  )
  formatter = logging.Formatter('%(asctime)s %(levelname)s: %(name)s: %(message)s')
  handler.setFormatter(formatter)
  logger.addHandler(handler)
    
  return logger

def get_file_path(type) -> str:
  """ Returns the full path to the log file. """
  return f'{Path(__file__).parent}/../../logs/{type}/{type}.log'

app_logger = setup_logger('app_logger', get_file_path('info'), level=logging.INFO)
debug_logger = setup_logger('deb_logger', get_file_path('debug'), level=logging.DEBUG)
error_logger = setup_logger('err_logger', get_file_path('error'), level=logging.ERROR)
