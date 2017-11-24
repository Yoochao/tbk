# -*- coding: utf-8 -*-
import MySQLdb
from DBUtils.PooledDB import PooledDB
from MySQLdb.cursors import DictCursor

from sqlconf import MysqlConfig


class MysqlTBK(object):
    """
    Attributes:
       None
    """
    __mysql_pool = None

    def __init__(self):
        self.__mysql_conn = MysqlTBK.__get_connection()
        self.__mysql_cursor = self.__mysql_conn.cursor()

    @staticmethod
    def __get_connection():
        """ get mysql connection
         :arg
         None
        :return
        connection
        """
        if not MysqlTBK.__mysql_pool:
            MysqlTBK.__mysql_pool = PooledDB(
                creator=MySQLdb,
                use_unicode=False,
                cursorclass=DictCursor,
                db=MysqlConfig['db'],
                host=MysqlConfig['host'],
                port=MysqlConfig['port'],
                user=MysqlConfig['user'],
                passwd=MysqlConfig['passwd'],
                charset=MysqlConfig['charset'],
                mincached=MysqlConfig['mincached'],
                maxcached=MysqlConfig['maxcached'],
                maxconnections=MysqlConfig['maxconnections'])
        return MysqlTBK.__mysql_pool.connection()

    def select(self, sql_command, cmd_param=None):
        if cmd_param:
            count = self.__mysql_cursor.execute(sql_command, cmd_param)
        else:
            count = self.__mysql_cursor.execute(sql_command)
        if count:
            sql_result = self.__mysql_cursor.fetchall()
        else:
            sql_result = None
        return sql_result

    def insert(self, sql_command, cmd_param=None):
        if cmd_param:
            self.__mysql_cursor.execute(sql_command, cmd_param)
        else:
            self.__mysql_cursor.execute(sql_command)

    def update(self, sql_command, cmd_param=None):
        if cmd_param:
            self.__mysql_cursor.execute(sql_command, cmd_param)
        else:
            self.__mysql_cursor.execute(sql_command)

    def batch_insert(self, sql_command, cmd_param=None):
        if cmd_param:
            self.__mysql_cursor.executemany(sql_command, cmd_param)

    def commit(self):
        self.__mysql_conn.commit()

    def rollback(self):
        self.__mysql_conn.rollback()

    def con_release(self):
        """release the mysql connection

        :return:
        """
        self.__mysql_cursor.close()
        self.__mysql_conn.close()
