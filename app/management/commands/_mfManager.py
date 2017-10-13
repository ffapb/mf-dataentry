import pymssql
from .titre import TITRE
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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

  def subtypeCount(self):
    cursor = self._execute("""
      SELECT
        count(*) as o
      FROM SOUSTYPETITRE 
  
    """)
       
    res = cursor.fetchall()
    return res[0]['o']

  def subtypeList(self):
    cursor = self._execute("""
      SELECT STY_COD, STY_LIB_LGE1
                                
      FROM SOUSTYPETITRE
                   
    """)
    return cursor

  def rateproviderCount(self):
    cursor = self._execute("""
      SELECT
      count(*) as r
      FROM RateList                    
    """)

    res = cursor.fetchall()
    return res[0]['r']

  def rateproviderList(self):
    cursor = self._execute("""
     SELECT RTL_COD, RTL_LIB_LGE1
     FROM RateList
                                                  
   """)
    return cursor

  def assetallocationCount(self):
    cursor = self._execute("""
      SELECT
      count(*) as a
      FROM Titre_AssetAllocation                    
   """)

    res = cursor.fetchall()
    return res[0]['a']

  def assetallocationList(self):
    cursor = self._execute("""
       SELECT Asset_Cod, Asset_Desc1
       FROM Titre_AssetAllocation
                                                                                
    """)
    return cursor


  def categoryCount(self):
    cursor = self._execute("""
       SELECT
       count(*) as c
       FROM Titre_Category
                                                              
    """)
    res = cursor.fetchall()
    return res[0]['c']

  def categoryList(self):
    cursor = self._execute("""
       SELECT Tit_Category_Cod, Tit_Cat_Desc1
                                      
       FROM Titre_Category
                                                                                                         
   """)
    return cursor


  def tradingcategoryCount(self):
    cursor = self._execute("""
       SELECT
       count(*) as tc
       FROM Trading_Category
                                                                  
     """)
    res = cursor.fetchall()
    return res[0]['tc']

  def tradingcategoryList(self):
    cursor = self._execute("""
       SELECT Trad_Cat_Code, Trad_Cat_Desc1
                                                   
       FROM Trading_Category
                                                                                                                                                                                 
    """)
    return cursor

  def quotationplaceCount(self):
      cursor = self._execute("""
          SELECT
          count(*) as qp
          FROM PLACECOTATION
                                                                                         
       """)
      res = cursor.fetchall()
      return res[0]['qp']

  def quotationplaceList(self):
      cursor = self._execute("""
         SELECT PCE_COD, PCE_LIB_LGE1
                                                                 
         FROM PLACECOTATION
                                                                                                                                                                                 
      """)
      return cursor

  def tradingcenterCount(self):
      cursor = self._execute("""
         SELECT
         count(*) as tce
         FROM MARCHE
                                                                                                                               
      """)
      res = cursor.fetchall()
      return res[0]['tce']

  def tradingcenterList(self):
      cursor = self._execute("""
         SELECT MAR_COD, MAR_LIB_LGE1
                                                                                                      
         FROM MARCHE                                                                                                                                                                                                                                                                                                                                                                                                          """)
      return cursor
                        



  def titreSeqMax(self):
    cursor = self._execute("""
      Select max(tit_seq) as m
      from titre
      where len(tit_seq)=6 and cast(tit_seq as int) = tit_seq
""")
    res = cursor.fetchall()
    return res[0]['m']


  def natureCount(self):
      cursor = self._execute("""
        SELECT
        count(*) as n
        FROM NATURETITRE
                                
      """)
      res = cursor.fetchall()
      return res[0]['n']

  def natureList(self):
      cursor = self._execute("""
        SELECT NAT_TIT_COD, NAT_TIT_LIB_LGE1
                  
        FROM NATURETITRE
                                             
     """)
      return cursor


#  def depositplaceCount(self):
#      cursor = self._execute("""
#        SELECT
#        count(*) as dp
#        FROM CLIENT_ENTITY
#       
#        where CLIENT_ENTITY.ENT_TYPE='4'
#                                                                   
#     """)
#      res = cursor.fetchall()
#      return res[0]['dp']
#
#  def depositplaceList(self):
#      cursor = self._execute("""
#        SELECT  ENT_COD,ENT_FULL_NAME
#                                                         
#        FROM CLIENT_ENTITY
#               
#        where CLIENT_ENTITY.ENT_TYPE='4'
#                                                                                                                      
#      """)
#      return cursor


  def getCodeLebDub(self, x, origin):
    return x.code_leb if origin=="MF Lebanon" else x.code_dub
 
  def insertSecurity(self, sec, origin):
    url = 'mssql+pymssql://'+self.user+':'+self.password+'@'+self.server+':'+str(self.port)+'/'+self.db
    engine = create_engine(url)
     
    session = sessionmaker()
    session.configure(bind=engine)

    s = session()

    # check if security already exists
    found = s.query(TITRE).filter(TITRE.TIT_COD==sec.code)
    if found.count()>0:
      if found.count()>1:
        raise Exception("Found %s rows for code %s"%(found.count(),sec.code))
      t1 = found.one() # will raise error if more than one found
    else:
      t1 = TITRE(TIT_COD=sec.code)

      # set defaults required
      t1.TIT_O_MOD_COD = 0
      t1.TIT_CATEG = ""
      t1.TIT_TRADING_CATEG = ""
      t1.TIT_RATE_LIST = 1
      t1.Tit_Asset_Cod = ""
      #t1.TIT_FORWARD = 0
      t1.TIT_TREATED_ONLINE = 0
      #t1.TIT_PIP_VALUE = 0
      #t1.TIT_MONITOR_TYPE = 0
      #t1.TIT_TTG_COD = 0
      #t1.TIT_NB_UNITE = 1
      t1.TIT_LST_COD = 0

      # set increment field that is not "auto" in marketflow database
      m = "%06.0f" % ( int(self.titreSeqMax()) +1 )
      t1.Tit_dep_Ref = m
      t1.TIT_SEQ = m

      # asset-type-specific fields
      t1.TIT_FUTUR = 0
      t1.TIT_OPTIONS = 0
      t1.TIT_BOND = 0
      t1.TIT_STRIKE = 0
      t1.TIT_UNDERLYING = 0
      t1.TIT_DAT_MAT = ""
      t1.TIT_HOLDER = ""
      t1.TIT_SHOW = 0
      t1.TIT_FIRST_NOTICE_DAT = ""
      t1.TIT_NB_UNITE = 1
      t1.TIT_MAR = 0
      t1.TIT_FORWARD = 0
      t1.TIT_PIP_VALUE = 0
      t1.TIT_TTG_COD = 0
      t1.TIT_MONITOR_TYPE = 0
      t1.TIT_OCCUPE = 0

      # some more
      t1.TIT_MAR_LN = 0
      t1.TIT_MAR_SH = 0


    # set fields
    t1.TIT_NOM = sec.designation
    t1.TIT_DEV_COD = self.getCodeLebDub(sec.currency, origin)
    t1.TIT_STY_COD =  self.getCodeLebDub(sec.subtype, origin)
    # wrong? # t1.TIT_CAT_COD = sec.category
    t1.TIT_NAT_COD = self.getCodeLebDub(sec.nationality, origin)
    t1.TIT_PCE_COD = self.getCodeLebDub(sec.quotation_place, origin)
   # t1.TIT_DEP_COD = self.getCodeLebDub(sec.deposit_place, origin)
    t1.TIT_DEP_COD=sec.deposit_place
    #t1.TIT_LST_COD = sec.ratelist
    t1.TIT_FIXING = 1 if sec.fixing else 0
    t1.TIT_FIX_1 = sec.fix1
    t1.TIT_FIX_2 = sec.fix2

    t1.TIT_CHART_ACC = sec.general_ledger
    t1.TIT_REU_COD = sec.provider_code
    t1.TIT_NAT_TIT_COD= self.getCodeLebDub(sec.nature, origin)
    t1.TIT_MAR_COD = self.getCodeLebDub(sec.trading_center, origin)
    t1.TIT_ISIN_COD = sec.isin
    t1.TIT_DESC = sec.symbol
    t1.TIT_CATEG = self.getCodeLebDub(sec.category, origin)
    t1.TIT_TRADING_CATEG = self.getCodeLebDub(sec.trading_category, origin)
    t1.TIT_RATE_LIST = self.getCodeLebDub(sec.provider_ratelist, origin)
    t1.Tit_Asset_Cod = self.getCodeLebDub(sec.asset_allocation, origin)
    t1.TIT_ONLINE_RATE_MULTIPLIER = sec.multiplier_for_online_prices
    t1.TIT_MAR_LN_MC = sec.main_lng_position
    t1.TIT_MAR_SH_MC = sec.main_short_position
    t1.TIT_MAR_LN = sec.mar_lng_position
    t1.TIT_MAR_SH = sec.mar_short_position
    #t1.TIT_MONITOR_TYPE = sec.monitoring_type

    if sec.__class__.__name__=="SecurityShare":
      t1.TIT_TYP_TIT_COD = 1
      t1.TIT_HOLDER = 1 if sec.shareholder_number else 0
      t1.TIT_SHOW = 1 if sec.show else 0
      t1.TIT_DIV_CHART = 4211
      t1.TIT_OCCUPE = -1

    if sec.__class__.__name__=="SecurityOption":
      t1.TIT_OPTIONS = 1 
      t1.TIT_TYP_TIT_COD = 6
      t1.TIT_DAT_MAT = sec.maturity_date.strftime("%Y-%m-%d")
      t1.TIT_UNDERLYING = sec.underlying_code
      t1.TIT_STRIKE = sec.strike_place
      t1.TIT_DIV_CHART = "4211"
      t1.TIT_OCCUPE= '-1'

    if sec.__class__.__name__=="SecurityBond":
     
      t1.TIT_BOND = 1 
      t1.TIT_TYP_TIT_COD = 2
      t1.TIT_CR_RATE1 = sec.moody
      t1.TIT_CR_RATE2 = sec.fitch
      t1.TIT_CR_RATE3 = sec.s_and_p
      t1.TIT_DIV_CHART = 4211

        
    if sec.__class__.__name__=="SecurityFutures":
      t1.TIT_FUTUR = 1
      t1.TIT_TYP_TIT_COD = 5
      t1.TIT_DAT_MAT = sec.maturity_date.strftime("%Y-%m-%d")
      t1.TIT_UNDERLYING = sec.underlying_code
      t1.TIT_NB_UNITE = sec.number_of_units
      t1.TIT_FIRST_NOTICE_DAT = sec.first_notice_date.strftime("%Y-%m-%d")
      t1.TIT_HOLDER = 1 if sec.shareholder_number else 0
      t1.TIT_SHOW = 1 if sec.show else 0
      t1.TIT_OCCUPE= '-1'
      t1.TIT_DIV_CHART = 8904

    # add and commit
    if found.count()==0:
      s.add(t1)

    s.commit()

