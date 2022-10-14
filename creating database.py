import mysql.connector as ms

# creating database
con=ms.connect(host='localhost',user='root',passwd='       ')
cur=con.cursor()
cur.execute('create database if not exists Password_manager')
cur.execute('use Password_manager')
cur.execute('create table if not exists Details (ID int(5) primary key,Username varchar(20),Password varchar(15),Category varchar(20)')

# inserting data
def insert_data():
    uid=int(input('Enter ID:'))
    uname=input('Enter Username:')
    pwd=input('Enter password:')
    cat=input('Enter category:')
    cur.execute('insert into Details values (uid,uname,pwd,cat)')

def delete_rec():
    uid=int(input('Enter ID of account whose details are to be deleted:'))
    cur.execute('delete from Details where ID=uid')

