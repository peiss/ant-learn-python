import pymysql

def get_conn():
    return pymysql.connect(
        host = "127.0.0.1",
        user = "root",
        password = "mysql123***",
        db = "mydb"
    )

def load_file_to_mysql(fname):
    conn = get_conn()
    try:
        with open(fname) as fin:
            for line in fin:
                line = line.strip()
                sid,yuwen,shuxue,yingyu = line.split("\t")
                sql = f"""
                    insert into sgrade (sid,yuwen,shuxue,yingyu)
                    values ('{sid}', {yuwen}, {shuxue},{yingyu})
                """
                cursor = conn.cursor()
                cursor.execute(sql)
            conn.commit()
    finally:
        if conn is not None: conn.close()



def query_all_sgrades():
    conn = get_conn()
    try:
        sql = "select * from sgrade"
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()
    finally:
        if conn is not None: conn.close()


def query_sgrade_byid(sid):
    conn = get_conn()
    try:
        sql = f"select * from sgrade where sid='{sid}'"
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchone()
    finally:
        if conn is not None: conn.close()


if __name__ == "__main__":
    # load file to mysql
    #load_file_to_mysql("input.txt")

    # query all sgrades
    all_grades = query_all_sgrades()
    for sgrade in all_grades: print(sgrade)

    # query sgrade by id
    grade1 = query_sgrade_byid("s001")
    print("grade1:", grade1)
    grade2 = query_sgrade_byid("s002")
    print("grade2:", grade2)