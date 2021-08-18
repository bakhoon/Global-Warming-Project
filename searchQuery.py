import sqlite3


def OceanTemp(theMonth, getCF, toYear, fromYear):
    connect = sqlite3.connect("database.db")
    if theMonth == "All":
        if getCF == "C":
            cursor = connect.execute('select years, months, tempC from Datas where years >= ? and years <= ?;', (fromYear, toYear))
            getDatas = cursor.fetchall()
            getAllData = []
            for i in getDatas:
                exactYear = float(0.0)
                if i[1] == "Jan": exactYear = i[0] + 0
                elif i[1] == "Feb": exactYear = i[0] + 0.08333333333
                elif i[1] == "Mar": exactYear = i[0] + 0.16666666666
                elif i[1] == "Apr": exactYear = i[0] + 0.25
                elif i[1] == "May": exactYear = i[0] + 0.33333333333
                elif i[1] == "Jun": exactYear = i[0] + 0.41666666666
                elif i[1] == "Jul": exactYear = i[0] + 0.5
                elif i[1] == "Aug": exactYear = i[0] + 0.58333333333
                elif i[1] == "Sep": exactYear = i[0] + 0.66666666666
                elif i[1] == "Oct": exactYear = i[0] + 0.75
                elif i[1] == "Nov": exactYear = i[0] + 0.83333333333
                elif i[1] == "Dec": exactYear = i[0] + 0.91666666666
                tempData = (exactYear, i[2])
                getAllData.append(tempData)
            return getAllData
        elif getCF == "F":
            cursor = connect.execute('select years, months, tempF from Datas where years >= ? and years <= ?;', (fromYear, toYear))
            getDatas = cursor.fetchall()
            getAllData = []
            for i in getDatas:
                exactYear = float(0.0)
                if i[1] == "Jan": exactYear = i[0] + 0
                elif i[1] == "Feb": exactYear = i[0] + 0.08333333333
                elif i[1] == "Mar": exactYear = i[0] + 0.16666666666
                elif i[1] == "Apr": exactYear = i[0] + 0.25
                elif i[1] == "May": exactYear = i[0] + 0.33333333333
                elif i[1] == "Jun": exactYear = i[0] + 0.41666666666
                elif i[1] == "Jul": exactYear = i[0] + 0.5
                elif i[1] == "Aug": exactYear = i[0] + 0.58333333333
                elif i[1] == "Sep": exactYear = i[0] + 0.66666666666
                elif i[1] == "Oct": exactYear = i[0] + 0.75
                elif i[1] == "Nov": exactYear = i[0] + 0.83333333333
                elif i[1] == "Dec": exactYear = i[0] + 0.91666666666
                tempData = (exactYear, i[2])
                getAllData.append(tempData)
            return getAllData
    else:
        if getCF == "C":
            cursor = connect.execute('select years, tempC from Datas where months = ? and years >= ? and years <= ?;', (theMonth, fromYear, toYear))
            getDatas = cursor.fetchall()
            return getDatas
        elif getCF == "F":
            cursor = connect.execute('select years, tempF from Datas where months = ? and years >= ? and years <= ?;', (theMonth, fromYear, toYear))
            getDatas = cursor.fetchall()
            return getDatas


def EarthTemp(theMonth, getCF, toYear, fromYear, getSource):
    connect = sqlite3.connect("database.db")
    if theMonth == "All":
        if getCF == "C":
            cursor = connect.execute('select years, months, tempC from Earth where years >= ? and years <= ? and types = ?;', (fromYear, toYear, getSource))
            getDatas = cursor.fetchall()
            getAllData = []
            for i in getDatas:
                exactYear = float(0.0)
                if i[1] == "01": exactYear = i[0] + 0
                elif i[1] == "02": exactYear = i[0] + 0.08333333333
                elif i[1] == "03": exactYear = i[0] + 0.16666666666
                elif i[1] == "04": exactYear = i[0] + 0.25
                elif i[1] == "05": exactYear = i[0] + 0.33333333333
                elif i[1] == "06": exactYear = i[0] + 0.41666666666
                elif i[1] == "07": exactYear = i[0] + 0.5
                elif i[1] == "08": exactYear = i[0] + 0.58333333333
                elif i[1] == "09": exactYear = i[0] + 0.66666666666
                elif i[1] == "10": exactYear = i[0] + 0.75
                elif i[1] == "11": exactYear = i[0] + 0.83333333333
                elif i[1] == "12": exactYear = i[0] + 0.91666666666
                tempData = (exactYear, i[2])
                getAllData.append(tempData)
            print(getAllData)
            return getAllData
        elif getCF == "F":
            cursor = connect.execute('select years, months, tempF from Earth where years >= ? and years <= ? and types = ?;', (fromYear, toYear, getSource))
            getDatas = cursor.fetchall()

            getAllData = []
            for i in getDatas:
                exactYear = float(0.0)
                if i[1] == "01": exactYear = i[0] + 0
                elif i[1] == "02": exactYear = i[0] + 0.08333333333
                elif i[1] == "03": exactYear = i[0] + 0.16666666666
                elif i[1] == "04": exactYear = i[0] + 0.25
                elif i[1] == "05": exactYear = i[0] + 0.33333333333
                elif i[1] == "06": exactYear = i[0] + 0.41666666666
                elif i[1] == "07": exactYear = i[0] + 0.5
                elif i[1] == "08": exactYear = i[0] + 0.58333333333
                elif i[1] == "09": exactYear = i[0] + 0.66666666666
                elif i[1] == "10": exactYear = i[0] + 0.75
                elif i[1] == "11": exactYear = i[0] + 0.83333333333
                elif i[1] == "12": exactYear = i[0] + 0.91666666666
                tempData = (exactYear, i[2])
                getAllData.append(tempData)
            print(getAllData)
            return getAllData
    else:
        if getCF == "C":
            cursor = connect.execute('select years, tempC from Earth where months = ? and years >= ? and years <= ? and types = ?;', (theMonth, fromYear, toYear, getSource))
            getDatas = cursor.fetchall()
            return getDatas
        elif getCF == "F":
            cursor = connect.execute('select years, tempF from Earth where months = ? and years >= ? and years <= ? and types = ?;', (theMonth, fromYear, toYear, getSource))
            getDatas = cursor.fetchall()
            return getDatas


def SeaLevel(fromMonth, fromYear, toMonth, toYear):
    listOfMonth = []
    connect = sqlite3.connect("database.db")
    cursor = connect.execute('select * from Sea where years = ? and months >= ?;', (fromYear, fromMonth))
    getYear = cursor.fetchall()
    for i in getYear:
        exactYear = float(0.0)
        if i[1] == "01":
            exactYear = i[0] + 0
        elif i[1] == "02":
            exactYear = i[0] + 0.08333333333
        elif i[1] == "03":
            exactYear = i[0] + 0.16666666666
        elif i[1] == "04":
            exactYear = i[0] + 0.25
        elif i[1] == "05":
            exactYear = i[0] + 0.33333333333
        elif i[1] == "06":
            exactYear = i[0] + 0.41666666666
        elif i[1] == "07":
            exactYear = i[0] + 0.5
        elif i[1] == "08":
            exactYear = i[0] + 0.58333333333
        elif i[1] == "09":
            exactYear = i[0] + 0.66666666666
        elif i[1] == "10":
            exactYear = i[0] + 0.75
        elif i[1] == "11":
            exactYear = i[0] + 0.83333333333
        elif i[1] == "12":
            exactYear = i[0] + 0.91666666666
        tempData = (exactYear, i[2])
        listOfMonth.append(tempData)
    cursor1 = connect.execute('select * from Sea where years > ? and years < ?;', (fromYear, toYear))
    getYear = cursor1.fetchall()
    for i in getYear:
        exactYear = float(0.0)
        if i[1] == "01":
            exactYear = i[0] + 0
        elif i[1] == "02":
            exactYear = i[0] + 0.08333333333
        elif i[1] == "03":
            exactYear = i[0] + 0.16666666666
        elif i[1] == "04":
            exactYear = i[0] + 0.25
        elif i[1] == "05":
            exactYear = i[0] + 0.33333333333
        elif i[1] == "06":
            exactYear = i[0] + 0.41666666666
        elif i[1] == "07":
            exactYear = i[0] + 0.5
        elif i[1] == "08":
            exactYear = i[0] + 0.58333333333
        elif i[1] == "09":
            exactYear = i[0] + 0.66666666666
        elif i[1] == "10":
            exactYear = i[0] + 0.75
        elif i[1] == "11":
            exactYear = i[0] + 0.83333333333
        elif i[1] == "12":
            exactYear = i[0] + 0.91666666666
        tempData = (exactYear, i[2])
        listOfMonth.append(tempData)
    cursor2 = connect.execute('select * from Sea where years = ? and months <= ?;', (toYear, toMonth))
    getYear = cursor2.fetchall()
    for i in getYear:
        exactYear = float(0.0)
        if i[1] == "01":
            exactYear = i[0] + 0
        elif i[1] == "02":
            exactYear = i[0] + 0.08333333333
        elif i[1] == "03":
            exactYear = i[0] + 0.16666666666
        elif i[1] == "04":
            exactYear = i[0] + 0.25
        elif i[1] == "05":
            exactYear = i[0] + 0.33333333333
        elif i[1] == "06":
            exactYear = i[0] + 0.41666666666
        elif i[1] == "07":
            exactYear = i[0] + 0.5
        elif i[1] == "08":
            exactYear = i[0] + 0.58333333333
        elif i[1] == "09":
            exactYear = i[0] + 0.66666666666
        elif i[1] == "10":
            exactYear = i[0] + 0.75
        elif i[1] == "11":
            exactYear = i[0] + 0.83333333333
        elif i[1] == "12":
            exactYear = i[0] + 0.91666666666
        tempData = (exactYear, i[2])
        listOfMonth.append(tempData)
    return listOfMonth


def CO2(fromMonth, fromYear, toMonth, toYear):
    listOfMonth = []
    connect = sqlite3.connect("database.db")
    cursor = connect.execute('select * from CO2 where years = ? and months >= ?;', (fromYear, fromMonth))
    getYear = cursor.fetchall()
    for i in getYear:
        exactYear = float(0.0)
        if i[1] == "01":
            exactYear = i[0] + 0
        elif i[1] == "02":
            exactYear = i[0] + 0.08333333333
        elif i[1] == "03":
            exactYear = i[0] + 0.16666666666
        elif i[1] == "04":
            exactYear = i[0] + 0.25
        elif i[1] == "05":
            exactYear = i[0] + 0.33333333333
        elif i[1] == "06":
            exactYear = i[0] + 0.41666666666
        elif i[1] == "07":
            exactYear = i[0] + 0.5
        elif i[1] == "08":
            exactYear = i[0] + 0.58333333333
        elif i[1] == "09":
            exactYear = i[0] + 0.66666666666
        elif i[1] == "10":
            exactYear = i[0] + 0.75
        elif i[1] == "11":
            exactYear = i[0] + 0.83333333333
        elif i[1] == "12":
            exactYear = i[0] + 0.91666666666
        tempData = (exactYear, i[2])
        listOfMonth.append(tempData)
    cursor1 = connect.execute('select * from CO2 where years > ? and years < ?;', (fromYear, toYear))
    getYear = cursor1.fetchall()
    for i in getYear:
        exactYear = float(0.0)
        if i[1] == "01":
            exactYear = i[0] + 0
        elif i[1] == "02":
            exactYear = i[0] + 0.08333333333
        elif i[1] == "03":
            exactYear = i[0] + 0.16666666666
        elif i[1] == "04":
            exactYear = i[0] + 0.25
        elif i[1] == "05":
            exactYear = i[0] + 0.33333333333
        elif i[1] == "06":
            exactYear = i[0] + 0.41666666666
        elif i[1] == "07":
            exactYear = i[0] + 0.5
        elif i[1] == "08":
            exactYear = i[0] + 0.58333333333
        elif i[1] == "09":
            exactYear = i[0] + 0.66666666666
        elif i[1] == "10":
            exactYear = i[0] + 0.75
        elif i[1] == "11":
            exactYear = i[0] + 0.83333333333
        elif i[1] == "12":
            exactYear = i[0] + 0.91666666666
        tempData = (exactYear, i[2])
        listOfMonth.append(tempData)
    cursor2 = connect.execute('select * from CO2 where years = ? and months <= ?;', (toYear, toMonth))
    getYear = cursor2.fetchall()
    for i in getYear:
        exactYear = float(0.0)
        if i[1] == "01":
            exactYear = i[0] + 0
        elif i[1] == "02":
            exactYear = i[0] + 0.08333333333
        elif i[1] == "03":
            exactYear = i[0] + 0.16666666666
        elif i[1] == "04":
            exactYear = i[0] + 0.25
        elif i[1] == "05":
            exactYear = i[0] + 0.33333333333
        elif i[1] == "06":
            exactYear = i[0] + 0.41666666666
        elif i[1] == "07":
            exactYear = i[0] + 0.5
        elif i[1] == "08":
            exactYear = i[0] + 0.58333333333
        elif i[1] == "09":
            exactYear = i[0] + 0.66666666666
        elif i[1] == "10":
            exactYear = i[0] + 0.75
        elif i[1] == "11":
            exactYear = i[0] + 0.83333333333
        elif i[1] == "12":
            exactYear = i[0] + 0.91666666666
        tempData = (exactYear, i[2])
        listOfMonth.append(tempData)
    return listOfMonth


def theYears():
    connect = sqlite3.connect("database.db")
    cursor = connect.execute('select distinct years from Datas order by years desc;')
    getYear = cursor.fetchall()
    getYears = []
    for i in getYear:
        getYears.append(i[0])
    return getYears


def theYearsEarth():
    connect = sqlite3.connect("database.db")
    cursor = connect.execute('select distinct years from Earth order by years desc;')
    getYear = cursor.fetchall()
    getYears = []
    for i in getYear:
        getYears.append(i[0])
    return getYears


def theYearsSea():
    connect = sqlite3.connect("database.db")
    cursor = connect.execute('select distinct years from Earth order by years desc;')
    getYear = cursor.fetchall()
    getYears = []
    for i in getYear:
        getYears.append(i[0])
    return getYears


def theYearsCO2():
    connect = sqlite3.connect("database.db")
    cursor = connect.execute('select distinct years from CO2 order by years desc;')
    getYear = cursor.fetchall()
    getYears = []
    for i in getYear:
        getYears.append(i[0])
    return getYears


def theMonthsSeaLevel():
    getYears = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return getYears


def theYearsSeaLevel():
    connect = sqlite3.connect("database.db")
    cursor = connect.execute('select distinct years from Sea order by years desc;')
    getYear = cursor.fetchall()
    getYears = []
    for i in getYear:
        getYears.append(i[0])
    return getYears


def getNum():
    connect = sqlite3.connect("database.db")
    cursor = connect.execute('select num from Num;')
    getNum = cursor.fetchall()
    getVal = getNum[0][0]
    getStr = str(getVal)
    return getStr