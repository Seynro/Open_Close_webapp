import subprocess
import psutil
import os
import webbrowser

import eel

eel.init("web")

#SQLLIGHT DB

import sqlite3

def insert_varible_into_table(path:str, proces:str):
    try:
        connection = sqlite3.connect('proceses.db')
        cursor = connection.cursor()
        print("Подключен к SQLite")
        cursor.execute('''CREATE TABLE IF NOT EXISTS  proceses
              (path TEXT, proces TEXT)''')

        sqlite_insert_with_param = """INSERT INTO proceses
                              (path, proces)
                              VALUES (?, ?);"""

        data_tuple = (path, proces)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        connection.commit()
        print("Переменные Python успешно вставлены в таблицу proceses")

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if connection:
            connection.close()
            print("Соединение с SQLite закрыто")




def adding(path:str):
    proces = str(path.rsplit('/',1)[1])
    insert_varible_into_table(path, proces)

#SQLLIGHT DB

@eel.expose
def open():
    subprocess.Popen('C:\\Program Files\\Rainmeter\\Rainmeter.exe')
    subprocess.Popen('C:\\Users\\user\\AppData\\Local\\Grammarly\\DesktopIntegrations\\Grammarly.Desktop.exe')
    subprocess.Popen('D:\\Telegram Desktop\\Telegram.exe')

@eel.expose
def close():
    for process in (process for process in psutil.process_iter() if process.name() == "Rainmeter.exe"):
        process.kill()

    for process in (process for process in psutil.process_iter() if process.name() == "Telegram.exe"):
        process.kill()

    for process in (process for process in psutil.process_iter() if process.name() == "Grammarly.Desktop.exe"):
        process.kill()

    path = "C:\\Users\\user\\Desktop\\Programs\\Games"
    webbrowser.open(path)

@eel.expose
def path_str(path:str):
    print('path_str done ', path)
    path = str(path)
    adding(path)

eel.start("python_open.html", size= (1960, 1020))
