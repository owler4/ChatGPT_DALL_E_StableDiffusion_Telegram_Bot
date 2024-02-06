import psycopg2
import os
from dotenv import load_dotenv

def is_user(user_id):
    load_dotenv()
    db_connection = psycopg2.connect(os.getenv("DATABASE_URL"), sslmode="require")
    db_object = db_connection.cursor()
    db_object.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
    result = db_object.fetchone()
    db_object.close()
    db_connection.close()
    return result

def insert_user(user_id, username):
    load_dotenv()
    db_connection = psycopg2.connect(os.getenv("DATABASE_URL"), sslmode="require")
    db_object = db_connection.cursor()
    db_object.execute("INSERT INTO users(user_id, username, chatgpt, dall_e, stable_diffusion) VALUES (%s, %s, %s, %s, %s)",(user_id, username, 3000, 3, 3))
    db_connection.commit()
    db_object.close()
    db_connection.close()
    return

def get_chatgpt(user_id):
    load_dotenv()
    db_connection = psycopg2.connect(os.getenv("DATABASE_URL"), sslmode="require")
    db_object = db_connection.cursor()
    db_object.execute(f"SELECT chatgpt FROM users WHERE user_id = '{user_id}'")
    result = int(db_object.fetchone()[0])
    db_object.close()
    db_connection.close()
    return result

def set_chatgpt(user_id, result):
    load_dotenv()
    db_connection = psycopg2.connect(os.getenv("DATABASE_URL"), sslmode="require")
    db_object = db_connection.cursor()
    db_object.execute(f"UPDATE users SET chatgpt = {result} WHERE user_id = '{user_id}'")
    db_connection.commit()
    db_object.close()
    db_connection.close()
    return result

def get_dalle(user_id):
    load_dotenv()
    db_connection = psycopg2.connect(os.getenv("DATABASE_URL"), sslmode="require")
    db_object = db_connection.cursor()
    db_object.execute(f"SELECT dall_e FROM users WHERE user_id = '{user_id}'")
    result = int(db_object.fetchone()[0])
    db_object.close()
    db_connection.close()
    return result

def set_dalle(user_id, result):
    load_dotenv()
    db_connection = psycopg2.connect(os.getenv("DATABASE_URL"), sslmode="require")
    db_object = db_connection.cursor()
    db_object.execute(f"UPDATE users SET dall_e = {result} WHERE user_id = '{user_id}'")
    db_connection.commit()
    db_object.close()
    db_connection.close()
    return result

def get_stable(user_id):
    load_dotenv()
    db_connection = psycopg2.connect(os.getenv("DATABASE_URL"), sslmode="require")
    db_object = db_connection.cursor()
    db_object.execute(f"SELECT stable_diffusion FROM users WHERE user_id = '{user_id}'")
    result = int(db_object.fetchone()[0])
    db_object.close()
    db_connection.close()
    return result

def set_stable(user_id, result):
    load_dotenv()
    db_connection = psycopg2.connect(os.getenv("DATABASE_URL"), sslmode="require")
    db_object = db_connection.cursor()
    db_object.execute(f"UPDATE users SET stable_diffusion = {result} WHERE user_id = '{user_id}'")
    db_connection.commit()
    db_object.close()
    db_connection.close()
    return result

def get_userinfo(user_id):
    load_dotenv()
    db_connection = psycopg2.connect(os.getenv("DATABASE_URL"), sslmode="require")
    db_object = db_connection.cursor()
    db_object.execute(f"SELECT * FROM users WHERE user_id = '{user_id}'")
    result = db_object.fetchone()
    db_object.close()
    db_connection.close()
    return result

def new_order(invoice_id, user_id, product):
    load_dotenv()
    db_connection = psycopg2.connect(os.getenv("DATABASE_URL"), sslmode="require")
    db_object = db_connection.cursor()
    db_object.execute("INSERT INTO orders(invoice_id, user_id, product) VALUES (%s, %s, %s)", (invoice_id, user_id, product))
    db_connection.commit()
    db_object.close()
    db_connection.close()
    return

def get_orderdata(invoice_id):
    load_dotenv()
    db_connection = psycopg2.connect(os.getenv("DATABASE_URL"), sslmode="require")
    db_object = db_connection.cursor()
    db_object.execute(f"SELECT user_id, product FROM orders WHERE invoice_id = {invoice_id}")
    result = db_object.fetchone()
    db_object.close()
    db_connection.close()
    return result

def update_chatgpt(user_id, invoice_id):
    load_dotenv()
    db_connection = psycopg2.connect(os.getenv("DATABASE_URL"), sslmode="require")
    db_object = db_connection.cursor()
    db_object.execute(f"UPDATE users SET chatgpt = chatgpt + 100000 WHERE user_id = '{user_id}'")
    db_object.execute(f"DELETE FROM orders WHERE invoice_id = {invoice_id}")
    db_connection.commit()
    db_object.close()
    db_connection.close()
    return

def update_dalle(user_id, invoice_id):
    load_dotenv()
    db_connection = psycopg2.connect(os.getenv("DATABASE_URL"), sslmode="require")
    db_object = db_connection.cursor()
    db_object.execute(f"UPDATE users SET dall_e = dall_e + 100 WHERE user_id = '{user_id}'")
    db_object.execute(f"DELETE FROM orders WHERE invoice_id = {invoice_id}")
    db_connection.commit()
    db_object.close()
    db_connection.close()
    return

def update_stable(user_id, invoice_id):
    load_dotenv()
    db_connection = psycopg2.connect(os.getenv("DATABASE_URL"), sslmode="require")
    db_object = db_connection.cursor()
    db_object.execute(f"UPDATE users SET stable_diffusion = stable_diffusion + 100 WHERE user_id = '{user_id}'")
    db_object.execute(f"DELETE FROM orders WHERE invoice_id = {invoice_id}")
    db_connection.commit()
    db_object.close()
    db_connection.close()
    return