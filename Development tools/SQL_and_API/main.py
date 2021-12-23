#Делаю табличку цена биткоина в рублях обновляющуюся через 30 секунд

import requests # Для получения данных с сайта
import time # Для фиксации времени взятия данных
import sqlite3 # Для работы с БД

conn = sqlite3.connect('example.db') #Для сохранения данных в файл
cursor = conn.cursor() #Доступ к БД для выполнения команд

# Выполняем SQL команды
# cursor.execute('CREATE TABLE dollar_rub (symbol text, moment time, price float)')


while True:
    # Взятие данных
    respo = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=BTCRUB')
    respo = respo.json() # Сохраняю данные, что спарсил в словарь
    
    print()
    print(respo['price'])

    cursor.execute(f"INSERT INTO dollar_rub VALUES ({respo['symbol']}, 'Ivan')")


    time.sleep(10) #Ждём 10 секунд



