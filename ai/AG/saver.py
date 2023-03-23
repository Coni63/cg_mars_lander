import sqlite3
from typing import Tuple


class Saver:

    def __init__(self, savefile: str):
        self.con = sqlite3.connect(savefile)
        self.cur = self.con.cursor()

        self.cur.execute("CREATE TABLE IF NOT EXISTS experiences(testfile, actions, score)")

    def save(self, testfile: str, actions: str, score: float):
        data = (testfile, actions, score)
        self.cur.execute("INSERT INTO experiences VALUES(?, ?, ?)", data)
        self.con.commit()

    def get_best(self, testfile) -> Tuple[str, float]:
        res = self.cur.execute("""
            SELECT actions, score
            FROM experiences
            WHERE testfile LIKE ?
            ORDER BY score DESC
            LIMIT 1""", (f'%{testfile}', ))
        return res.fetchone()
