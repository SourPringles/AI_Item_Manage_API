import sqlite3

DB_FILE = "./db/userdata.db"

def init_db():
    """
    데이터베이스 초기화: storage 테이블 생성, temp 테이블 생성
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS storage (
            qr_code TEXT PRIMARY KEY,
            x INTEGER,
            y INTEGER,
            lastChecked TEXT,
            nickname TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS temp (
            qr_code TEXT PRIMARY KEY,
            takeout_time TEXT,
            nickname TEXT
        )
    ''')
    conn.commit()
    conn.close()

def reset_db():
    """
    데이터베이스 초기화: storage 테이블, temp 테이블
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute('DROP TABLE IF EXISTS storage')
    cursor.execute('DROP TABLE IF EXISTS temp')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS storage (
            qr_code TEXT PRIMARY KEY,
            x INTEGER,
            y INTEGER,
            lastChecked TEXT,
            nickname TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS temp (
            qr_code TEXT PRIMARY KEY,
            takeout_time TEXT,
            nickname TEXT
        )
    ''')

    conn.commit()
    conn.close()