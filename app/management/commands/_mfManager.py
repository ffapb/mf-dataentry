
import pymssql

class MfManager:
  def __init__(self, host: str=None, port: str=None, user: str=None, password: str=None, db:str=None):
    self.server   = host      #or "localhost"
    self.port     = port        #or "6200"
    self.user     = user     #or "root"
    self.password = password # or ""
    self.db = db 
   
  # get MF names
  # http://pymssql.org/en/stable/pymssql_examples.html
  def __enter__(self):
    self.conn = pymssql.connect(self.server, self.user, self.password, self.db, port=self.port, as_dict=True, charset="latin1")
    return self

  def _execute(self, query:str):
    cursor = self.conn.cursor()
    cursor.execute(query)
    return cursor

  def __exit__(self, exc_type, exc_val, exc):
    self.conn.close()

  def currenciesCount(self):
    cursor = self._execute("""
      SELECT
        count(*) as n
      FROM DEVISE
      
    """)
    res = cursor.fetchall()
    return res[0]['n']

  def currenciesList(self):
    cursor = self._execute("""
      SELECT DEV_COD, DEV_SYM_LGE1
        
      FROM DEVISE
     
    """)
    return cursor
   
  def nationalitiesCount(self):
    cursor = self._execute("""
      SELECT
        count(*) as n
      FROM NATIONALITE
      
    """)
    res = cursor.fetchall()
    return res[0]['n']

  def nationalitiesList(self):
    cursor = self._execute("""
      SELECT NAT_COD, NAT_LIB_LGE1
        
      FROM NATIONALITE
     
    """)
    return cursor
  
  
