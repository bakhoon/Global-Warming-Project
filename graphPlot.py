import matplotlib.pyplot as plt
import sqlite3
import os
import os.path

def CreatePlotMeasureSL(getDatas):
    for i in getDatas:
        tempnum = i[0] % 1
        temptempnum = '{0:.4g}'.format(tempnum)
        strnum = str(temptempnum)
        if strnum == '0':
            plt.plot(i[0], i[1], "ro")
        elif strnum == '0.08333':
            plt.plot(i[0], i[1], "yo")
        elif strnum == '0.1667':
            plt.plot(i[0], i[1], "go")
        elif strnum == '0.25':
            plt.plot(i[0], i[1], "co")
        elif strnum == '0.3333':
            plt.plot(i[0], i[1], "bo")
        elif strnum == '0.4167':
            plt.plot(i[0], i[1], "mo")
        elif strnum == '0.5':
            plt.plot(i[0], i[1], "r*")
        elif strnum == '0.5833':
            plt.plot(i[0], i[1], "y*")
        elif strnum == '0.6667':
            plt.plot(i[0], i[1], "g*")
        elif strnum == '0.75':
            plt.plot(i[0], i[1], "c*")
        elif strnum == '0.8333':
            plt.plot(i[0], i[1], "b*")
        elif strnum == '0.9167':
            plt.plot(i[0], i[1], "m*")
    plt.xlabel('Year')
    plt.xticks(rotation=90)
    plt.ylabel('Height in mm')
    connect = sqlite3.connect("database.db")
    cursor = connect.execute('select num from Num;')
    getNum = cursor.fetchall()
    num = getNum[0][0]
    cursor.execute('delete from Num where num = ?', (num,))
    connect.commit()
    numstr = str(num)
    boollean = os.path.isfile(
        'C:\\Users\\HP\\PycharmProjects\\Global Warming Project\\static\\thefile' + numstr + '.png')
    if boollean == False:
        pass
    else:
        os.remove('C:\\Users\\HP\\PycharmProjects\\Global Warming Project\\static\\thefile' + numstr + '.png')
    num += 1
    numstr1 = str(num)
    plt.savefig('C:\\Users\\HP\\PycharmProjects\\Global Warming Project\\static\\thefile' + numstr1 + '.png')
    plt.show()
    cursor.execute('insert into Num(num) values (?);', (num,))
    connect.commit()


def CreatePlotTemp(getDatas, getMonth):
    if getMonth == "Total":
        for i in getDatas:
            tempnum = i[0] % 1
            temptempnum = '{0:.4g}'.format(tempnum)
            strnum = str(temptempnum)
            if strnum == '0':
                plt.plot(i[0], i[1], "ro")
            elif strnum == '0.08333':
                plt.plot(i[0], i[1], "yo")
            elif strnum == '0.1667':
                plt.plot(i[0], i[1], "go")
            elif strnum == '0.25':
                plt.plot(i[0], i[1], "co")
            elif strnum == '0.3333':
                plt.plot(i[0], i[1], "bo")
            elif strnum == '0.4167':
                plt.plot(i[0], i[1], "mo")
            elif strnum == '0.5':
                plt.plot(i[0], i[1], "r*")
            elif strnum == '0.5833':
                plt.plot(i[0], i[1], "y*")
            elif strnum == '0.6667':
                plt.plot(i[0], i[1], "g*")
            elif strnum == '0.75':
                plt.plot(i[0], i[1], "c*")
            elif strnum == '0.8333':
                plt.plot(i[0], i[1], "b*")
            elif strnum == '0.9167':
                plt.plot(i[0], i[1], "m*")
        plt.xlabel('year')
        plt.xticks(rotation=90)
        plt.ylabel('temperature')
        connect = sqlite3.connect("database.db")
        cursor = connect.execute('select num from Num;')
        getNum = cursor.fetchall()
        num = getNum[0][0]
        cursor.execute('delete from Num where num = ?', (num,))
        connect.commit()
        numstr = str(num)
        boollean = os.path.isfile(
            'C:\\Users\\HP\\PycharmProjects\\Global Warming Project\\static\\thefile' + numstr + '.png')
        if boollean == False:
            pass
        else:
            os.remove('C:\\Users\\HP\\PycharmProjects\\Global Warming Project\\static\\thefile' + numstr + '.png')
        num += 1
        numstr1 = str(num)
        plt.savefig('C:\\Users\\HP\\PycharmProjects\\Global Warming Project\\static\\thefile' + numstr1 + '.png')
        plt.show()
        cursor.execute('insert into Num(num) values (?);', (num,))
        connect.commit()
    elif getMonth == "January":
        for i in getDatas:
            plt.plot(i[0], i[1], "ro")
        plt.xlabel('Year')
        plt.xticks(rotation=90)
        plt.ylabel('Temperature')
        connect = sqlite3.connect("database.db")
        cursor = connect.execute('select num from Num;')
        getNum = cursor.fetchall()
        num = getNum[0][0]
        cursor.execute('delete from Num where num = ?', (num,))
        connect.commit()
        numstr = str(num)
        boollean = os.path.isfile(
            'C:\\Users\\HP\\PycharmProjects\\Global Warming Project\\static\\thefile' + numstr + '.png')
        if boollean == False:
            pass
        else:
            os.remove('C:\\Users\\HP\\PycharmProjects\\Global Warming Project\\static\\thefile' + numstr + '.png')
        num += 1
        numstr1 = str(num)
        plt.savefig('C:\\Users\\HP\\PycharmProjects\\Global Warming Project\\static\\thefile' + numstr1 + '.png')
        plt.show()
        cursor.execute('insert into Num(num) values (?);', (num,))
        connect.commit()
    elif getMonth == "February":
        for i in getDatas:
            plt.plot(i[0], i[1], "yo")
        plt.xlabel('year')
        plt.xticks(rotation=90)
        plt.ylabel('temperature')
        connect = sqlite3.connect("database.db")
        cursor = connect.execute('select num from Num;')
        getNum = cursor.fetchall()
        num = getNum[0][0]
        cursor.execute('delete from Num where num = ?', (num,))
        connect.commit()
        numstr = str(num)
        boollean = os.path.isfile(
            'C:\\Users\\HP\\PycharmProjects\\Global Warming Project\\static\\thefile' + numstr + '.png')
        if boollean == False:
            pass
        else:
            os.remove('C:\\Users\\HP\\PycharmProjects\\Global Warming Project\\static\\thefile' + numstr + '.png')
        num += 1
        numstr1 = str(num)
        plt.savefig('C:\\Users\\HP\\PycharmProjects\\Global Warming Project\\static\\thefile' + numstr1 + '.png')
        plt.show()
        cursor.execute('insert into Num(num) values (?);', (num,))
        connect.commit()
    elif getMonth == "March":
        for i in getDatas:
            plt.plot(i[0], i[1], "go")
        plt.xlabel('year')
        plt.xticks(rotation=90)
        plt.ylabel('temperature')
        connect = sqlite3.connect("database.db")
        cursor = connect.execute('select num from Num;')
        getNum = cursor.fetchall()
        num = getNum[0][0]
        cursor.execute('delete from Num where num = ?', (num,))
        connect.commit()
        numstr = str(num)
        boollean = os.path.isfile(
            'C:\\Users\\HP\\PycharmProjects\\Global Warming Project\\static\\thefile' + numstr + '.png')
        if boollean == False:
            pass
        else:
            os.remove('C:\\Users\\HP\\PycharmProjects\\Global Warming Project\\static\\thefile' + numstr + '.png')
        num += 1
        numstr1 = str(num)
        plt.savefig('C:\\Users\\HP\\PycharmProjects\\Global Warming Project\\static\\thefile' + numstr1 + '.png')
        plt.show()
        cursor.execute('insert into Num(num) values (?);', (num,))
        connect.commit()
    elif getMonth == "April":
        for i in getDatas:
            plt.plot(i[0], i[1], "co")
        plt.xlabel('year')
        plt.xticks(rotation=90)
        plt.ylabel('temperature')
        connect = sqlite3.connect("database.db")
        cursor = connect.execute('select num from Num;')
        getNum = cursor.fetchall()
        num = getNum[0][0]
        cursor.execute('delete from Num where num = ?', (num,))
        connect.commit()
        numstr = str(num)
        boollean = os.path.isfile(
            'C:\\Users\\HP\\PycharmProjects\\Global Warming Project\\static\\thefile' + numstr + '.png')
        if boollean == False:
            pass
        else:
            os.remove('C:\\Users\\HP\\PycharmProjects\\Global Warming Project\\static\\thefile' + numstr + '.png')
        num += 1
        numstr1 = str(num)
        plt.savefig('C:\\Users\\HP\\PycharmProjects\\Global Warming Project\\static\\thefile' + numstr1 + '.png')
        plt.show()
        cursor.execute('insert into Num(num) values (?);', (num,))
        connect.commit()
    elif getMonth == "May":
        for i in getDatas:
            plt.plot(i[0], i[1], "bo")
        plt.xlabel('year')
        plt.xticks(rotation=90)
        plt.ylabel('temperature')
        connect = sqlite3.connect("database.db")
        cursor = connect.execute('select num from Num;')
        getNum = cursor.fetchall()
        num = getNum[0][0]
        cursor.execute('delete from Num where num = ?', (num,))
        connect.commit()
        numstr = str(num)
        boollean = os.path.isfile(
            'C:\\Users\\HP\\PycharmProjects\\Global Warming Project\\static\\thefile' + numstr + '.png')
        if boollean == False:
            pass
        else:
            os.remove('C:\\Users\\HP\\PycharmProjects\\Global Warming Project\\static\\thefile' + numstr + '.png')
        num += 1
        numstr1 = str(num)
        plt.savefig('C:\\Users\\HP\\PycharmProjects\\Global Warming Project\\static\\thefile' + numstr1 + '.png')
        plt.show()
        cursor.execute('insert into Num(num) values (?);', (num,))
        connect.commit()
    elif getMonth == "June":
        for i in getDatas:
            plt.plot(i[0], i[1], "mo")
        plt.xlabel('year')
        plt.xticks(rotation=90)
        plt.ylabel('temperature')
        connect = sqlite3.connect("database.db")
        cursor = connect.execute('select num from Num;')
        getNum = cursor.fetchall()
        num = getNum[0][0]
        cursor.execute('delete from Num where num = ?', (num,))
        connect.commit()
        numstr = str(num)
        boollean = os.path.isfile(
            'C:\\Users\\HP\\PycharmProjects\\Global Warming Project\\static\\thefile' + numstr + '.png')
        if boollean == False:
            pass
        else:
            os.remove('C:\\Users\\HP\\PycharmProjects\\Global Warming Project\\static\\thefile' + numstr + '.png')
        num += 1
        numstr1 = str(num)
        plt.savefig('C:\\Users\\HP\\PycharmProjects\\Global Warming Project\\static\\thefile' + numstr1 + '.png')
        plt.show()
        cursor.execute('insert into Num(num) values (?);', (num,))
        connect.commit()
    elif getMonth == "July":
        for i in getDatas:
            plt.plot(i[0], i[1], "r*")
        plt.xlabel('year')
        plt.xticks(rotation=90)
        plt.ylabel('temperature')
        connect = sqlite3.connect("database.db")
        cursor = connect.execute('select num from Num;')
        getNum = cursor.fetchall()
        num = getNum[0][0]
        cursor.execute('delete from Num where num = ?', (num,))
        connect.commit()
        numstr = str(num)
        boollean = os.path.isfile(
            'C:\\Users\\HP\\PycharmProjects\\Global Warming Project\\static\\thefile' + numstr + '.png')
        if boollean == False:
            pass
        else:
            os.remove('C:\\Users\\HP\\PycharmProjects\\Global Warming Project\\static\\thefile' + numstr + '.png')
        num += 1
        numstr1 = str(num)
        plt.savefig('C:\\Users\\HP\\PycharmProjects\\Global Warming Project\\static\\thefile' + numstr1 + '.png')
        plt.show()
        cursor.execute('insert into Num(num) values (?);', (num,))
        connect.commit()
    elif getMonth == "August":
        for i in getDatas:
            plt.plot(i[0], i[1], "y*")
        plt.xlabel('year')
        plt.xticks(rotation=90)
        plt.ylabel('temperature')
        connect = sqlite3.connect("database.db")
        cursor = connect.execute('select num from Num;')
        getNum = cursor.fetchall()
        num = getNum[0][0]
        cursor.execute('delete from Num where num = ?', (num,))
        connect.commit()
        numstr = str(num)
        boollean = os.path.isfile(
            'C:\\Users\\HP\\PycharmProjects\\Global Warming Project\\static\\thefile' + numstr + '.png')
        if boollean == False:
            pass
        else:
            os.remove('C:\\Users\\HP\\PycharmProjects\\Global Warming Project\\static\\thefile' + numstr + '.png')
        num += 1
        numstr1 = str(num)
        plt.savefig('C:\\Users\\HP\\PycharmProjects\\Global Warming Project\\static\\thefile' + numstr1 + '.png')
        plt.show()
        cursor.execute('insert into Num(num) values (?);', (num,))
        connect.commit()
    elif getMonth == "September":
        for i in getDatas:
            plt.plot(i[0], i[1], "g*")
        plt.xlabel('year')
        plt.xticks(rotation=90)
        plt.ylabel('temperature')
        connect = sqlite3.connect("database.db")
        cursor = connect.execute('select num from Num;')
        getNum = cursor.fetchall()
        num = getNum[0][0]
        cursor.execute('delete from Num where num = ?', (num,))
        connect.commit()
        numstr = str(num)
        boollean = os.path.isfile(
            'C:\\Users\\HP\\PycharmProjects\\Global Warming Project\\static\\thefile' + numstr + '.png')
        if boollean == False:
            pass
        else:
            os.remove('C:\\Users\\HP\\PycharmProjects\\Global Warming Project\\static\\thefile' + numstr + '.png')
        num += 1
        numstr1 = str(num)
        plt.savefig('C:\\Users\\HP\\PycharmProjects\\Global Warming Project\\static\\thefile' + numstr1 + '.png')
        plt.show()
        cursor.execute('insert into Num(num) values (?);', (num,))
        connect.commit()
    elif getMonth == "October":
        for i in getDatas:
            plt.plot(i[0], i[1], "c*")
        plt.xlabel('year')
        plt.xticks(rotation=90)
        plt.ylabel('temperature')
        connect = sqlite3.connect("database.db")
        cursor = connect.execute('select num from Num;')
        getNum = cursor.fetchall()
        num = getNum[0][0]
        cursor.execute('delete from Num where num = ?', (num,))
        connect.commit()
        numstr = str(num)
        boollean = os.path.isfile(
            'C:\\Users\\HP\\PycharmProjects\\Global Warming Project\\static\\thefile' + numstr + '.png')
        if boollean == False:
            pass
        else:
            os.remove('C:\\Users\\HP\\PycharmProjects\\Global Warming Project\\static\\thefile' + numstr + '.png')
        num += 1
        numstr1 = str(num)
        plt.savefig('C:\\Users\\HP\\PycharmProjects\\Global Warming Project\\static\\thefile' + numstr1 + '.png')
        plt.show()
        cursor.execute('insert into Num(num) values (?);', (num,))
        connect.commit()
    elif getMonth == "November":
        for i in getDatas:
            plt.plot(i[0], i[1], "b*")
        plt.xlabel('year')
        plt.xticks(rotation=90)
        plt.ylabel('temperature')
        connect = sqlite3.connect("database.db")
        cursor = connect.execute('select num from Num;')
        getNum = cursor.fetchall()
        num = getNum[0][0]
        cursor.execute('delete from Num where num = ?', (num,))
        connect.commit()
        numstr = str(num)
        boollean = os.path.isfile(
            'C:\\Users\\HP\\PycharmProjects\\Global Warming Project\\static\\thefile' + numstr + '.png')
        if boollean == False:
            pass
        else:
            os.remove('C:\\Users\\HP\\PycharmProjects\\Global Warming Project\\static\\thefile' + numstr + '.png')
        num += 1
        numstr1 = str(num)
        plt.savefig('C:\\Users\\HP\\PycharmProjects\\Global Warming Project\\static\\thefile' + numstr1 + '.png')
        plt.show()
        cursor.execute('insert into Num(num) values (?);', (num,))
        connect.commit()
    elif getMonth == "December":
        for i in getDatas:
            plt.plot(i[0], i[1], "m*")
        plt.xlabel('year')
        plt.xticks(rotation=90)
        plt.ylabel('temperature')
        connect = sqlite3.connect("database.db")
        cursor = connect.execute('select num from Num;')
        getNum = cursor.fetchall()
        num = getNum[0][0]
        cursor.execute('delete from Num where num = ?', (num,))
        connect.commit()
        numstr = str(num)
        boollean = os.path.isfile(
            'C:\\Users\\HP\\PycharmProjects\\Global Warming Project\\static\\thefile' + numstr + '.png')
        if boollean == False:
            pass
        else:
            os.remove('C:\\Users\\HP\\PycharmProjects\\Global Warming Project\\static\\thefile' + numstr + '.png')
        num += 1
        numstr1 = str(num)
        plt.savefig('C:\\Users\\HP\\PycharmProjects\\Global Warming Project\\static\\thefile' + numstr1 + '.png')
        plt.show()
        cursor.execute('insert into Num(num) values (?);', (num,))
        connect.commit()

def CreatePlotMeasureCO2(getDatas):
    for i in getDatas:
        tempnum = i[0] % 1
        temptempnum = '{0:.4g}'.format(tempnum)
        strnum = str(temptempnum)
        if strnum == '0':
            plt.plot(i[0], i[1], "ro")
        elif strnum == '0.08333':
            plt.plot(i[0], i[1], "yo")
        elif strnum == '0.1667':
            plt.plot(i[0], i[1], "go")
        elif strnum == '0.25':
            plt.plot(i[0], i[1], "co")
        elif strnum == '0.3333':
            plt.plot(i[0], i[1], "bo")
        elif strnum == '0.4167':
            plt.plot(i[0], i[1], "mo")
        elif strnum == '0.5':
            plt.plot(i[0], i[1], "r*")
        elif strnum == '0.5833':
            plt.plot(i[0], i[1], "y*")
        elif strnum == '0.6667':
            plt.plot(i[0], i[1], "g*")
        elif strnum == '0.75':
            plt.plot(i[0], i[1], "c*")
        elif strnum == '0.8333':
            plt.plot(i[0], i[1], "b*")
        elif strnum == '0.9167':
            plt.plot(i[0], i[1], "m*")
    plt.xlabel('Year')
    plt.xticks(rotation=90)
    plt.ylabel('CO2 level')
    connect = sqlite3.connect("database.db")
    cursor = connect.execute('select num from Num;')
    getNum = cursor.fetchall()
    num = getNum[0][0]
    cursor.execute('delete from Num where num = ?', (num,))
    connect.commit()
    numstr = str(num)
    boollean = os.path.isfile(
        'C:\\Users\\HP\\PycharmProjects\\Global Warming Project\\static\\thefile' + numstr + '.png')
    if boollean == False:
        pass
    else:
        os.remove('C:\\Users\\HP\\PycharmProjects\\Global Warming Project\\static\\thefile' + numstr + '.png')
    num += 1
    numstr1 = str(num)
    plt.savefig('C:\\Users\\HP\\PycharmProjects\\Global Warming Project\\static\\thefile' + numstr1 + '.png')
    plt.show()
    cursor.execute('insert into Num(num) values (?);', (num,))
    connect.commit()