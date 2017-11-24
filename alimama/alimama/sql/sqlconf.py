# -*- coding: utf-8 -*-

MysqlConfig = {
    'port': 3306,
    # 启动时连接池中创建的的连接数
    'mincached': 1,
    # 连接池中最大允许创建的连接数
    'maxcached': 5,
    'user': 'root',
    'charset': 'utf8',
    'db': 'taobaok',
    # 所有允许的最大连接数上限设置
    'maxconnections': 10,
    'passwd': '123456',
    'host': '127.0.0.1'
}
