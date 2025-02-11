import pandas as pd
import psycopg
import os
import streamlit as st
from dotenv import load_dotenv

members = {"SEO": 5, "TOM": 1, "cho": 2, "hyun": 3, "nuni": 10, "JERRY": 4, "jacob": 7, "jiwon": 6, "lucas": 9, "heejin": 8}

load_dotenv()
db_name=os.getenv("DB_NAME")
DB_CONFIG = {
    "user": os.getenv("DB_USERNAME"),
    "dbname" : db_name,
    "password" : os.getenv("DB_PASSWORD"),
    "host" : os.getenv("DB_HOST"),
    "port" : os.getenv("DB_PORT")
}

def get_connection():
    return psycopg.connect(**DB_CONFIG)


def select_df():
    query = """
    SELECT
        l.menu_name,
        m.name,
        l.dt
    FROM 
        lunch_menu l  
        inner join member m
        on l.member_id = m.id
    """

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    #conn.commit()
    cursor.close()
    conn.close()

    #selected_df = pd.DateFrame([[1,2,3]],[4,5,6], columns=[['a','b','c'])
    selected_df = pd.DataFrame(rows, columns=['menu_name', 'ename', 'dt'])
    return selected_df

def insert_menu(menu_name, member_id, dt):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
           " INSERT INTO lunch_menu(menu_name, member_id, dt) VALUES (%s, %s, %s);",
            (menu_name, member_id, dt)
            )
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        print(f"Exception:{e}")
        return False
    
def rank_menu():
    conn = get_connection()

    query = """
            SELECT menu_name, COUNT(*) AS order_count
            FROM lunch_menu
            GROUP BY menu_name
            ORDER BY order_count DESC
            limit 5;
            """
    df = pd.read_sql(query, conn)
    conn.close()
    return df