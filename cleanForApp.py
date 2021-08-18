import searchQuery


def OceanTemp(getMonth, getCF, toYear, fromYear):
    if getMonth == "January":
        theMonth = "Jan"
        getDatas = searchQuery.OceanTemp(theMonth, getCF, toYear, fromYear)
    elif getMonth == "February":
        theMonth = "Feb"
        getDatas = searchQuery.OceanTemp(theMonth, getCF, toYear, fromYear)
    elif getMonth == "March":
        theMonth = "Mar"
        getDatas = searchQuery.OceanTemp(theMonth, getCF, toYear, fromYear)
    elif getMonth == "April":
        theMonth = "Apr"
        getDatas = searchQuery.OceanTemp(theMonth, getCF, toYear, fromYear)
    elif getMonth == "May":
        theMonth = "May"
        getDatas = searchQuery.OceanTemp(theMonth, getCF, toYear, fromYear)
    elif getMonth == "June":
        theMonth = "Jun"
        getDatas = searchQuery.OceanTemp(theMonth, getCF, toYear, fromYear)
    elif getMonth == "July":
        theMonth = "Jul"
        getDatas = searchQuery.OceanTemp(theMonth, getCF, toYear, fromYear)
    elif getMonth == "August":
        theMonth = "Aug"
        getDatas = searchQuery.OceanTemp(theMonth, getCF, toYear, fromYear)
    elif getMonth == "September":
        theMonth = "Sep"
        getDatas = searchQuery.OceanTemp(theMonth, getCF, toYear, fromYear)
    elif getMonth == "October":
        theMonth = "Oct"
        getDatas = searchQuery.OceanTemp(theMonth, getCF, toYear, fromYear)
    elif getMonth == "November":
        theMonth = "Nov"
        getDatas = searchQuery.OceanTemp(theMonth, getCF, toYear, fromYear)
    elif getMonth == "December":
        theMonth = "Dec"
        getDatas = searchQuery.OceanTemp(theMonth, getCF, toYear, fromYear)
    else:
        theMonth = "All"
        getDatas = searchQuery.OceanTemp(theMonth, getCF, toYear, fromYear)
    return getDatas


def EarthTemp(getMonth, getCF, toYear, fromYear, getSource):
    if getMonth == "January":
        theMonth = "01"
        getDatas = searchQuery.EarthTemp(theMonth, getCF, toYear, fromYear, getSource)
    elif getMonth == "February":
        theMonth = "02"
        getDatas = searchQuery.EarthTemp(theMonth, getCF, toYear, fromYear, getSource)
    elif getMonth == "March":
        theMonth = "03"
        getDatas = searchQuery.EarthTemp(theMonth, getCF, toYear, fromYear, getSource)
    elif getMonth == "April":
        theMonth = "04"
        getDatas = searchQuery.EarthTemp(theMonth, getCF, toYear, fromYear, getSource)
    elif getMonth == "May":
        theMonth = "05"
        getDatas = searchQuery.EarthTemp(theMonth, getCF, toYear, fromYear, getSource)
    elif getMonth == "June":
        theMonth = "06"
        getDatas = searchQuery.EarthTemp(theMonth, getCF, toYear, fromYear, getSource)
    elif getMonth == "July":
        theMonth = "07"
        getDatas = searchQuery.EarthTemp(theMonth, getCF, toYear, fromYear, getSource)
    elif getMonth == "August":
        theMonth = "08"
        getDatas = searchQuery.EarthTemp(theMonth, getCF, toYear, fromYear, getSource)
    elif getMonth == "September":
        theMonth = "09"
        getDatas = searchQuery.EarthTemp(theMonth, getCF, toYear, fromYear, getSource)
    elif getMonth == "October":
        theMonth = "10"
        getDatas = searchQuery.EarthTemp(theMonth, getCF, toYear, fromYear, getSource)
    elif getMonth == "November":
        theMonth = "11"
        getDatas = searchQuery.EarthTemp(theMonth, getCF, toYear, fromYear, getSource)
    elif getMonth == "December":
        theMonth = "12"
        getDatas = searchQuery.EarthTemp(theMonth, getCF, toYear, fromYear, getSource)
    else:
        theMonth = "All"
        getDatas = searchQuery.EarthTemp(theMonth, getCF, toYear, fromYear, getSource)
    return getDatas


def SeaLevel(fromMonth, fromYear, toMonth, toYear):
    theMonth = None
    if fromMonth == "January":
        theMonth = "01"
    elif fromMonth == "February":
        theMonth = "02"
    elif fromMonth == "March":
        theMonth = "03"
    elif fromMonth == "April":
        theMonth = "04"
    elif fromMonth == "May":
        theMonth = "05"
    elif fromMonth == "June":
        theMonth = "06"
    elif fromMonth == "July":
        theMonth = "07"
    elif fromMonth == "August":
        theMonth = "08"
    elif fromMonth == "September":
        theMonth = "09"
    elif fromMonth == "October":
        theMonth = "10"
    elif fromMonth == "November":
        theMonth = "11"
    elif fromMonth == "December":
        theMonth = "12"
    thetoMonth = None
    if toMonth == "January":
        thetoMonth = "01"
    elif toMonth == "February":
        thetoMonth = "02"
    elif toMonth == "March":
        thetoMonth = "03"
    elif toMonth == "April":
        thetoMonth = "04"
    elif toMonth == "May":
        thetoMonth = "05"
    elif toMonth == "June":
        thetoMonth = "06"
    elif toMonth == "July":
        thetoMonth = "07"
    elif toMonth == "August":
        thetoMonth = "08"
    elif toMonth == "September":
        thetoMonth = "09"
    elif toMonth == "October":
        thetoMonth = "10"
    elif toMonth == "November":
        thetoMonth = "11"
    elif toMonth == "December":
        thetoMonth = "12"
    getDatas = searchQuery.SeaLevel(theMonth, fromYear, thetoMonth, toYear)
    return getDatas


def CO2(fromMonth, fromYear, toMonth, toYear):
    theMonth = None
    if fromMonth == "January":
        theMonth = "01"
    elif fromMonth == "February":
        theMonth = "02"
    elif fromMonth == "March":
        theMonth = "03"
    elif fromMonth == "April":
        theMonth = "04"
    elif fromMonth == "May":
        theMonth = "05"
    elif fromMonth == "June":
        theMonth = "06"
    elif fromMonth == "July":
        theMonth = "07"
    elif fromMonth == "August":
        theMonth = "08"
    elif fromMonth == "September":
        theMonth = "09"
    elif fromMonth == "October":
        theMonth = "10"
    elif fromMonth == "November":
        theMonth = "11"
    elif fromMonth == "December":
        theMonth = "12"
    thetoMonth = None
    if toMonth == "January":
        thetoMonth = "01"
    elif toMonth == "February":
        thetoMonth = "02"
    elif toMonth == "March":
        thetoMonth = "03"
    elif toMonth == "April":
        thetoMonth = "04"
    elif toMonth == "May":
        thetoMonth = "05"
    elif toMonth == "June":
        thetoMonth = "06"
    elif toMonth == "July":
        thetoMonth = "07"
    elif toMonth == "August":
        thetoMonth = "08"
    elif toMonth == "September":
        thetoMonth = "09"
    elif toMonth == "October":
        thetoMonth = "10"
    elif toMonth == "November":
        thetoMonth = "11"
    elif toMonth == "December":
        thetoMonth = "12"
    getDatas = searchQuery.CO2(theMonth, fromYear, thetoMonth, toYear)
    return getDatas