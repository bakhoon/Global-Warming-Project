import csv
import sqlite3
import pandas as pd
import numpy as np


def get_data():
    connect = sqlite3.connect("database.db")
    cursor = connect.cursor()
    cursor.execute(
        'create table if not exists Datas(years INTEGER, months TEXT, tempC FLOAT, tempF FLOAT)')
    cursor.execute(
        'create table if not exists CO2(years INTEGER, months TEXT, amount FLOAT)')
    cursor.execute(
        'create table if not exists Earth(types TEXT, years INTEGER, months TEXT, tempC FLOAT, tempF FLOAT)')
    cursor.execute(
        'create table if not exists Sea(years INTEGER, months TEXT, mm FLOAT)')

    searchingCursor = connect.execute(
        'select count(*) from Datas limit 1;')
    searching = searchingCursor.fetchall()

    if searching[0][0] == 0:
        df = pd.read_csv('temperatures.csv')

        allList = []
        monthList = []

        monthOnly = csv.reader(open("temperatures.csv", "r"))
        for set in monthOnly:
            if set[0] == "Year":
                for i in range(1,13):
                    monthList.append(set[i])
        print(monthList)

        for index, rows in df.iterrows():
            tempList = [rows.Year, monthList[0], rows.Jan]
            allList.append(tempList)
            tempList = [rows.Year, monthList[1], rows.Feb]
            allList.append(tempList)
            tempList = [rows.Year, monthList[2], rows.Mar]
            allList.append(tempList)
            tempList = [rows.Year, monthList[3], rows.Apr]
            allList.append(tempList)
            tempList = [rows.Year, monthList[4], rows.May]
            allList.append(tempList)
            tempList = [rows.Year, monthList[5], rows.Jun]
            allList.append(tempList)
            tempList = [rows.Year, monthList[6], rows.Jul]
            allList.append(tempList)
            tempList = [rows.Year, monthList[7], rows.Aug]
            allList.append(tempList)
            tempList = [rows.Year, monthList[8], rows.Sep]
            allList.append(tempList)
            tempList = [rows.Year, monthList[9], rows.Oct]
            allList.append(tempList)
            tempList = [rows.Year, monthList[10], rows.Nov]
            allList.append(tempList)
            tempList = [rows.Year, monthList[11], rows.Dec]
            allList.append(tempList)
        print(allList)
        for i in range(len(allList)):
            if allList[i][2] == '***':
                pass
            else:
                tC = float(allList[i][2])
                getC = tC
                tF = float(allList[i][2])
                getF = (tF * (9/5)) + 32
                finalizeList = [allList[i][0], allList[i][1], getC, getF]
                cursor.execute(
                    "INSERT INTO Datas(years, months, tempC, tempF) VALUES (?,?,?,?);", finalizeList)
                connect.commit()
    else:
        pass

    searchingCursor = connect.execute(
        'select count(*) from CO2 limit 1;')
    searching = searchingCursor.fetchall()

    if searching[0][0] == 0:
        df = pd.read_csv('co2-mm-mlo_csv.csv')

        for index, rows in df.iterrows():
            getMonth = rows.Date
            eachMonth = getMonth.split("-")
            tempList = [eachMonth[0], eachMonth[1], rows.Interpolated]
            cursor.execute(
                "INSERT INTO CO2(years, months, amount) VALUES (?,?,?);", tempList)
            connect.commit()
    else:
        pass

    searchingCursor = connect.execute(
        'select count(*) from Earth limit 1;')
    searching = searchingCursor.fetchall()

    if searching[0][0] == 0:
        df = pd.read_csv('global_temperature.csv')

        for index, rows in df.iterrows():
            getMonth = rows.Date
            eachMonth = getMonth.split("-")
            tempTemp = rows.Mean
            tempinF = (tempTemp * (9/5)) + 32
            tempList = [rows.Source, eachMonth[0], eachMonth[1], rows.Mean, tempinF]
            cursor.execute(
                "INSERT INTO Earth(types, years, months, tempC, tempF) VALUES (?,?,?,?,?);", tempList)
            connect.commit()
    else:
        pass

    searchingCursor = connect.execute(
        'select count(*) from Sea limit 1;')
    searching = searchingCursor.fetchall()

    if searching[0][0] == 0:
        df = pd.read_csv('sea_level.csv')

        for index, rows in df.iterrows():
            getMonth = rows.Time
            eachMonth = getMonth.split("-")
            tempList = [eachMonth[0], eachMonth[1], rows.GMSL]
            cursor.execute(
                "INSERT INTO Sea(years, months, mm) VALUES (?,?,?);", tempList)
            connect.commit()
    else:
        pass

    cursor.execute('create table if not exists Num(num INTEGER)')
    searchingCursor = connect.execute(
        'select count(*) from Num limit 1;')
    searching = searchingCursor.fetchall()
    init = 100
    if searching[0][0] == 0:
        cursor.execute(
            "INSERT INTO Num(num) VALUES (?);", (init,))
        connect.commit()