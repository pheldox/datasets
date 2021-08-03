# -*- coding: utf-8 -*-
import urllib.request as request
import csv
from os import mkdir
from os.path import exists, join
from bs4 import BeautifulSoup

datadir = "data"
if not exists(datadir):
    mkdir(datadir)

source = "https://en.wikipedia.org/wiki/Road_safety_in_Europe"
 
def extract():
    text = request.urlopen(source)
    soup = BeautifulSoup(text,"html.parser")
    table = soup.find("table",{"class": "wikitable sortable"})
    
    
    header = table.findAll("th")
    if header[0].text.rstrip() != "Country":
        raise Exception("Can't parse Wikipedia's table!")

    getdata = []
    rows = table.findAll("tr")
    for row in rows:
        fields = row.findAll("td")
        if fields:
            country = fields[0].text.rstrip()
            year = "2018"
            area = fields[1].text.rstrip()
            population = fields[2].text.rstrip()
            gdp = fields[3].text.rstrip()
            popdensity = fields[4].text.rstrip()
            vehicleowners = fields[5].text.rstrip()
            roaddeaths = fields[7].text.rstrip()
            deathspermillion = fields[8].text.rstrip()
            
            getdata.append([country, year,area,population,gdp,popdensity,vehicleowners,roaddeaths,deathspermillion])
            
            header = ["Country","Year","Area(1000km sq)","Population","GDP per capita","Population Density(Inhabitants per km sq.2017)","Vehicle Ownership(per 1000 inhabitants,2016)","Total Road Deaths","Road deaths per Million Inhabitants"]
            
            writer = csv.writer(
                open("./data/roadsafety.csv","w"), lineterminator="\n"
                )
            writer.writerow(header)
            getdata.sort(key=lambda s: s[8].lower())
            writer.writerows(getdata)



if __name__ == "__main__":
    extract()
