from flask import Flask, render_template, request, redirect
import getTemperature, cleanForApp, searchQuery, graphPlot, tableChart

app = Flask(__name__)

getTemperature.get_data()

seatMonth = "None"
seatCF = "None"
seatFrom = 0
seatTo = 0

earthSource = "None"
earthMonth = "None"
earthCF = "None"
earthFrom = "None"
earthTo = "None"

co2FromMonth = "None"
co2ToMonth = "None"
co2FromYear = "None"
co2ToYear = "None"

sealFromMonth = "None"
sealToMonth = "None"
sealFromYear = "None"
sealToYear = "None"


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route('/seatemp', methods=['POST', 'GET'])
def seatemp():
    global seatMonth
    global seatCF
    global seatTo
    global seatFrom
    getYears = searchQuery.theYears()
    getCF = "None"
    getTableDatas = None
    if request.method == "POST":
        getMonth = request.form['monthlist']
        seatMonth = getMonth
        getCF = request.form['temperature']
        seatCF = getCF
        toYear = request.form['toYear']
        seatTo = int(toYear)
        fromYear = request.form['fromYear']
        seatFrom = int(fromYear)
        getDatas = cleanForApp.OceanTemp(getMonth, getCF, toYear, fromYear)
        getTableDatas = tableChart.tableSeaTemp(getMonth, getCF, toYear, fromYear)
        if not getTableDatas:
            return redirect('/seatemp')
        graphPlot.CreatePlotTemp(getDatas, getMonth)
    num = searchQuery.getNum()
    return render_template('seatemp.html', getYears=getYears, table=getTableDatas, getCF=getCF, num=num, seatMonth=seatMonth, seatCF=seatCF, seatTo=seatTo, seatFrom=seatFrom)


@app.route('/earthtemp', methods=['POST', 'GET'])
def earthtemp():
    getCF = "None"
    revertedDatas = None
    getYears = searchQuery.theYearsEarth()
    global earthSource
    global earthMonth
    global earthCF
    global earthFrom
    global earthTo
    if request.method == "POST":
        getSource = request.form['source']
        earthSource = getSource
        getMonth = request.form['monthlist']
        earthMonth = getMonth
        getCF = request.form['temperature']
        earthCF = getCF
        toYear = request.form['toYear']
        earthTo = int(toYear)
        fromYear = request.form['fromYear']
        earthFrom = int(fromYear)
        getDatas = cleanForApp.EarthTemp(getMonth, getCF, toYear, fromYear, getSource)
        getTableDatas = tableChart.tableEarthTemp(getMonth, getCF, toYear, fromYear, getSource)
        if not getTableDatas:
            return redirect('/earthtemp')
        revertedDatas = getTableDatas[::-1]
        graphPlot.CreatePlotTemp(getDatas, getMonth)
    num = searchQuery.getNum()
    return render_template('earthtemp.html', getYears=getYears, table=revertedDatas, getCF=getCF, num=num, earthSource=earthSource, earthMonth=earthMonth, earthCF=earthCF, earthFrom=earthFrom, earthTo=earthTo)


@app.route('/co2', methods=['POST', 'GET'])
def co2():
    getMonths = searchQuery.theMonthsSeaLevel()
    getYears = searchQuery.theYearsCO2()
    getTableDatas = "None"
    global co2FromMonth
    global co2ToMonth
    global co2FromYear
    global co2ToYear
    if request.method == "POST":
        fromMonth = request.form['fromMonth']
        co2FromMonth = fromMonth
        fromYear = request.form['fromYear']
        co2FromYear = int(fromYear)
        toMonth = request.form['toMonth']
        co2ToMonth = toMonth
        toYear = request.form['toYear']
        co2ToYear = int(toYear)
        getDatas = cleanForApp.CO2(fromMonth, fromYear, toMonth, toYear)
        getTableDatas = tableChart.tableCO2(fromMonth, fromYear, toMonth, toYear)
        if not getTableDatas:
            return redirect('/co2')
        graphPlot.CreatePlotMeasureCO2(getDatas)
    num = searchQuery.getNum()
    return render_template('co2.html', getMonths=getMonths, getYears=getYears, table=getTableDatas, num=num, co2FromMonth=co2FromMonth, co2FromYear=co2FromYear, co2ToMonth=co2ToMonth, co2ToYear=co2ToYear)


@app.route('/sealevel', methods=['POST', 'GET'])
def sealevel():
    getMonths = searchQuery.theMonthsSeaLevel()
    getYears = searchQuery.theYearsSeaLevel()
    getTableDatas = "None"
    global sealFromMonth
    global sealToMonth
    global sealFromYear
    global sealToYear
    if request.method == "POST":
        fromMonth = request.form['fromMonth']
        sealFromMonth = fromMonth
        fromYear = request.form['fromYear']
        sealFromYear = int(fromYear)
        toMonth = request.form['toMonth']
        sealToMonth = toMonth
        toYear = request.form['toYear']
        sealToYear = int(toYear)
        getDatas = cleanForApp.SeaLevel(fromMonth, fromYear, toMonth, toYear)
        getTableDatas = tableChart.tableSeaLevel(fromMonth, fromYear, toMonth, toYear)
        if not getTableDatas:
            return redirect('/sealevel')
        graphPlot.CreatePlotMeasureSL(getDatas)
    num = searchQuery.getNum()
    return render_template('sealevel.html', getMonths=getMonths, getYears=getYears, table=getTableDatas, num=num, sealFromYear=sealFromYear, sealFromMonth=sealFromMonth, sealToMonth=sealToMonth, sealToYear=sealToYear)


if __name__ == '__main__':
    app.run()


