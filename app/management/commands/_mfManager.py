
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
  
  def insertSecurity(self,Security):
 
    self.execute("INSERT INTO TITRE (TIT_COD,TIT_CIR,TIT_NOM,TIT_DEV_COD,TIT_TYP_TIT_COD,TIT_STY_COD,TIT_NAT_TIT_COD,TIT_CAT_COD,TIT_MAR_COD,TIT_NAT_COD,TIT_PCE_COD,TIT_DEP_COD,TIT_LST_COD,TIT_FIXING,TIT_FIX_1,TIT_FIX_2,TIT_FRAIS,TIT_FR1,TIT_FR1_FFA,TIT_FR1_DEP,TIT_FR2,TIT_FR2_FFA,TIT_FR2_DEP,TIT_FR3,TIT_FR3_FFA,TIT_FR3_DEP,TIT_FR4,TIT_FR4_FFA,TIT_FR4_DEP,TIT_FR5,TIT_FR5_FFA,TIT_FR5_DEP,TIT_OCCUPE,TIT_O_MOD_COD,TIT_SHOW,TIT_HOLDER,TIT_OPTIONS,TIT_NB_UNITE,TIT_DAT_MAT,TIT_SEQ,TIT_FR1_FFACPT,TIT_FR1_DEPCPT,TIT_FR2_FFACPT,TIT_FR2_DEPCPT,TIT_FR3_FFACPT,TIT_FR3_DEPCPT,TIT_FR4_FFACPT,TIT_FR4_DEPCPT,TIT_FR5_FFACPT,TIT_FR5_DEPCPT,TIT_CHART_ACC,TIT_REU_COD,TIT_DIV_CHART,TIT_MAR,TIT_MAR_LN,TIT_MAR_SH,TIT_UPD,TIT_STRIKE,TIT_UNDERLYING,TIT_PUT,TIT_CALL,TIT_FUTUR,TIT_DEV_COD2,TIT_ISIN_COD,Tit_dep_Ref,TIT_DEV_COD1,TIT_ISSUER,TIT_DESC,TIT_RATIO,TIT_CATEG,TIT_TRADING_CATEG,TIT_RATE_LIST,Tit_Asset_Cod,TIT_FORWARD,TIT_FWD_SPOT,TIT_TREATED_ONLINE,TIT_FIRST_NOTICE_DAT,TIT_PIP_VALUE,TIT_ONLINE_RATE_MULTIPLIER,TIT_MAR_DEV,TIT_MONITOR_TYPE,TIT_CR_RATE1,TIT_CR_RATE2,TIT_CR_RATE3,TIT_TTG_COD,TIT_MAR_LN_MC,TIT_MAR_SH_MC,TIT_UPD_LOGIN,TIT_UPD_ACTION,TIT_UPD_LAST_DATE,TIT_TICKET_PROVIDER_CODE,TIT_TICKET_PROVIDER_SYMBOL) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)%(Security.code,NULL,Security.designation,Security.currency,NULL,Security.subtype,1,Security.category,4,Security.nationality,Security.qotation_place,Security.deposit_place,Security.ratelist,Security.fixing,Security.fix1,Security.fix2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,Security.show,Security.shareholder_number,0,Security_number_of_unit,Security.maturity_date,Security.bank_reference,0,0,0,0,0,0,0,0,0,0,Security.general_ledger,Security.provider_code,4211,0,100,100,0,Security.strike_place,Security.underlying_code,0,0,0,NULL,Security.isin,Security.bank_reference,NULL,NULL, Security.symbol,0,Security.category,Security.trading_category,Security.provider_ratelist,Security.asset_allocation,0,NULL,0,NULL,0,Security.multiplier_for_online_prices,02,Security.monitoring_type,NULL,NULL,NULL,0,100,100,NULL,NULL,NULL,NULL,NULL)")


    return self
