import pymysql

import os


class ColumbiaStudentResource:

    def __int__(self):
        pass

    @staticmethod
    def _get_connection():
        DBUSER = os.environ.get('DBUSER')
        DBPASSWORD = os.environ.get('DBPASSWORD')
        DBHOST = os.environ.get('HOST')
        conn = pymysql.connect(
            user=DBUSER,
            password=DBPASSWORD,
            host=DBHOST,
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return conn

    @staticmethod
    def get_by_key(key):

        sql = "SELECT * FROM f22_databases.columbia_students where guid=%s";
        conn = ColumbiaStudentResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()

        return result

