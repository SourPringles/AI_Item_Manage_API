import sqlite3

DB_FILE = "./db/userdata.db"

def init_db():
    """
    데이터베이스 초기화: inventory 테이블 생성
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventory (
            qr_code TEXT PRIMARY KEY,
            x INTEGER,
            y INTEGER,
            last_modified TEXT,
            nickname TEXT
        )
    ''')
    conn.commit()
    conn.close()

def load_storage():
    """
    데이터베이스에서 인벤토리 로드
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM inventory')
    rows = cursor.fetchall()
    conn.close()
    inventory = {row[0]: {"x": row[1], "y": row[2], "lastModified": row[3], "nickname": row[4]} for row in rows}
    return inventory

def update_storage(qr_code, data):
    """
    데이터베이스에 항목 저장 또는 업데이트
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR REPLACE INTO inventory (qr_code, x, y, last_modified, nickname)
        VALUES (?, ?, ?, ?, ?)
    ''', (qr_code, data["x"], data["y"], data["lastModified"], data["nickname"]))
    conn.commit()
    conn.close()

def delete_storage(qr_code):
    """
    데이터베이스에서 항목 삭제
    """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM inventory WHERE qr_code = ?', (qr_code,))
    conn.commit()
    conn.close()