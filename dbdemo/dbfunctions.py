import pymysql

def connect():
    try:
        connection = pymysql.connect(
            host="10.241.42.218", #10.241.42.218
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
        connection.rollback()
    finally:
        cursor.close()
        connection.close()


def updaterecord(id,fi,la,de,ye):
    try:
        connection = connect()
        if(connection):
            cursor = connection.cursor()
            sql = f"""
                update employees set
                firstname='{fi}',lastname='{la}',department='{de}',yearhired={ye}
                where empid={id}
                """
            cursor.execute(sql)
            connection.commit()
            print("Record Updated")
    except Exception as e:
        print(e)
        connection.rollback()
    finally:
        cursor.close()
        connection.close()


def deleterecord(id):
    try:
        connection = connect()
        if(connection):
            cursor = connection.cursor()
            sql = f"delete from employees where empid={id}"
            cursor.execute(sql)
            connection.commit()
            print("record deleted")
    except Exception as e:
        print(e)
        connection.rollback()
    finally:
        cursor.close()
        connection.close()

def clearemployeestable():
    try:
        connection=connect()
        if(connection):
            cursor = connection.cursor()
            sql = "truncate table employees"
            cursor.execute(sql)
            connection.commit()
            print('Employees table has been cleared')
    except Exception as e:
        print(e)
        connection.rollback()
    finally:
        cursor.close()
        connection.close()
