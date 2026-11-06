import sqlite3
class sqlite:
    def __init__(self, filename):
        self.con = sqlite3.connect(filename)
        self.c = self.con.cursor()
        self.c.execute('''
        CREATE TABLE IF NOT EXISTS user(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            text TEXT    
        );
        ''')
    def add_note(self, user_id, text):
        self.c.execute('''INSERT INTO user (user_id, text) VALUES (?, ?)''', (user_id, text,))
        self.con.commit()
    def view_notes(self, user_id):
        self.c.execute('''SELECT id, text FROM user WHERE user_id = ?''', (user_id,))
        row = self.c.fetchall()
        if row is None:
            return 'notes not found'
        else:
            return row
    def del_notes(self, id, user_id):
        self.c.execute('''DELETE FROM user WHERE id = ? and user_id = ?''', (id, user_id,))   
        self.con.commit() 
    def del_all_notes(self,user_id):
        self.c.execute('''DELETE FROM user WHERE user_id = ?''', (user_id,))
        self.con.commit()
        