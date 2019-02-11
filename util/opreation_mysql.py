#coding:utf-8

import MySQLdb.cursors

class OperationMysql:
    def __init__(self,db):
        self.conn = MySQLdb.connect(
            host='192.168.XXX.128',
            port=3306,
            user='root',
            passwd='',
            charset='utf8',
            db=db,
            #设置查询后每条记录的结果已字典表示，默认已列表表示
            cursorclass=MySQLdb.cursors.DictCursor
        )
        #获取操作游标
        self.cur = self.conn.cursor()

    def create_table(self,sql):
        self.cur.execute(sql)

    def insert(self,sql):
        # try:
        #     self.cur.execute(sql)
        #     self.conn.commit()
        # except:
        #     self.conn.rollback()
        self.cur.execute(sql)
        self.conn.commit()

    def select(self,sql):
        try:
            self.cur.execute(sql)
            #获取所有记录列表
            results = self.cur.fetchall()
            return results
        except:
            return "Error: unable to fecth data"

    def update(self,sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()

    def close_db(self):
        self.conn.close()

if __name__ == '__main__':
    op_mysql = OperationMysql('wdfp')
    #op_mysql.create_table(sql)
    # sql = "INSERT INTO TESTONE(FIRST_NAME) VALUES('ABC')"
    #op_mysql.insert(sql)
    #sql = "select * from TESTONE"
    #print(op_mysql.select(sql))
