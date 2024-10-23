import sqlite3

def init_db():
    conn = sqlite3.connect('pci_dss_assessment.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS assessments (
            id INTEGER PRIMARY KEY,
            date TEXT,
            requirement TEXT,
            status TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_assessment(date, requirement, status):
    conn = sqlite3.connect('pci_dss_assessment.db')
    c = conn.cursor()
    c.execute('INSERT INTO assessments (date, requirement, status) VALUES (?, ?, ?)', (date, requirement, status))
    conn.commit()
    conn.close()
