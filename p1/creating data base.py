import mysql.connector as sq
con=sq.connect(host="localhost",user="root",passwd="root")
cur=con.cursor()

dtb="create database gym"
cur.execute(dtb)
con.commit()
