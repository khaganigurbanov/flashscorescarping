import sqlite3, os

PATH = "C:\\Users\\Xaqani\\PycharmProjects\\untitled1\\venv"
#PATH = os.getcwd()
NAME = "/myscore.db"

class Database:

    def __init__(self, path):
        # self.path = path # "C:/Users/terminator/Desktop/Scripts/EFS/myscore.db"
        # self.path = PATH + NAME
        self.path = path

    def connect(self):
        return sqlite3.connect(self.path)

    def read(self, sql, **kwargs):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        if kwargs.setdefault("all", False):
            res = cursor.fetchall()
        else:
            res = cursor.fetchone()
        conn.close()
        return res


    def read_iter(self, sql):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor


    def write(self, sql, args = None):
        conn = self.connect()
        cursor = conn.cursor()
        if args:
            cursor.executemany(sql, args)
        else:
            cursor.execute(sql)
        conn.commit()
        conn.close()


if __name__ == '__main__':
    db = Database("C:\\Users\\Xaqani\\PycharmProjects\\untitled1\\venv\\myscore.db")
    db.write("CREATE TABLE match (id_match TEXT, date_match DATETIME , time_match DATETIME , country TEXT , league TEXT , team1 TEXT , team2 TEXT,   ht_score_h integer , ht_score_a integer , ft_score_h integer , ft_score_a , status  integer, isDelete integer )")
    # result = db.read("SELECT url FROM match", all = True)
    # for url in result:
    #     print(url[0])