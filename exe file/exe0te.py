import pandas 
import numpy 
import matplotlib.pyplot as plt

import time 
import datetime

class KPI:
    def __init__(self):
        now_date = str(datetime.datetime.now())

        self.year = now_date[:4] # year 
        self.month = now_date[5:7] # month 
        self.day = now_date[8:10] # day 
        self.hour = now_date[11:13] # hour

    def createPlotData(self):
        URL = "https://finance.naver.com//sise/sise_index_time.naver?code=KPI200&thistime=%s%s%s%s" % (self.year, self.month, self.day, self.hour) 
        KPI_table = pandas.read_html(URL)[0].dropna()

        self.time_data = numpy.flip(KPI_table["체결시각"].values)
        self.price_data = numpy.flip(KPI_table["체결가"].values)
    
        

    def drawPlot(self):
        self.createPlotData()

        print("시세 갱신 - %s - %s - %s - %s - %s" % (self.year, self.month, self.day, self.hour, self.time_data[5]))
        
        plt.rc("font", family = "Malgun Gothic")

        plt.plot(self.time_data, self.price_data)

        plt.title("시간별시세 %s - %s - %s\n%s ~ %s" % (self.year, self.month, self.day, self.time_data[0], self.time_data[5]))

        plt.xlabel("체결시각")
        plt.ylabel("체결가")

        plt.pause(5)
        plt.clf()

kpi = KPI()

while True:
    kpi.drawPlot()
