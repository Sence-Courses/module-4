from enum import Enum

CREATE_ENTERPRISE = """
  CREATE TABLE enterprise(
    enterprise_id VARCHAR(6) PRIMARY KEY,
    name VARCHAR(35) NOT NULL,
    address VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    phone VARCHAR(512) NOT NULL,
    register_date TEXT,
    active INTEGER NOT NULL CHECK (active IN (0, 1))
  );
  """

INSERT_ENTERPRISE = """
  INSERT INTO enterprise
  (enterprise_id, name, address, email, phone, register_date, active)
  VALUES(?,?,?,?,?,?,?);
  """

DELETE_ENTERPRISE = 'DELETE FROM enterprise WHERE enterprise_id = ?'

SELECT_ENTERPRISE = """
  SELECT enterprise_id, name, address, email, phone, register_date, active
  FROM enterprise
  WHERE enterprise_id = ?
  """

SELECT_ALL_ENTERPRISE = """
  SELECT enterprise_id, name, address, email, phone, register_date, active
  FROM enterprise
  ORDER BY name ASC
  """

"""
Coleccion que contiene las queries de la aplicacion.
"""
EntQuery = Enum('EntQuery', [
  ('create', CREATE_ENTERPRISE),
  ('insert', INSERT_ENTERPRISE),
  ('delete', DELETE_ENTERPRISE),
  ('select', SELECT_ENTERPRISE),
  ('select_all', SELECT_ALL_ENTERPRISE)
])
