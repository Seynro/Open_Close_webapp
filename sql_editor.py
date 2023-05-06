import sqlite3

def insert_varible_into_table(path:str, proces:str):
    try:
        connection = sqlite3.connect('proceses.db')
        cursor = connection.cursor()
        print("Подключен к SQLite")
        cursor.execute('''CREATE TABLE IF NOT EXISTS  Group1
              (path TEXT, proces TEXT)''')


        sqlite_insert_with_param = """INSERT INTO Group1
                              (path, proces)
                              VALUES (?, ?);"""

        data_tuple = (path, proces)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        connection.commit()
        print("Переменные Python успешно вставлены в таблицу Group1")

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if connection:
            connection.close()
            print("Соединение с SQLite закрыто")

insert_varible_into_table()