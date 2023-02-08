import sqlite3
from APP_IngresosGastos.connection import ConnectDatabase
from config import DATABASE

def select_all():
    connection = ConnectDatabase("SELECT id, Date, Description, Value FROM movements order by date;")

    rows = connection.res.fetchall() # Se capturan filas de datos
    columns = connection.res.description # Se capturan nombres de columnas

    allRecords = []

    for row in rows:
        record = {}
        for position, column in enumerate(columns):
            record[column[0]] = row[position]
        allRecords.append(record)
    
    connection.con.close()

    return allRecords

def insert(requestFormValues):
    connection = ConnectDatabase("INSERT INTO movements(Date, Description, Value) VALUES(?, ?, ?)", requestFormValues)
    connection.con.commit()
    connection.con.close()

def select_by(id):
    connection = ConnectDatabase(f"SELECT id, Date, Description, Value FROM movements WHERE id={id}")
    record = connection.res.fetchall()
    connection.con.close()
    return  record[0] 

def delete_by(id):
    connection = ConnectDatabase(f"DELETE FROM movements WHERE id={id}")
    connection.con.commit()
    connection.con.close()

def edit_by(id, record):
    connection = ConnectDatabase(f"UPDATE movements SET Date=?, Description=?, Value=? WHERE id={id};", record)
    connection.con.commit()
    connection.con.close()

def total_earnings():
    connection = ConnectDatabase(f"SELECT sum(Value) FROM movements WHERE Value>0")
    record = connection.res.fetchall()
    connection.con.close()
    return record[0][0]

def total_expenses():
    connection = ConnectDatabase(f"SELECT sum(Value) FROM movements WHERE Value<0")
    record = connection.res.fetchall()
    connection.con.close()
    return record[0][0]