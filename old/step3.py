import pandas as pd

geo_data = pd.read_csv("C:\\Users\\KB\\Desktop\\김홍근프로\\Raw_DATA\\Goemetry.csv", encoding='cp949')
mal_data = pd.read_csv("C:\\Users\\KB\\Desktop\\김홍근프로\\Raw_DATA\\step2.csv", encoding='cp949')

def Geometry_Find(line):
    long, lati, co = [], [], []

    co = geo_data['국가코드']
    long = geo_data['Longitude']
    lati = geo_data['Latitude']

    for co_code, longi, lati in zip(co, long, lati):
        if line == co_code:
            lo = longi
            la = lati
            return [lo, la]

    return [0.0000000, 0.000000]

def write_geo():
    co = mal_data['Co_code']
    geo1, longit, latit = [], [], []
    for line in co:
        geo1.append(Geometry_Find(line))

    for i in range(len(geo1)):
        longit.append(geo1[i][0])
        latit.append(geo1[i][1])

    mal_data['Longitude'] = longit
    mal_data['Latitude'] = latit

write_geo()

print(mal_data)
statics = mal_data['Co_code'].value_counts()
statics.to_csv("C:\\Users\\KB\\Desktop\\김홍근프로\\Raw_DATA\\Step4.csv", encoding='cp949')

mal_data.to_csv("C:\\Users\\KB\\Desktop\\김홍근프로\\Raw_DATA\\Step3.csv", encoding='cp949')