# -*- coding=UTF-8 -*-
import MySQLdb
import sys

class mmdb:
    def __init__(self):
        pass

    def execute(self, sql):
        # 打开数据库连接
        db = MySQLdb.connect("mmDB", "moumou", "9Af9TFYheBjfBT3Q", "moumou")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        try:
            if isinstance(sql, list):
                i = 0
                ret = []
                for s in sql:
                    ret.append(cursor.execute(s))
                    i += 1
            else:
                ret = cursor.execute(sql)
            db.commit()
        except:
            print sys.exc_info()[0]
            db.rollback()
        # 关闭数据库连接
        db.close()
        return ret
