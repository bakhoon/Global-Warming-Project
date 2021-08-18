import sqlite3


def tableSeaTemp(getMonth, getCF, toYear, fromYear):
    if fromYear > toYear:
        print("error!")
    else:
        connect = sqlite3.connect("database.db")
        getDatas = None
        if getCF == "C":
            cursor = connect.execute('select years, months, tempC from Datas where years >= ? and years <= ?;',
                                     (fromYear, toYear))
            getDatas = cursor.fetchall()
        elif getCF == "F":
            cursor = connect.execute('select years, months, tempF from Datas where years >= ? and years <= ?;',
                                     (fromYear, toYear))
            getDatas = cursor.fetchall()
        if getMonth != "Total":
            getList = []
            for i in getDatas:
                if getMonth == "January" and i[1] == "Jan":
                    tempList = (i[0], "January", i[2])
                    getList.append(tempList)
                elif getMonth == "February" and i[1] == "Feb":
                    tempList = (i[0], "February", i[2])
                    getList.append(tempList)
                elif getMonth == "March" and i[1] == "Mar":
                    tempList = (i[0], "March", i[2])
                    getList.append(tempList)
                elif getMonth == "April" and i[1] == "Apr":
                    tempList = (i[0], "April", i[2])
                    getList.append(tempList)
                elif getMonth == "May" and i[1] == "May":
                    tempList = (i[0], "May", i[2])
                    getList.append(tempList)
                elif getMonth == "June" and i[1] == "Jun":
                    tempList = (i[0], "June", i[2])
                    getList.append(tempList)
                elif getMonth == "July" and i[1] == "Jul":
                    tempList = (i[0], "July", i[2])
                    getList.append(tempList)
                elif getMonth == "August" and i[1] == "Aug":
                    tempList = (i[0], "August", i[2])
                    getList.append(tempList)
                elif getMonth == "September" and i[1] == "Sep":
                    tempList = (i[0], "September", i[2])
                    getList.append(tempList)
                elif getMonth == "October" and i[1] == "Oct":
                    tempList = (i[0], "October", i[2])
                    getList.append(tempList)
                elif getMonth == "November" and i[1] == "Nov":
                    tempList = (i[0], "November", i[2])
                    getList.append(tempList)
                elif getMonth == "December" and i[1] == "Dec":
                    tempList = (i[0], "December", i[2])
                    getList.append(tempList)
            print(getList)
            return getList
        elif getMonth == "Total":
            getList = []
            for i in getDatas:
                if i[1] == "Jan":
                    tempList = (i[0], "January", i[2])
                    getList.append(tempList)
                elif i[1] == "Feb":
                    tempList = (i[0], "February", i[2])
                    getList.append(tempList)
                elif i[1] == "Mar":
                    tempList = (i[0], "March", i[2])
                    getList.append(tempList)
                elif i[1] == "Apr":
                    tempList = (i[0], "April", i[2])
                    getList.append(tempList)
                elif i[1] == "May":
                    tempList = (i[0], "May", i[2])
                    getList.append(tempList)
                elif i[1] == "Jun":
                    tempList = (i[0], "June", i[2])
                    getList.append(tempList)
                elif i[1] == "Jul":
                    tempList = (i[0], "July", i[2])
                    getList.append(tempList)
                elif i[1] == "Aug":
                    tempList = (i[0], "August", i[2])
                    getList.append(tempList)
                elif i[1] == "Sep":
                    tempList = (i[0], "September", i[2])
                    getList.append(tempList)
                elif i[1] == "Oct":
                    tempList = (i[0], "October", i[2])
                    getList.append(tempList)
                elif i[1] == "Nov":
                    tempList = (i[0], "November", i[2])
                    getList.append(tempList)
                elif i[1] == "Dec":
                    tempList = (i[0], "December", i[2])
                    getList.append(tempList)
            return getList


def tableEarthTemp(getMonth, getCF, toYear, fromYear, Source):
    if fromYear > toYear:
        print("error!")
    else:
        connect = sqlite3.connect("database.db")
        if getMonth == "Total":
            if getCF == "C":
                cursor = connect.execute('select years, months, tempC from Earth where (years >= ? and years <= ?) and types = ?;', (fromYear, toYear, Source))
                getDatas = cursor.fetchall()
                theList = getTableforEarth(getDatas)
                return theList
            elif getCF == "F":
                cursor = connect.execute('select years, months, tempF from Earth where (years >= ? and years <= ?) and types = ?;', (fromYear, toYear, Source))
                getDatas = cursor.fetchall()
                theList = getTableforEarth(getDatas)
                return theList
        elif getMonth != "Total":
            if getCF == "F":
                cursor = connect.execute('select years, months, tempF from Earth where (years >= ? and years <= ?) and types = ?;', (fromYear, toYear, Source))
                getDatas = cursor.fetchall()
                tempList = []
                for i in getDatas:
                    if i[1] == "01" and getMonth == "January":
                        tempgroup = (i[0], "January", i[2])
                        tempList.append(tempgroup)
                    elif i[1] == "02" and getMonth == "February":
                        tempgroup = (i[0], "February", i[2])
                        tempList.append(tempgroup)
                    elif i[1] == "03" and getMonth == "March":
                        tempgroup = (i[0], "March", i[2])
                        tempList.append(tempgroup)
                    elif i[1] == "04" and getMonth == "April":
                        tempgroup = (i[0], "April", i[2])
                        tempList.append(tempgroup)
                    elif i[1] == "05" and getMonth == "May":
                        tempgroup = (i[0], "May", i[2])
                        tempList.append(tempgroup)
                    elif i[1] == "06" and getMonth == "June":
                        tempgroup = (i[0], "June", i[2])
                        tempList.append(tempgroup)
                    elif i[1] == "07" and getMonth == "July":
                        tempgroup = (i[0], "July", i[2])
                        tempList.append(tempgroup)
                    elif i[1] == "08" and getMonth == "August":
                        tempgroup = (i[0], "August", i[2])
                        tempList.append(tempgroup)
                    elif i[1] == "09" and getMonth == "September":
                        tempgroup = (i[0], "September", i[2])
                        tempList.append(tempgroup)
                    elif i[1] == "10" and getMonth == "October":
                        tempgroup = (i[0], "October", i[2])
                        tempList.append(tempgroup)
                    elif i[1] == "11" and getMonth == "November":
                        tempgroup = (i[0], "November", i[2])
                        tempList.append(tempgroup)
                    elif i[1] == "12" and getMonth == "December":
                        tempgroup = (i[0], "December", i[2])
                        tempList.append(tempgroup)
                return tempList
            if getCF == "C":
                cursor = connect.execute('select years, months, tempC from Earth where (years >= ? and years <= ?) and types = ?;', (fromYear, toYear, Source))
                getDatas = cursor.fetchall()
                tempList = []
                for i in getDatas:
                    if i[1] == "01":
                        tempgroup = (i[0], "January", i[2])
                        tempList.append(tempgroup)
                    elif i[1] == "02":
                        tempgroup = (i[0], "February", i[2])
                        tempList.append(tempgroup)
                    elif i[1] == "03":
                        tempgroup = (i[0], "March", i[2])
                        tempList.append(tempgroup)
                    elif i[1] == "04":
                        tempgroup = (i[0], "April", i[2])
                        tempList.append(tempgroup)
                    elif i[1] == "05":
                        tempgroup = (i[0], "May", i[2])
                        tempList.append(tempgroup)
                    elif i[1] == "06":
                        tempgroup = (i[0], "June", i[2])
                        tempList.append(tempgroup)
                    elif i[1] == "07":
                        tempgroup = (i[0], "July", i[2])
                        tempList.append(tempgroup)
                    elif i[1] == "08":
                        tempgroup = (i[0], "August", i[2])
                        tempList.append(tempgroup)
                    elif i[1] == "09":
                        tempgroup = (i[0], "September", i[2])
                        tempList.append(tempgroup)
                    elif i[1] == "10":
                        tempgroup = (i[0], "October", i[2])
                        tempList.append(tempgroup)
                    elif i[1] == "11":
                        tempgroup = (i[0], "November", i[2])
                        tempList.append(tempgroup)
                    elif i[1] == "12":
                        tempgroup = (i[0], "December", i[2])
                        tempList.append(tempgroup)
                return tempList


def getTableforEarth(list):
    getList = []
    for i in list:
        if i[1] == "01":
            tempList = (i[0], "January", i[2])
            getList.append(tempList)
        elif i[1] == "02":
            tempList = (i[0], "February", i[2])
            getList.append(tempList)
        elif i[1] == "03":
            tempList = (i[0], "March", i[2])
            getList.append(tempList)
        elif i[1] == "04":
            tempList = (i[0], "April", i[2])
            getList.append(tempList)
        elif i[1] == "05":
            tempList = (i[0], "May", i[2])
            getList.append(tempList)
        elif i[1] == "06":
            tempList = (i[0], "June", i[2])
            getList.append(tempList)
        elif i[1] == "07":
            tempList = (i[0], "July", i[2])
            getList.append(tempList)
        elif i[1] == "08":
            tempList = (i[0], "August", i[2])
            getList.append(tempList)
        elif i[1] == "09":
            tempList = (i[0], "September", i[2])
            getList.append(tempList)
        elif i[1] == "10":
            tempList = (i[0], "October", i[2])
            getList.append(tempList)
        elif i[1] == "11":
            tempList = (i[0], "November", i[2])
            getList.append(tempList)
        elif i[1] == "12":
            tempList = (i[0], "December", i[2])
            getList.append(tempList)
    return getList


def tableCO2(fromMonth, fromYear, toMonth, toYear):
    connect = sqlite3.connect("database.db")
    toMonthInt = getMonth(toMonth)
    fromMonthInt = getMonth(fromMonth)
    if fromYear > toYear:
        print("error!")
    elif toYear == fromYear:
        if fromMonthInt > toMonthInt:
            print("error!")
        else:
            cursor = connect.execute('select years, months, amount from CO2 where years = ? and months <= ? and months >= ?;',
                                     (toYear, toMonthInt, fromMonthInt))
            getDatas = cursor.fetchall()
            thisList = getTableforEarth(getDatas)
            return thisList
    elif (int(toYear) - int(fromYear)) == 1:
        cursor = connect.execute('select years, months, amount from CO2 where years = ? and months >= ?;',
                                 (fromYear, fromMonthInt))
        getDatas1 = cursor.fetchall()
        cursor = connect.execute('select years, months, amount from CO2 where years = ? and months <= ?;',
                                 (toYear, toMonthInt))
        getDatas2 = cursor.fetchall()
        getList = getDatas1 + getDatas2
        thisList = getTableforEarth(getList)
        return thisList
    else:
        cursor = connect.execute('select years, months, amount from CO2 where years = ? and months >= ?;',
                                 (fromYear, fromMonthInt))
        getDatas1 = cursor.fetchall()

        cursor = connect.execute('select years, months, amount from CO2 where years > ? and years < ?;',
                                 (fromYear, toYear))
        getDatas3 = cursor.fetchall()

        cursor = connect.execute('select years, months, amount from CO2 where years = ? and months <= ?;',
                                 (toYear, toMonthInt))
        getDatas2 = cursor.fetchall()
        getList = getDatas1 + getDatas3 + getDatas2
        thisList = getTableforEarth(getList)
        return thisList


def tableSeaLevel(fromMonth, fromYear, toMonth, toYear):
    connect = sqlite3.connect("database.db")
    toMonthInt = getMonth(toMonth)
    fromMonthInt = getMonth(fromMonth)
    if fromYear > toYear:
        print("error!")
    elif toYear == fromYear:
        if fromMonthInt > toMonthInt:
            print("error!")
        else:
            cursor = connect.execute('select years, months, mm from Sea where years = ? and months <= ? and months >= ?;',
                                     (toYear, toMonthInt, fromMonthInt))
            getDatas = cursor.fetchall()
            thisList = getTableforEarth(getDatas)
            return thisList
    elif (int(toYear) - int(fromYear)) == 1:
        cursor = connect.execute('select years, months, mm from Sea where years = ? and months >= ?;',
                                 (fromYear, fromMonthInt))
        getDatas1 = cursor.fetchall()
        cursor = connect.execute('select years, months, mm from Sea where years = ? and months <= ?;',
                                 (toYear, toMonthInt))
        getDatas2 = cursor.fetchall()
        getList = getDatas1 + getDatas2
        thisList = getTableforEarth(getList)
        return thisList
    else:
        cursor = connect.execute('select years, months, mm from Sea where years = ? and months >= ?;',
                                 (fromYear, fromMonthInt))
        getDatas1 = cursor.fetchall()

        cursor = connect.execute('select years, months, mm from Sea where years > ? and years < ?;',
                                 (fromYear, toYear))
        getDatas3 = cursor.fetchall()

        cursor = connect.execute('select years, months, mm from Sea where years = ? and months <= ?;',
                                 (toYear, toMonthInt))
        getDatas2 = cursor.fetchall()
        getList = getDatas1 + getDatas3 + getDatas2
        thisList = getTableforEarth(getList)
        return thisList

def getMonth(month):
    if month == "January": return "01"
    elif month == "February": return "02"
    elif month == "March": return "03"
    elif month == "April": return "04"
    elif month == "May": return "05"
    elif month == "June": return "06"
    elif month == "July": return "07"
    elif month == "August": return "08"
    elif month == "September": return "09"
    elif month == "October": return "10"
    elif month == "November": return "11"
    elif month == "December": return "12"

