import mysql.connector as msq
v=msq.connect(host='localhost',user='root',passwd='root',database='gym')
crs=v.cursor()
st='''CREATE TABLE GMAC(
      GAME_ID int  PRIMARY KEY,
      GAME_NAME varchar(20),
      STORAGE varchar (4),
      RAM varchar (2),
      GRAPHIC_REQ varchar(3),
      GENRE varchar (10),
      DATE_OF_LAUNCH DATE)'''
crs.execute(st)
v.close()
