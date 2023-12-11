import pymysql

def connect():
    try:
        connection = pymysql.connect(
            host="localhost",
            user="eyadmin",
            password="123",
            database="eygds")
        print("connect ok")
        return connection
    except Exception as e:
        print(e)
        return

# read and load data
def getall():
    try:
        connection = connect()
        if(connection):
            cursor = connection.cursor()
            sql = "select * from employees"
            cursor.execute(sql)
            rows = cursor.fetchall()
            for r in rows:
                print(f'{r[0]},{r[1]},{r[2]},{r[3]},{r[4]}')
        
        # if(connect()):
        #     rows = connect().cursor().execute("select * from employees").fetchall()
        #     for r in rows:
        #         print(f"{r[0]},{r[1]},{r[2]},{r[3]},{r[4]}")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()


# add record - firstname,lastname,department,yearhired
def addrecord(fn,ln,de,ye):
    try:
        connection = connect()
        if(connection):
            cursor = connection.cursor()
            sql = f"""
                    insert into employees 
                    (firstname,lastname,department,yearhired) 
                    values  
                    ('{fn}','{ln}','{de}',{ye})
                    """

            cursor.execute(sql)
            connection.commit()
            print("new record added")
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        connection.close()










