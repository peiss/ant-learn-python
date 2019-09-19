import pymysql

"""
常用模块：读写MySQL
"""


def get_conn():
    """
    获取MySQL的链接
    :return: mysql connection
    """
    return pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='12345678',
        database='test',
        charset='utf8'
    )


def query_data(sql):
    """
    根据SQL查询数据并且返回
    :param sql: SQL语句
    :return: list[dict]
    """
    conn = get_conn()
    try:
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        return cursor.fetchall()
    finally:
        # 别忘了关闭链接
        conn.close()


def insert_or_update_data(sql):
    """
    执行新增insert或者update的sql
    :param sql: insert or update sql
    :return: 不返回内容
    """
    conn = get_conn()
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        # 注意这里，只有commit才可以生效
        conn.commit()
    finally:
        # 别忘了关闭链接
        conn.close()


