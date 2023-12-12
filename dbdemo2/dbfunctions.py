import pymysql
from getpass import getpass

def connect():
    try:

        myhost = input('enter host name: ')
        myuser = getpass('enter username: ')
        mypass = getpass('enter password: ')
        mydb = input('enter database name: ')

        connection = pymysql.connect(
            host=myhost, #10.241.42.218
            user=myuser,
            password=mypass,
            database=mydb)
        
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
            sql = "select * from employees2"
            cursor.execute(sql)
            rows = cursor.fetchall()
            for r in rows:
                print(f'{r[0]},{r[1]},{r[2]},{r[3]},{r[4]},{r[5]},{r[6]}')
        
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
def addrecord(fn,ln,de,po,sa,br):
    try:
        connection = connect()
        if(connection):
            cursor = connection.cursor()
            sql = f"""
                    insert into employees2 
                    (firstname,lastname,department,position,salary,branch) 
                    values  
                    ('{fn}','{ln}','{de}','{po}',{sa},'{br}')
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


def updaterecord(id,fi,la,de,po,sa,br):
    try:
        connection = connect()
        if(connection):
            cursor = connection.cursor()
            sql = f"""
                update employees2 set
                firstname='{fi}',lastname='{la}',department='{de}',
                salary={sa},position='{po}',branch='{br}'
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
            sql = f"delete from employees2 where empid={id}"
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
            sql = "truncate table employees2"
            cursor.execute(sql)
            connection.commit()
            print('Employees table has been cleared')
    except Exception as e:
        print(e)
        connection.rollback()
    finally:
        cursor.close()
        connection.close()
