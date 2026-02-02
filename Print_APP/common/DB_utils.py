import pymysql
import redis
import pytest


class DB:

    def __init__(self):
        # --- MySQL ---
        self.conn = pymysql.connect(
            host="127.0.0.1",
            user="root",
            password="123456",
            database="test",
            charset="utf8mb4"
        )
        self.cursor = self.conn.cursor()

        # --- Redis ---
        self.redis = redis.Redis(
            host="127.0.0.1",
            port=6379,
            db=0,
            password=None
        )

    # ---------------------------------------------------------
    # 执行单条 SQL
    # ---------------------------------------------------------
    def exec(self, sql: str):
        sql = sql.strip().rstrip(";")
        self.cursor.execute(sql)

        # 返回查询结果
        if sql.lower().startswith(("select", "show", "describe")):
            return self.cursor.fetchall()
        else:
            self.conn.commit()
            return "OK"

    # ---------------------------------------------------------
    # 执行多条 SQL，返回 dict
    # ---------------------------------------------------------
    def exec_many(self, sql_list):
        results = {}
        for sql in sql_list:
            clean_sql = sql.strip().rstrip(";")
            self.cursor.execute(clean_sql)

            if clean_sql.lower().startswith(("select", "show", "describe")):
                results[clean_sql] = self.cursor.fetchall()
            else:
                self.conn.commit()
                results[clean_sql] = "OK"

        return results

    # ---------------------------------------------------------
    def close(self):
        try:
            self.cursor.close()
            self.conn.close()
        except:
            pass
        # Redis 无需关闭
