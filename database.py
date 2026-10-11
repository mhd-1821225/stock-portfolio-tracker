#this is the place where we will store all the database related functions 
import stock_api
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
import os
from dotenv import load_dotenv

load_dotenv()

def create_user(username, password, name):

    db = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"))
    cursor = db.cursor()
    hashed_password = generate_password_hash(password)
    
    
   
    sql = "INSERT INTO USERS Values('{}','{}','{}')".format(username,hashed_password,name)
    
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
        

def validate_user(username, password):
    db = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"))
    
    cursor = db.cursor()

    

    sql = "select password from users where username = '{}'".format(username)

    cursor.execute(sql)
    result = cursor.fetchone()
    if result is None:
       
        return "USER_NOT_FOUND"
       
        
    
    
    elif check_password_hash(result[0], password):
           
            print("Login successful!")
            
            sql = "select name from users where username = '{}'".format(username)
            cursor.execute(sql)
            name = cursor.fetchone()[0]
            global username1
            username1 = username
            cursor.close()
            db.close()
            
            
            return name
            

    
    else:
        cursor.close()
        db.close()
            
        return "INVALID_PASSWORD"

def get_name():
     db = mysql.connector.connect(
              host=os.getenv("DB_HOST"),
              user=os.getenv("DB_USER"),
              password=os.getenv("DB_PASSWORD"),
              database=os.getenv("DB_NAME"))
              
     cursor = db.cursor()
     sql = "SELECT name FROM USERS WHERE username = %s"
     cursor.execute(sql, (username1,))
     name = cursor.fetchone()[0]
     cursor.close()
     db.close()
     return name
            


   
def duplicate_user(username):
    db = mysql.connector.connect(
         host=os.getenv("DB_HOST"),
         user=os.getenv("DB_USER"),
         password=os.getenv("DB_PASSWORD"),
         database=os.getenv("DB_NAME"))
         
    cursor = db.cursor()
    sql = "SELECT * FROM USERS WHERE username = %s"
    cursor.execute(sql, (username,))
    if cursor.fetchone():
         cursor.close()
         db.close()
         return "DUPLICATE_USER"
    else:
         cursor.close()
         db.close()
         return "NO_DUPLICATE_USER"


def add_stock(ticker, purchase_price, shares):
    db = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"))
    cursor = db.cursor()
    if duplicate_stock(ticker):
         cursor.close()
         db.close()
         return "DUPLICATE_STOCK"
    else:
         company_name = stock_api.get_name(ticker)
         sql = "INSERT INTO STOCKS (username,ticker,purchase_price,count,company) VALUES('{}','{}',{},{},'{}')".format(username1,ticker,purchase_price,shares,company_name)
         cursor.execute(sql)
         db.commit()
         cursor.close()
         db.close()
         return "STOCK_ADDED_SUCCESSFULLY"

def duplicate_stock(ticker):
    db = mysql.connector.connect(
             host=os.getenv("DB_HOST"),
             user=os.getenv("DB_USER"),
             password=os.getenv("DB_PASSWORD"),
             database=os.getenv("DB_NAME"))
    cursor = db.cursor()
    sql = "SELECT * FROM STOCKS WHERE username = '{}' AND ticker = '{}'".format(username1,ticker)
    cursor.execute(sql)
    if cursor.fetchone():
            cursor.close()
            db.close()
            return True
    else:
            cursor.close()
            db.close()
            return False


def view_portfolio():
    db = mysql.connector.connect(
         host=os.getenv("DB_HOST"),
         user=os.getenv("DB_USER"),
         password=os.getenv("DB_PASSWORD"),
         database=os.getenv("DB_NAME"))
    cursor = db.cursor()
    sql = "SELECT ticker,purchase_price,count,company FROM STOCKS WHERE username = '{}'".format(username1)
    cursor.execute(sql) 
    result = cursor.fetchall()
    total_money_invested = 0
    total_current_value = 0
    total_profit_loss = 0
    
    stack = []
    for row in result:
       
       current_price = stock_api.get_price(row[0])
       
       
       
       profit_loss = (current_price - row[1]) * row[2]
       total_money_invested += row[1] * row[2]
       total_profit_loss += profit_loss
       total_current_value += current_price * row[2]
       status = "🟢" if profit_loss > 0 else "🔴" 
       stack.append([row[0],row[3],row[1],row[2],current_price,round(abs(profit_loss),2),status])
    return stack, round(total_money_invested,2), round(total_current_value,2), round(total_profit_loss,2)


def delete_portfolio():
    db = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"))
    cursor = db.cursor()
    sql = "DELETE FROM STOCKS WHERE username = '{}'".format(username1)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()

    
def delete_stock(ticker):
    db = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"))
    cursor = db.cursor()
    sql = "DELETE FROM STOCKS WHERE ticker = '{}' and username = '{}'".format(ticker,username1)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    return "STOCK_DELETED_SUCCESSFULLY"

def edit_stock(ticker,new_shares,new_purchase_price):
    db = mysql.connector.connect(
         host=os.getenv("DB_HOST"),
         user=os.getenv("DB_USER"),
         password=os.getenv("DB_PASSWORD"),
         database=os.getenv("DB_NAME"))
    cursor = db.cursor()
    

    
    sql = "UPDATE STOCKS SET count = {}, purchase_price = {} WHERE ticker = '{}'".format(new_shares, new_purchase_price, ticker)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    return "STOCK_EDITED_SUCCESSFULLY"

#note the below code is not complete  and needs to be completed in the future please see to it

