# creating database
import mysql.connector as ms
con=ms.connect(host='localhost',user='root',passwd='       ')
cur=con.cursor()
cur.execute('create database if not exists Password_manager')
cur.execute('use Password_manager')
cur.execute('create table if not exists Details (ID int(5),Username varchar(20),Password varchar(15),Category varchar(20)')
