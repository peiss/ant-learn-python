import db


def test_insert():
    sql = """
        insert user (name, sex, age, email) 
        values('mayi', 'man', 20, 'mayi@qq.com')
    """
    db.insert_or_update_data(sql)


def test_update():
    sql = """
        update user set name='damayi'
        where id=6
    """
    db.insert_or_update_data(sql)


def test_select():
    sql = """
        select * from user
    """
    import pprint
    pprint.pprint(db.query_data(sql))


if __name__ == "__main__":
    test_insert()
    test_update()
    test_select()
