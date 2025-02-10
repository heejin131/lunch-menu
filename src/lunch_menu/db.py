import pandas as pd
import psycopg
import os
from  dotenv import load_dotenv

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